import asyncio
from concurrent.futures import ThreadPoolExecutor
from logging.handlers import RotatingFileHandler
import sys
import logging
import os
import cv2
from queue import Queue
from datetime import datetime as dt 
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QFileDialog,
    QMessageBox, QSystemTrayIcon,QMenu
)
from PyQt5.QtGui import QIcon, QColor
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from ftp_config import FTPConfigWindow


Base = declarative_base()

class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    rtsp_url = Column(String(200), nullable=False)
    save_path = Column(String(200), nullable=False)
    interval = Column(Integer, nullable=False, default=60)
    active = Column(Boolean, nullable=False, default=False)

    
class RTSPMonitor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.engine = create_engine('sqlite:///rtsp_data.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        self.current_device = None
        self.streaming_thread = None
        self.device_streams = {}
        self.device_threads = {}
        
        self.thread_pool = ThreadPoolExecutor(max_workers=10)  # Максимальна кількість одночасних потоків
        self.frame_queues = {} # Черга для передачі кадрів між потоками
        self.frame_queue_locks = {}
        self.start_times = {}  # Словник для збереження початкового часу моніторингу
        self.ftp_config_window = FTPConfigWindow()  # Створюємо екземпляр FTPConfigWindow
        self.ftp = None


        self.init_ui()
        self.load_devices()
        self.refresh_device_list()
        
        # Максимальний розмір файлу в байтах (20 МБ)
        max_log_size = 20 * 1024 * 1024  

        # Створюємо об'єкт RotatingFileHandler
        handler = RotatingFileHandler('RTSPMonitor.txt', maxBytes=max_log_size, backupCount=5)

        # Конфігуруємо рівень логування та обробник
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[handler])


    def init_ui(self):
        self.setWindowTitle("RTSP Monitor")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QHBoxLayout()

        self.tray_icon = QSystemTrayIcon(QIcon("main_icon.ico"), self)
        # self.tray_icon.setWindowIcon(QIcon('main_icon.ico'))  #  шлях до вашої іконки
        self.tray_icon.setToolTip("RTSP Monitor")
        self.tray_icon.activated.connect(self.tray_icon_clicked)
                
        # Створюємо контекстне меню для іконки в системному лотку
        tray_menu = QMenu()
        exit_action = tray_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        self.tray_icon.setContextMenu(tray_menu)
        
        self.tray_icon.show()

        # Left side - Input Form
        self.input_form_layout = QVBoxLayout()
        self.rtsp_label = QLabel("RTSP URL:")
        self.rtsp_input = QLineEdit()
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.save_path_label = QLabel("Save Path:")
        self.save_path_input = QLineEdit()
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        self.interval_label = QLabel("Interval (seconds):")
        self.interval_input = QLineEdit()
        self.interval_input.setText("60")  # Значення за замовчуванням
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_device)

        # Створюємо кнопку для відкриття вікна конфігурації FTP
        self.ftp_config_button = QPushButton("Open FTP Config")
        self.ftp_config_button.clicked.connect(self.open_ftp_config_window)
        
        self.select_folder_button = QPushButton("Select Folder")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.input_form_layout.addWidget(self.rtsp_label)
        self.input_form_layout.addWidget(self.rtsp_input)
        self.input_form_layout.addWidget(self.name_label)
        self.input_form_layout.addWidget(self.name_input)
        self.input_form_layout.addWidget(self.save_path_label)
        self.input_form_layout.addWidget(self.select_folder_button)
        self.input_form_layout.addWidget(self.save_path_input)
        self.input_form_layout.addWidget(self.interval_label)
        self.input_form_layout.addWidget(self.interval_input)
        self.input_form_layout.addWidget(self.add_button)
        self.input_form_layout.addWidget(self.ftp_config_button)
        self.input_form_layout.addStretch()

        # Right side - Device List
        self.device_list_layout = QVBoxLayout()
        self.device_list_label = QLabel("Devices:")
        self.device_list = QTableWidget()
        self.device_list.setColumnCount(4)
        self.device_list.setHorizontalHeaderLabels(["Name", "RTSP URL", "Save Path", "Status"])
        self.device_list.horizontalHeader().setStretchLastSection(True)
        self.device_list.cellClicked.connect(self.select_device)

        self.change_button = QPushButton("Change")
        self.delete_button = QPushButton("Delete")
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

        self.change_button.clicked.connect(self.change_device)
        self.delete_button.clicked.connect(self.delete_device)
        self.start_button.clicked.connect(self.start_monitoring)
        self.stop_button.clicked.connect(self.stop_monitoring)

        self.device_list_layout.addWidget(self.device_list_label)
        self.device_list_layout.addWidget(self.device_list)
        self.device_list_layout.addWidget(self.change_button)
        self.device_list_layout.addWidget(self.delete_button)
        self.device_list_layout.addWidget(self.start_button)
        self.device_list_layout.addWidget(self.stop_button)

        self.main_layout.addLayout(self.input_form_layout)
        self.main_layout.addLayout(self.device_list_layout)

        self.central_widget.setLayout(self.main_layout)
        

        # Load devices from database
        self.load_devices()

    def open_ftp_config_window(self):
        #self.ftp_config_window = FTPConfigWindow()
        self.ftp_config_window.show()
        
    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.save_path_input.setText(folder_path)

    def add_device(self):
        rtsp_url = self.rtsp_input.text()
        name = self.name_input.text()
        save_path = self.save_path_input.text()
        interval = int(self.interval_input.text()) if self.interval_input.text().isdigit() else 60

        if not rtsp_url or not name or not save_path:
            QMessageBox.warning(self, "Warning", "RTSP URL, Name, and Save Path are required fields.")
            return

        if self.is_duplicate_device(rtsp_url, name):
            QMessageBox.warning(self, "Error", "A device with the same RTSP URL or name already exists.")
            return

        try:
            cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)
            if not cap.isOpened():
                QMessageBox.warning(self, "Error", "Failed to open RTSP stream.")
                return
            cap.release()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error while accessing RTSP stream: {e}")
            return

        try:
            new_device = Device(name=name, rtsp_url=rtsp_url, save_path=save_path, interval=interval, active=False)
            self.session.add(new_device)
            self.session.commit()
            self.load_devices()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error while saving device data: {e}")

        self.refresh_device_list()

    def delete_device(self):
        if self.current_device:
            self.session.delete(self.current_device)
            self.session.commit()
            self.current_device = None
            self.load_devices()

        self.refresh_device_list()

    def change_device(self):
        if self.current_device:
            new_name = self.name_input.text()
            new_rtsp_url = self.rtsp_input.text()
            new_save_path = self.save_path_input.text()
            new_interval = int(self.interval_input.text()) if self.interval_input.text().isdigit() else 60

            # Перевірка на дублікати
            if self.is_duplicate_device(new_rtsp_url, new_name, exclude_id=self.current_device.id):
                QMessageBox.warning(self, "Error", "A device with the same RTSP URL or name already exists.")
                return

            self.current_device.name = new_name
            self.current_device.rtsp_url = new_rtsp_url
            self.current_device.save_path = new_save_path
            self.current_device.interval = new_interval

            self.session.commit()
            self.load_devices()
            self.current_device = None

        self.refresh_device_list()

    def has_active_devices(self):
        return self.session.query(Device).filter(Device.active == True).count() > 0
    
    def start_monitoring(self):
        if self.current_device:
            self.current_device.active = True
            
            if self.ftp is None and self.has_active_devices():
                self.ftp = self.ftp_config_window.connect_to_ftp()
                        
            self.session.commit()

            self.frame_queues[self.current_device.id] = Queue()  # Створити чергу для поточного пристрою
            self.start_times[self.current_device.id] = dt.now()  # Збереження початкового часу
            self.thread_pool.submit(self.run_async_task, self.current_device)
            logging.info(f"Monitoring started for device {self.current_device.name}")


        self.refresh_device_list()

    def run_async_task(self, device):
        asyncio.run(self.start_streaming(device))

    async def start_streaming(self, device):
        logging.info(f"Starting streaming for device {device.name}")
        try:
            cap = cv2.VideoCapture(device.rtsp_url, cv2.CAP_FFMPEG)
            while cap.isOpened() and device.active:
                ret, frame = cap.read()
                if ret:
                    if self.frame_queues[device.id].qsize() >= 2:
                        self.frame_queues[device.id].get()  # Видалити найстаріший кадр з черги
                    current_time = dt.now()
                    start_time = self.start_times.get(device.id)
                    if start_time and (current_time - start_time).seconds >= device.interval:
                        self.start_times[device.id] = current_time  # Оновити час старту для порівняння
                        self.frame_queues[device.id].put(frame)  # Покласти новий кадр у чергу потоку
                        await self.save_frames(device)
                else:
                    logging.error(f"Failed to capture frame from - {device.name}, {device.rtsp_url}")
                    self.stop_monitoring
            cap.release()
        except Exception as e:
            logging.error(f"Error while reading RTSP stream for device {device.name}: {e}")
            cap.release()
    
    def stop_monitoring(self):
        if self.current_device:
            self.current_device.active = False
            self.session.commit()

            device_id = self.current_device.id
            if device_id in self.device_streams:
                self.device_streams[device_id].join()  # Зупинити потік для цього пристрою
                logging.info(f"Monitoring stoped for device {self.current_device.name}")
                
            if not self.has_active_devices():
                self.ftp_config_window.disconnect_from_ftp(self.ftp)
                print('Disconnected')
            else:
                print('have active device')
                
        self.refresh_device_list()
   
    async def save_frames(self, device):
        try:
            frame_queue = self.frame_queues[device.id]
            if frame_queue.qsize() > 0:
                frame = frame_queue.queue[-1]
                await self.async_save_frame(frame, device.name, device.save_path, device)
                frame_queue.queue.clear() # Очистити чергу після збереження
            else:
                logging.error(f"No frames in queue for {device.name}")
        except Exception as e:
            logging.error(f"Error while saving frame for device {device.name}: {e}")

    async def async_save_frame(self, frame, device_name, save_path, device):
        try:
            current_time = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
            image_name = f"{device_name}_{current_time}.jpg"
            image_path = os.path.join(save_path, image_name)
            if save_path:
                cv2.imwrite(image_path, frame)
                logging.info(f'Save picture from device {device_name} to path - {image_path}')
                if self.ftp_config_window:
                    self.ftp_config_window.send_photo_from_path(self.ftp, device) # Виклик методу send_photo з FTPConfigWindow
            else:
                if self.ftp_config_window:
                    self.ftp_config_window.send_photo_from_buffer(self.ftp, frame, image_name) # Виклик методу send_photo з FTPConfigWindow
        except Exception as e:
            logging.error(f"Error in device {device_name}: {e}")

    def select_device(self, row, col):
        self.current_device = self.devices[row]
        self.name_input.setText(self.current_device.name)
        self.rtsp_input.setText(self.current_device.rtsp_url)
        self.save_path_input.setText(self.current_device.save_path)
        self.interval_input.setText(str(self.current_device.interval))

    def load_devices(self):
        self.devices = self.session.query(Device).all()
        self.refresh_device_list()

    def refresh_device_list(self):
        self.device_list.clearContents()
        self.device_list.setRowCount(len(self.devices)) 
        for row, device in enumerate(self.devices):
            self.device_list.setItem(row, 0, QTableWidgetItem(device.name))
            self.device_list.setItem(row, 1, QTableWidgetItem(device.rtsp_url))

            if not self.device_list.item(row, 2):
                save_path_item = QTableWidgetItem(device.save_path)
                self.device_list.setItem(row, 2, save_path_item)

            status_item = QTableWidgetItem("Active" if device.active else "Inactive")
            status_item.setBackground(QColor(0, 255, 0) if device.active else QColor(255, 255, 255))
            self.device_list.setItem(row, 3, status_item)

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show() 
            self.tray_icon.hide()

    def stop_all_streams(self):
        for device in self.devices:
            if device.active:
                device.active = False
                self.session.commit()
                self.current_device = None

    def closeEvent(self, event):
        self.stop_all_streams()
        super().closeEvent(event)
        if self.ftp is not None:
            self.ftp_config_window.disconnect_from_ftp(self.ftp)
        else:
            pass

    def is_duplicate_device(self, rtsp_url, name, exclude_id=None):
        if exclude_id is not None:
            device_with_rtsp = self.session.query(Device).filter(Device.id != exclude_id, Device.rtsp_url == rtsp_url).first()
            device_with_name = self.session.query(Device).filter(Device.id != exclude_id, Device.name == name).first()
        else:
            device_with_rtsp = self.session.query(Device).filter(Device.rtsp_url == rtsp_url).first()
            device_with_name = self.session.query(Device).filter(Device.name == name).first()

        return device_with_rtsp or device_with_name 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RTSPMonitor()
    window.show()
    sys.exit(app.exec_())
    