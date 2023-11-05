import logging
from logging.handlers import RotatingFileHandler
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox
)
from concurrent.futures import ThreadPoolExecutor
from configparser import ConfigParser
import os
from ftplib import FTP
from io import BytesIO
from PIL import Image


class FTPConfigWindow(QMainWindow):
    def __init__(self):

        super().__init__()
        self.init_ui()
                
        self.thread_pool = ThreadPoolExecutor(max_workers=2)
        self.ftp = None
        self.remote_path = '/'
        # Максимальний розмір файлу в байтах (20 МБ)
        max_log_size = 20 * 1024 * 1024  

        # Створюємо об'єкт RotatingFileHandler
        handler_FTP = RotatingFileHandler('log/ftp_log.txt', maxBytes=max_log_size, backupCount=5)
        
        # Максимальна кількість фото у буфері
        self.max_buffer_size = 5
        self.buffer = []

        # Конфігуруємо рівень логування та обробник
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[handler_FTP])

        
    def init_ui(self):
        self.setWindowTitle("FTP Configuration")
        self.setGeometry(100, 100, 400, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.host_label = QLabel("FTP Host:")
        self.host_input = QLineEdit()
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()

        self.save_button = QPushButton("Save Configuration")
        self.save_button.clicked.connect(self.save_configuration)
        self.try_button = QPushButton("Check connection")
        self.try_button.clicked.connect(self.connect_to_ftp)

        self.layout.addWidget(self.host_label)
        self.layout.addWidget(self.host_input)
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.port_label)
        self.layout.addWidget(self.port_input)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.try_button)

        self.central_widget.setLayout(self.layout)

    def save_configuration(self):
        host = self.host_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        port = self.port_input.text()

        try:
            ftp = FTP(host)
            ftp.login(username, password)
            ftp.quit()

            config = ConfigParser()
            config.add_section('FTP')
            config.set('FTP', 'host', host)
            config.set('FTP', 'username', username)
            config.set('FTP', 'password', password)
            config.set('FTP', 'port', port)

            with open('ftp_data.conf', 'w') as config_file:
                config.write(config_file)

            QMessageBox.information(self, "Configuration Saved", "FTP configuration has been saved.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to connect to FTP server: {str(e)}")
            
    def connect_to_ftp(self):
        try:
            config = ConfigParser()
            config.read('ftp_data.conf')
            
            host = config.get('FTP', 'host')
            username = config.get('FTP', 'username')
            password = config.get('FTP', 'password')

            ftp = FTP(host, username, password, acct='', timeout=None, source_address=None, encoding='utf-8')
            ftp.login(username, password)
            
            QMessageBox.information(self, "Success", "Connected to FTP successfully!")  # Виводимо спливаюче повідомлення
            return ftp
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to connect to FTP: {e}")  # Виводимо спливаюче повідомлення з помилкою
            return None
    
    def disconnect_from_ftp(self, ftp):
        try:
            if ftp:
                ftp.quit()
                logging.info("Disconnected from FTP successfully!")
        except Exception as e:
            logging.error(f"Error while disconnecting from FTP: {e}")


    def send_photo_from_path(self, ftp, device):
        try:
            self.thread_pool.submit(self.send_photo_to_ftp, ftp, device)
        except Exception as e:
            logging.error('Error:', e)
            
    def send_photo_to_ftp(self, ftp, device):
        pass
        try:
            if not ftp:
                logging.warning("Not connected to FTP")
                return
            # Отримуємо список всіх файлів у директорії save_path
            local_files = os.listdir(device.save_path)
            
            # Отримуємо список файлів, які були відправлені раніше
            remote_files = self.get_remote_files_list(ftp)
            
            # Визначаємо нові файли, які потрібно відправити
            new_files = [file for file in local_files if file not in remote_files]
            
            # Відправляємо нові файли на FTP
            for file in new_files:
                local_file_path = os.path.join(device.save_path, file)
                remote_file_name = os.path.join(self.remote_path, file)
                with open(local_file_path, "rb") as local_file:
                    ftp.storbinary(f"STOR {remote_file_name}", local_file)
                logging.info(f"File {file} sent to FTP")
        except Exception as e:
            logging.error("Error sending new files:", e)

    def get_remote_files_list(self, ftp):
        try:
            # Отримуємо список файлів на FTP
            remote_files = ftp.nlst(self.remote_path)
            return remote_files
        except Exception as e:
            logging.error("Error getting remote files list:", e)
            return []
        
    
    def send_photo_from_buffer(self, ftp, frame, image_name):
        print(f'Added data to buffer: {len(self.buffer)} items')
        print('here')
        # Зберегти фото в буфер
        image_bytes = BytesIO()
        frame.save(image_bytes, format="JPEG")
        self.buffer.append((image_bytes.getvalue(), image_name))

        print(self.buffer)
        # Перевірити розмір буфера
        if len(self.buffer) >= self.max_buffer_size:
            print('here0')
            self.process_buffer(ftp)
    
    def process_buffer(self, ftp):
        print('here1')
        while self.buffer:
            image_bytes, image_name = self.buffer.pop(0)
            self.upload_to_ftp(ftp,image_bytes, image_name)
            
    def upload_to_ftp(self, ftp, image_bytes, image_name):
        print('here2')
        if not ftp:
            logging.warning("Not connected to FTP")
            return
        try:
            ftp.cwd(self.remote_path)
            with BytesIO(image_bytes) as img_buffer:
                ftp.storbinary("STOR " + image_name, img_buffer)
            logging.info(f"Uploaded {image_name} to FTP")
        except Exception as e:
            logging.error(f"Error uploading {image_name} to FTP: {e}")
            
            
    