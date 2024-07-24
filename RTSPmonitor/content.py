import os
import platform
from GUI.ui_main_sidebar import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QHeaderView, QTableWidgetItem, QAbstractItemView, QDialog, QPushButton
from data.json_data import DataBase
from data.schedule_data import SchedulesBase


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("RS tool")
        self.new_window = QDialog()

        file_path = os.path.join(self.get_data_directory(), 'devices.json')
        file_path_schedule = os.path.join(self.get_data_directory(), 'schedule.json')
        self.bson = DataBase(file_path)
        self.schedule_bson = SchedulesBase(file_path_schedule)

        self.time_dict = set()

        self.load_devices_to_table()
        self.load_to_schedule_table()
        self.populate_combo_box()

        self.current_device_name = None

        self.icon_name_widget.setHidden(True)

        ### BUTTONS ###
        ### DASHBOARD PAGE BUTTONS ###
        self.dashboard_button.clicked.connect(self.dashboard)
        self.dashboard_button_1.clicked.connect(self.dashboard)

        self.add_device_1.clicked.connect(self.add_device_p)
        self.delete_device_1.clicked.connect(self.delete_selected_device)
        self.change_device_1.clicked.connect(self.open_edit_device)

        self.start_button.clicked.connect(self.test)
        ### DASHBOARD PAGE BUTTONS ###

        ### CONNECT FTP PAGE BUTTONS ###
        self.connect_ftp_button.clicked.connect(self.connect_ftp)
        self.connect_ftp_button_1.clicked.connect(self.connect_ftp)
        ### CONNECT FTP PAGE BUTTONS ###

        ### ADD SCHEDULE PAGE BUTTONS ###
        self.addScheduleButton.clicked.connect(self.add_schedule_p)
        self.addScheduleButton_1.clicked.connect(self.add_schedule_p)

        self.add_time_button.clicked.connect(self.add_time_to_dict)
        self.save_time_button.clicked.connect(self.add_time_schedule)
        self.back_dashdoard_button_3.clicked.connect(self.dashboard)
        ### ADD SCHEDULE PAGE BUTTONS ###

        ### ADD DEVICE PAGE BUTTONS ###
        self.add_new_device_button.clicked.connect(self.manage_devices)
        self.select_folder.clicked.connect(self.select_folder_path)
        self.back_dashdoard_button.clicked.connect(self.dashboard)


        # self.schedule_comboBox.currentIndexChanged.connect(self.update_combo_box)
        ### ADD DEVICE PAGE BUTTONS ###

        ### CHANGE DEVICE PAGE BUTTONS ###
        self.select_folder_2.clicked.connect(self.select_folder_path)
        self.save_changed_device_2.clicked.connect(self.edit_device)
        self.back_dashdoard_button_2.clicked.connect(self.dashboard)
        ### CHANGE DEVICE PAGE BUTTONS ###
        ### BUTTONS ###

        self.tableWidget.itemDoubleClicked.connect(self.open_edit_device)

        self.stackedWidget.setCurrentIndex(0)

        self.dashboard_button.setChecked(True)
    ### PAGES ###
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
    ### PAGES ###

    def populate_table(self):
        try:
            devices = self.bson.load_devices()
            self.tableWidget.setRowCount(len(devices))
            for row, device in enumerate(devices):
                self.tableWidget.setItem(row, 0, QTableWidgetItem(device.name))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(device.rtsp_url))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(device.save_path))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(device.schedule))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(device.active)))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to populate table: {e}")

    def load_devices_to_table(self):
        try:
            self.tableWidget.setColumnCount(5)  # 5 колонок для ідентифікатора, імені, URL, шляху і активності
            headers = ['Name', 'RTSP URL', 'Save Path', 'Schedule', 'Active']
            self.tableWidget.setHorizontalHeaderLabels(headers)
            self.tableWidget.verticalHeader().setVisible(True)

            self.populate_table()

            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

            # Розтягуємо стовпці на всю ширину таблиці.
            for i in range(len(headers)):
                self.tableWidget.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)

            self.tableWidget.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load devices to table: {e}")

    def manage_devices(self):
        try:
            device_name_text = self.device_name_text.text()
            rtsp_string_text = self.rtsp_string_text.text()
            folder_path_text = self.folder_path_text.text()
            schedule_name_text = self.schedule_comboBox.currentText()

            if self.bson.add_device(device_name_text, rtsp_string_text, folder_path_text, schedule_name_text):
                self.populate_table()
                self.populate_combo_box()
                QMessageBox.information(self, "Success", "Device successfully added")
            else:
                QMessageBox.warning(self, "Warning", "Some data is wrong, please check")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to manage device: {e}")

    def delete_selected_device(self):
        try:
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
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to delete selected device: {e}")

    def open_edit_device(self):
        try:
            selected_items = self.tableWidget.selectedItems()
            if not selected_items:
                QMessageBox.warning(self, "Warning", "No device selected")
                return

            device_name = selected_items[0].text()
            device_rtsp = selected_items[1].text()
            device_folder = selected_items[2].text()
            device_schedule = selected_items[3].text()
            self.current_device_name = device_name
            self.device_name_text_2.setText(device_name)
            self.rtsp_string_text_2.setText(device_rtsp)
            self.folder_path_text_2.setText(device_folder)
            self.schedule_comboBox_1.setCurrentText(device_schedule)

            # Перемкніться на екран редагування
            self.stackedWidget.setCurrentIndex(2)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to open edit device: {e}")

    def edit_device(self):
        try:
            device_name_text = self.device_name_text_2.text()
            rtsp_string_text = self.rtsp_string_text_2.text()
            folder_path_text = self.folder_path_text_2.text()
            current_schedule_text = self.schedule_comboBox_1.currentText()
            if self.bson.edit_device(self.current_device_name, device_name_text, rtsp_string_text, folder_path_text, current_schedule_text):
                self.populate_table()
                self.populate_combo_box()
                QMessageBox.information(self, "Success", "Device successfully edited")
            else:
                QMessageBox.warning(self, "Warning", "Some data is wrong, please check")
            self.current_device_name = None
            self.stackedWidget.setCurrentIndex(0)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to edit device: {e}")

    def select_folder_path(self):
        try:
            folder_path = QFileDialog.getExistingDirectory(self.new_window, "Select Folder")
            if folder_path:
                self.folder_path_text.setText(folder_path)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to select folder path: {e}")

    def get_data_directory(self):
        try:
            app_name = "RTSPmonitor"
            system = platform.system()

            if system == "Windows":
                appdata_roaming = os.getenv("LOCALAPPDATA")
                data_directory = os.path.join(appdata_roaming, app_name)
                print(f"this is {system}")
            elif system == "Linux":
                home_directory = os.path.expanduser('~')
                data_directory = os.path.join(home_directory, f'.{app_name}')
                print(f"this is {system}")
            else:
                raise Exception('Unsupported operating system')

            os.makedirs(data_directory, exist_ok=True)
            return data_directory
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to get data directory: {e}")

    def add_time_to_dict(self):
        try:
            time_value = self.timeEdit.text()
            if time_value in self.time_dict:
                QMessageBox.warning(self, "Duplicate Entry", "This time value already exists.")
            else:
                self.time_dict.add(time_value)
                time_dict_str = ", ".join(sorted(self.time_dict))
                self.time_label.setText(time_dict_str)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to add time to dictionary: {e}")

    def add_time_schedule(self):
        try:
            schedule_name = self.schedule_name_text.text()
            time_dict = ", ".join(sorted(self.time_dict))
            if self.schedule_bson.add_schedule(schedule_name, time_dict):
                self.populate_schedule_table()
                self.populate_combo_box()
                self.time_dict.clear()
                self.time_label.clear()
                QMessageBox.information(self, "Success", "Schedule successfully added")
            else:
                QMessageBox.warning(self, "Warning", "Some data is wrong, please check")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to add time schedule: {e}")

    def populate_schedule_table(self):
        try:
            schedules = self.schedule_bson.load_devices()
            self.tableWidget_2.setRowCount(len(schedules))
            for row, schedule in enumerate(schedules):
                self.tableWidget_2.setItem(row, 0, QTableWidgetItem(schedule.name))
                self.tableWidget_2.setItem(row, 1, QTableWidgetItem(schedule.time_dict))

                delete_button = QPushButton('✖')
                delete_button.clicked.connect(lambda _, r=row: self.delete_schedule_row(r))
                self.tableWidget_2.setCellWidget(row, 2, delete_button)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to populate schedule table: {e}")

    def load_to_schedule_table(self):
        try:
            self.tableWidget_2.setColumnCount(3)
            headers = ['Name', 'Time', '✖']
            self.tableWidget_2.setHorizontalHeaderLabels(headers)
            self.tableWidget_2.verticalHeader().setVisible(True)

            self.populate_schedule_table()

            self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

            # Розтягуємо стовпці на всю ширину таблиці.
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
            self.tableWidget_2.setColumnWidth(0, 200)
            self.tableWidget_2.setColumnWidth(2, 50)

        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load schedule table: {e}")

    def delete_schedule_row(self, row):
        try:
            schedule_name = self.tableWidget_2.item(row, 0).text()
            data = self.bson.load_devices()
            for i in range(len(data)):
                device = data[i]
                if schedule_name == device.schedule:
                    QMessageBox.warning(self, "Warning", f"Can't delete, first change schedule for device {device.name}")
                    return

            self.tableWidget_2.removeRow(row)
            # Видаляємо відповідний об'єкт із schedules
            del self.schedule_bson.schedules[row]
            self.schedule_bson.save_devices()
            self.populate_combo_box()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to delete schedule row: {e}")

    def populate_combo_box(self):
        try:
            data = self.schedule_bson.load_devices()
            self.schedule_comboBox.clear()
            self.schedule_comboBox_1.clear()
            for i in range(len(data)):
                schedule = data[i]
                self.schedule_comboBox.addItem(schedule.name)
                self.schedule_comboBox_1.addItem(schedule.name)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to populate combo box: {e}")

    def test(self):
        try:
            data = self.schedule_bson.load_devices()
            for i in range(len(data)):
                device = data[i]
                print(f"Name: {device.name}")
                print(f"Times: {device.time_dict}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to test: {e}")
