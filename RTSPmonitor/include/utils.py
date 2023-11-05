from db.database import Device, DataBase
from PyQt5.QtWidgets import QTableWidgetItem

from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt



class Utils():
    def __init__(self, device_list) -> None:
        self.db = DataBase()
        self.device_list = device_list  
        self.devices = []  

    def load_device_list(self):
        self.devices = self.db.session.query(Device).all()
        #print(f'load device list sussecc {self.devices}')
        self.refresh_device_list()

    def refresh_device_list(self):
        self.device_list.setRowCount(len(self.devices)) 
        for row, device in enumerate(self.devices):
            self.device_list.setItem(row, 0, QTableWidgetItem(device.name))
            self.device_list.setItem(row, 1, QTableWidgetItem(device.rtsp_url))

            if self.device_list.item(row, 2) is None:
                save_path_item = QTableWidgetItem(device.save_path)
                self.device_list.setItem(row, 2, save_path_item)
            else:
                self.device_list.item(row, 2).setData(Qt.DisplayRole, device.save_path)

            # status_item = QTableWidgetItem("Active" if device.active else "Inactive")
            # status_item.setBackground(QColor(0, 255, 0) if device.active else QColor(255, 255, 255))
            # self.device_list.setItem(row, 3, status_item)
            
    def is_duplicate_device(self, rtsp_url, name, exclude_id=None):
        if exclude_id is not None:
            device_with_rtsp = self.db.session.query(Device).filter(Device.id != exclude_id, Device.rtsp_url == rtsp_url).first()
            device_with_name = self.db.session.query(Device).filter(Device.id != exclude_id, Device.name == name).first()
        else:
            device_with_rtsp = self.db.session.query(Device).filter(Device.rtsp_url == rtsp_url).first()
            device_with_name = self.db.session.query(Device).filter(Device.name == name).first()

        return device_with_rtsp or device_with_name 