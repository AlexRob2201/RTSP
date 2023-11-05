from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
import cv2
import os

from include.utils import Utils
from db.database import Device, DataBase


class AddDeviceWindow(QDialog):
    def __init__(self, device_list):
        super().__init__()
        
        self.db = DataBase()
        self.utils = Utils(device_list)

        self.setWindowTitle("Add Device")
        self.setGeometry(100, 100, 400, 250)

        self.layout = QVBoxLayout()

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

        self.layout.addWidget(self.rtsp_label)
        self.layout.addWidget(self.rtsp_input)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.save_path_label)
        self.layout.addWidget(self.save_path_input)
        self.layout.addWidget(self.select_folder_button)
        self.layout.addWidget(self.interval_label)
        self.layout.addWidget(self.interval_input)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.check_directory_permissions(folder_path)
            self.save_path_input.setText(folder_path)
            
    def check_directory_permissions(self, save_path):
        if os.access(save_path, os.R_OK):
            print(f"Можна читати каталог {save_path}")
        else:
            print(f"Немає доступу до читання каталогу {save_path}")

        if os.access(save_path, os.W_OK):
            print(f"Можна писати в каталог {save_path}")
        else:
            print(f"Немає доступу до запису в каталог {save_path}")

        if os.access(save_path, os.X_OK):
            print(f"Можна виконувати файли в каталозі {save_path}")
        else:
            print(f"Немає доступу до виконання файлів у каталозі {save_path}")

    def add_device(self):
        rtsp_url = self.rtsp_input.text()
        name = self.name_input.text()
        save_path = self.save_path_input.text()
        interval = int(self.interval_input.text()) if self.interval_input.text().isdigit() else 60

        if not rtsp_url or not name or not save_path:
            QMessageBox.warning(self, "Warning", "RTSP URL, Name, and Save Path are required fields.")
            return

        if self.utils.is_duplicate_device(rtsp_url, name):
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
            self.db.session.add(new_device)
            self.db.session.commit()
            #self.utils.load_device_list()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error while saving device data: {e}")

        self.utils.load_device_list()


        # Тут ви можете передати отримані дані, де потрібно
        # Наприклад, до вашої основної програми чи окремому класу для обробки
