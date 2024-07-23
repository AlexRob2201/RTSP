import json
import os
from cv2 import VideoCapture
from PyQt6.QtWidgets import QMessageBox


class Device:
    def __init__(self, name, rtsp_url, save_path, active=False):
        self.name = name
        self.rtsp_url = rtsp_url
        self.save_path = save_path
        self.active = active


    def to_dict(self):
        return {
            'name': self.name,
            'rtsp_url': self.rtsp_url,
            'save_path': self.save_path,
            'active': self.active
        }

class DataBase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.devices = self.load_devices()

    def load_devices(self):
        devices = []
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    for device_data in data:
                        device = Device(**device_data)
                        devices.append(device)
                        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            QMessageBox.warning(self, f"Error loading devices from {self.file_path}: {str(e)}")
        
        return devices

    def save_devices(self):
        with open(self.file_path, 'w') as file:
            json.dump([device.to_dict() for device in self.devices], file, indent=4)

    def add_device(self, name, rtsp_url, save_path, active=False):
        try:
            if self.check_duplicate_name(name):
                return False
            if not self.check_rtsp_url(rtsp_url):
                return False
            if not self.check_save_path(save_path):
                return False
            new_device = Device(name, rtsp_url, save_path, active)
            self.devices.append(new_device)
            self.save_devices()
            return True
        except Exception as e:
            print(f"Error adding device: {str(e)}")
            
            
    def remove_device(self, name):
        try:
            self.devices = [device for device in self.devices if device.name != name]
            self.save_devices()
            return True
        except Exception as e:
            return False
        
    def edit_device(self, current_device_name, new_name, rtsp_url, save_path, active=False):
        for device in self.devices:
            if device.name == current_device_name:
                if new_name != current_device_name and self.check_duplicate_name(new_name):
                    print("Error with name")
                    return False
                device.name = new_name
                if not self.check_rtsp_url(rtsp_url):
                    print("Error with RTSP")
                    return False
                device.rtsp_url = rtsp_url
                if not self.check_save_path(save_path):
                    print("Error with path")
                    return False
                device.save_path = save_path
                self.save_devices()
                return True  
        return False

    ### VALIDATORS ####
    def check_duplicate_name(self, name):
        for device in self.devices:
            if device.name == name:
                return True
        return False
                
    def check_rtsp_url(self, rtsp_url):
        try:
            cap = VideoCapture(rtsp_url)
            if not cap.isOpened():
                cap.release()
                return False
            cap.release()
            return True
        except Exception as e:
            print(f"Error checking RTSP URL '{rtsp_url}': {str(e)}")
            return False
    
    def check_save_path(self, save_path):
        return os.path.exists(save_path)
    
    ### VALIDATORS ####
                