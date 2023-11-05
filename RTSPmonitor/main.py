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
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, 
    QLabel,QPushButton, QTableWidget, QMessageBox, QSystemTrayIcon, QMenu, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QColor

from include.utils import Utils
from include.ftp_config import FTPConfigWindow
from include.add_device import AddDeviceWindow

from db.database import DataBase, Device
    
class RTSPMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.db = DataBase()
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
        
        self.devices = []
        self.utils.load_device_list()
        
        # Максимальний розмір файлу в байтах (20 МБ)
        max_log_size = 20 * 1024 * 1024  

        # Створюємо об'єкт RotatingFileHandler
        handler_RTSOmonitor = RotatingFileHandler('log/RTSPMonitor_log.txt', maxBytes=max_log_size, backupCount=5)

        # Конфігуруємо рівень логування та обробник
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[handler_RTSOmonitor])


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

        # Left side - Input Form
        self.input_form_layout = QVBoxLayout()
        self.add_device_window_button = QPushButton("Add device")
        self.add_device_window_button.clicked.connect(self.open_add_device_window)

        # Додайте інші віджети до розміщення
        self.input_form_layout.addWidget(self.add_device_window_button)
        self.input_form_layout = QVBoxLayout()

        # Створюємо кнопку для відкриття вікна конфігурації FTP
        self.ftp_config_button = QPushButton("Open FTP Config")
        self.ftp_config_button.clicked.connect(self.open_ftp_config_window)
        
        self.input_form_layout.addWidget(self.ftp_config_button)
        self.input_form_layout.addStretch()
        
        # Створюємо кнопку для відкриття вікна конфігурації FTP
        self.add_device_button = QPushButton("Add device")
        self.add_device_button.clicked.connect(self.open_add_device_window)
        
        self.input_form_layout.addWidget(self.add_device_button)
        self.input_form_layout.addStretch()

        self.main_layout.addLayout(self.input_form_layout)
        self.main_layout.addLayout(self.device_list_layout)

        self.central_widget.setLayout(self.main_layout)
        
        self.add_device_window = AddDeviceWindow(self.device_list)  # Ініціалізуємо AddDeviceWindow
        self.utils = Utils(self.device_list)
        # Load devices from database
        self.utils.load_device_list()
        
    def open_ftp_config_window(self):
        #self.ftp_config_window = FTPConfigWindow()
        self.ftp_config_window.show()
    
    def open_add_device_window(self):
        self.add_device_window.show()

    def delete_device(self):
        if self.current_device:
            self.db.session.delete(self.current_device)
            self.db.session.commit()
            self.current_device = None
            self.utils.load_device_list()

        self.utils.load_device_list()

    def change_device(self):
        if self.current_device:
            new_name = self.name_input.text()
            new_rtsp_url = self.rtsp_input.text()
            new_save_path = self.save_path_input.text()
            new_interval = int(self.interval_input.text()) if self.interval_input.text().isdigit() else 60

            # Перевірка на дублікати
            if self.utils.is_duplicate_device(new_rtsp_url, new_name, exclude_id=self.current_device.id):
                QMessageBox.warning(self, "Error", "A device with the same RTSP URL or name already exists.")
                return

            self.current_device.name = new_name
            self.current_device.rtsp_url = new_rtsp_url
            self.current_device.save_path = new_save_path
            self.current_device.interval = new_interval

            self.db.session.commit()
            self.utils.load_device_list()
            self.current_device = None

        self.utils.load_device_list()

    def has_active_devices(self):
        return self.db.session.query(Device).filter(Device.active == True).count() > 0
    
    def start_monitoring(self):
        if self.current_device:
            self.current_device.active = True
            
            if self.ftp is None and self.has_active_devices():
                self.ftp = self.ftp_config_window.connect_to_ftp()
                        
            self.db.session.commit()

            self.frame_queues[self.current_device.id] = Queue()  # Створити чергу для поточного пристрою
            self.start_times[self.current_device.id] = dt.now()  # Збереження початкового часу
            self.thread_pool.submit(self.run_async_task, self.current_device)
            logging.info(f"Monitoring started for device {self.current_device.name}")
        
        self.change_status()
        self.utils.load_device_list()

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
            self.db.session.commit()

            device_id = self.current_device.id
            if device_id in self.device_streams:
                self.device_streams[device_id].join()  # Зупинити потік для цього пристрою
                logging.info(f"Monitoring stoped for device {self.current_device.name}")
                
            if not self.has_active_devices():
                self.ftp_config_window.disconnect_from_ftp(self.ftp)
                print('Disconnected')
            else:
                print('have active device')
        self.change_status()
        self.utils.load_device_list()
   
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

    def tray_icon_clicked(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.show() 
            self.tray_icon.hide()

    def stop_all_streams(self):
        for device in self.devices:
            if device.active:
                device.active = False
                self.db.session.commit()
                self.current_device = None

    def closeEvent(self, event):
        self.stop_all_streams()
        super().closeEvent(event)
        if self.ftp is not None:
            self.ftp_config_window.disconnect_from_ftp(self.ftp)
        else:
            pass

    def select_device(self, row):
        self.devices = self.db.session.query(Device).all()
        if self.devices and row < len(self.devices):
            self.current_device = self.devices[row]
        else:
            self.current_device = None
            
    def change_status(self):
        for row, device in enumerate(self.devices):
            status_item = QTableWidgetItem("Active" if device.active else "Inactive")
            status_item.setBackground(QColor(0, 255, 0) if device.active else QColor(255, 255, 255))
            self.device_list.setItem(row, 3, status_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RTSPMonitor()
    window.show()
    sys.exit(app.exec_())
    