# import datetime
# import json

# def generate_schedule(interval_minutes, start_time):
#     # Список для збереження графіка
#     schedule = []

#     # Генерація графіка на 24 години з вказаним інтервалом
#     for i in range(0, 1440, interval_minutes):
#         time_point = start_time + datetime.timedelta(minutes=i)
#         schedule.append(time_point.strftime("%H:%M:%S"))

#     return schedule

# def main(start_time_str=None):
#     # Інтервал у хвилинах
#     interval_minutes = 60  # Наприклад, кожні 60 хвилин

#     # Перевірка, чи передано значення start_time
#     if start_time_str is None:
#         start_time = datetime.datetime.now()
#     else:
#         # Перетворення рядка часу на datetime об'єкт
#         now = datetime.datetime.now()
#         start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
#         start_time = start_time.replace(year=now.year, month=now.month, day=now.day)

#     # Генерація графіка
#     schedule = generate_schedule(interval_minutes, start_time)

#     # Перетворення графіка в JSON
#     schedule_json = json.dumps(schedule, indent=4)

#     # Виведення JSON в консоль
#     print(schedule_json)

# if __name__ == "__main__":
#     # Виклик main() з дефолтним start_time
#     main()
#     # Або передача конкретного start_time
#     main(start_time_str="11:00")


import datetime
import json

def generate_schedule(interval_minutes):
    schedule = []
    start_time = datetime.datetime(2024, 1, 1, 0, 0)  # Початок доби
    for i in range(0, 1440, interval_minutes):
        time_point = start_time + datetime.timedelta(minutes=i)
        schedule.append(time_point.strftime("%H:%M:%S"))
    return schedule

def main(interval_minutes=60):
    # Генерація графіка
    schedule = generate_schedule(interval_minutes)
    
    # Перетворення графіка в JSON
    schedule_json = json.dumps(schedule, indent=4)
    
    # Запис JSON у файл
    with open('schedule.json', 'w') as file:
        file.write(schedule_json)

if __name__ == "__main__":
    main()  # Викликаємо з дефолтним значенням 60 хвилин або можна передати інший інтервал



import sys
import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, 
    QWidget, QPushButton, QHBoxLayout, QMessageBox, QItemDelegate, QTimeEdit
)
from PyQt6.QtCore import QTime

class TimeDelegate(QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QTimeEdit(parent)
        editor.setDisplayFormat("HH:mm:ss")
        return editor

    def setEditorData(self, editor, index):
        time_str = index.data(Qt.ItemDataRole.EditRole)
        if time_str:
            time = QTime.fromString(time_str, "HH:mm:ss")
            editor.setTime(time)

    def setModelData(self, editor, model, index):
        time = editor.time().toString("HH:mm:ss")
        model.setData(index, time, Qt.ItemDataRole.EditRole)

class ScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schedule")
        self.setGeometry(100, 100, 400, 500)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)
        
        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Save Schedule")
        self.save_button.clicked.connect(self.save_schedule)
        self.button_layout.addWidget(self.save_button)
        
        self.layout.addLayout(self.button_layout)
        
        self.load_schedule()

    def load_schedule(self):
        with open('schedule.json', 'r') as file:
            schedule = json.load(file)
        
        self.table.setRowCount(len(schedule))
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(['Time'])
        
        for row, time in enumerate(schedule):
            self.table.setItem(row, 0, QTableWidgetItem(time))
        
        self.table.setItemDelegate(TimeDelegate(self.table))
        self.table.setEditTriggers(QTableWidget.EditTrigger.AllEditTriggers)

    def save_schedule(self):
        schedule = []
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            if item is not None:
                schedule.append(item.text())
        
        with open('schedule.json', 'w') as file:
            json.dump(schedule, file, indent=4)
        
        QMessageBox.information(self, "Saved", "Schedule has been saved successfully!")

def load_stylesheet(filename):
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    # Генерація розкладу (якщо потрібно змінити інтервал, можна передати інший аргумент)
    main(interval_minutes=60)
    
    app = QApplication(sys.argv)
    
    
    window = ScheduleWindow()
    window.show()
    sys.exit(app.exec())


