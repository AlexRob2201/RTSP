import json
from PyQt6.QtCore import Qt
from GUI.ui_main_sidebar import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QHeaderView, QTableWidgetItem, QAbstractItemView, QDialog
from data.json_data import DataBase


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("RS tool")
        self.new_window = QDialog()
        self.bson = DataBase('devices.json')
        
        self.load_devices_to_table()
        
        self.current_device_name = None
        
        self.icon_name_widget.setHidden(True)
        
        
        ### BUTTONS ###
        self.dashboard_button.clicked.connect(self.dashboard)
        self.dashboard_button_1.clicked.connect(self.dashboard)
        
        self.back_dashdoard_button.clicked.connect(self.dashboard)
        self.back_dashdoard_button_2.clicked.connect(self.dashboard)
        
        self.add_device_1.clicked.connect(self.add_device_p)
        
        self.connect_ftp_button.clicked.connect(self.connect_ftp)
        self.connect_ftp_button_1.clicked.connect(self.connect_ftp)
 
        self.addScheduleButton.clicked.connect(self.add_schedule_p)
        self.addScheduleButton_1.clicked.connect(self.add_schedule_p)
        
        self.delete_device_1.clicked.connect(self.delete_selected_device)
        
        self.select_folder.clicked.connect(self.select_folder_path)
        self.select_folder_2.clicked.connect(self.select_folder_path)
        
        self.change_device_1.clicked.connect(self.open_edit_device)
        self.save_changed_device_2.clicked.connect(self.edit_device)
        
        ### BUTTONS ###
        
        self.tableWidget.itemDoubleClicked.connect(self.open_edit_device)
        
        self.stackedWidget.setCurrentIndex(0)
        
        self.dashboard_button.setChecked(True)
        
        self.add_new_device_button.clicked.connect(self.manage_devices)
    
    def dashboard(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def add_device_p(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def change_device_p(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def connect_ftp(self):
        self.stackedWidget.setCurrentIndex(3)
        
    def add_schedule_p(self):
        self.stackedWidget.setCurrentIndex(4)

    def populate_table(self):
        devices = self.bson.load_devices()
        self.tableWidget.setRowCount(len(devices))
        for row, device in enumerate(devices):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(device.name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(device.rtsp_url))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(device.save_path))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(device.active)))
    
    def load_devices_to_table(self):
        self.tableWidget.setColumnCount(4)  # 5 колонок для ідентифікатора, імені, URL, шляху і активності
        headers = ['Name', 'RTSP URL', 'Save Path', 'Active']
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.verticalHeader().setVisible(True)
        
        self.populate_table()
        
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        
        # Розтягуємо стовпці на всю ширину таблиці.
        for i in range(len(headers)):
            self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
    
        self.tableWidget.resizeColumnsToContents()
    
    def manage_devices(self):
        device_name_text = self.device_name_text.text()
        rtsp_string_text = self.rtsp_string_text.text()
        folder_path_text = self.folder_path_text.text()
        
        if self.bson.add_device(device_name_text, rtsp_string_text, folder_path_text):
            self.populate_table()
            QMessageBox.information(self, "Success", "Device succesfuly added")
        else:
            QMessageBox.warning(self, "Warning", "Some data is wrong, please check")
    
    def delete_selected_device(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "No device selected")
            return
        
        device_name = selected_items[0].text()
        if self.bson.remove_device(device_name):
            self.populate_table()
            QMessageBox.information(self, "Info", f"Device '{device_name}' has been removed.")
        else:
            QMessageBox.warning(self, "Error", f"Device '{device_name}' can't be removed.")
            
    def open_edit_device(self):
        selected_items = self.tableWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "No device selected")
            return
        
        
        device_name = selected_items[0].text()
        device_rtsp = selected_items[1].text()
        device_folder = selected_items[2].text()
        self.current_device_name = device_name
        self.device_name_text_2.setText(device_name)
        self.rtsp_string_text_2.setText(device_rtsp)
        self.folder_path_text_2.setText(device_folder)
        
        # Перемкніться на екран редагування
        self.stackedWidget.setCurrentIndex(2)
        
    def edit_device(self):
        
        device_name_text = self.device_name_text_2.text()
        rtsp_string_text = self.rtsp_string_text_2.text()
        folder_path_text = self.folder_path_text_2.text()
        if self.bson.edit_device(self.current_device_name, device_name_text, rtsp_string_text, folder_path_text):
            self.populate_table()
            QMessageBox.information(self, "Success", "Device succesfuly edited")
        else:
            QMessageBox.warning(self, "Warning", "Some data is wrong, please check")
        self.current_device_name = None
        self.stackedWidget.setCurrentIndex(0)
        
    def select_folder_path(self):
        folder_path = QFileDialog.getExistingDirectory(self.new_window, "Select Folder")
        if folder_path:
            self.folder_path_text.setText(folder_path)
        
        
