import json
import os


class TimeSchedules:
    def __init__(self, name, time_dict):
        self.time_dict = time_dict
        self.name = name
    
    def __repr__(self):
        return f"TimeSchedules(name={self.name}, time_dict={self.time_dict})"
        
    def to_dict(self):
        return {
            'name': self.name,
            'time_dict': self.time_dict
        }
    
class SchedulesBase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.schedules = self.load_devices()

    def load_devices(self):
        schedules = []
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as file:
                    data = json.load(file)
                    for device_data in data:
                        device = TimeSchedules(**device_data)
                        schedules.append(device)
                        
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading devices from {self.file_path}: {str(e)}")
        
        return schedules
    
    def save_devices(self):
        try:
            with open(self.file_path, 'w') as file:
                json.dump([schedule.to_dict() for schedule in self.schedules], file, indent=4)
        except Exception as e:
            print(f"Error saving devices: {str(e)}")
            
    
    def add_schedule(self, name, time_dict):
        try:
            if self.check_duplicate_name(name):
                return False
            new_device = TimeSchedules(name, time_dict)
            self.schedules.append(new_device)
            self.save_devices()
            return True
        except Exception as e:
            print(f"Error adding device: {str(e)}")
            return False
        
    def remove_schedule(self, name):
        try:
            self.schedules = [schedule for schedule in self.schedules if schedule.name != name]
            self.save_devices()
            return True
        except Exception as e:
            return False
        
        ### VALIDATORS ####
    def check_duplicate_name(self, name):
        for schedule in self.schedules:
            if schedule.name == name:
                return True
        return False
    ### VALIDATORS ####
