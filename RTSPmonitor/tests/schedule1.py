import sys
import json
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTimeEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, QTime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Менеджер графіку')
        self.setGeometry(100, 100, 600, 400)

        # Основний віджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Віджети для вводу часу та виводу
        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm:ss")
        
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(1)
        self.table_widget.setHorizontalHeaderLabels(['Година'])
        self.table_widget.horizontalHeader().setStretchLastSection(True)

        # Кнопки додавання, видалення та збереження
        add_button = QPushButton('Додати годину')
        add_button.clicked.connect(self.add_hour)
        
        edit_button = QPushButton('Редагувати годину')
        edit_button.clicked.connect(self.edit_hour)
        
        delete_button = QPushButton('Видалити годину')
        delete_button.clicked.connect(self.delete_hour)
        
        save_button = QPushButton('Зберегти графік у JSON')
        save_button.clicked.connect(self.save_schedule)

        # Компонування віджетів у вікні
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        time_layout = QHBoxLayout()
        time_layout.addWidget(self.time_edit)
        time_layout.addWidget(add_button)
        time_layout.addWidget(edit_button)
        time_layout.addWidget(delete_button)
        layout.addLayout(time_layout)

        layout.addWidget(self.table_widget)
        layout.addWidget(save_button)

        # Початковий графік, якщо він завантажений
        self.load_schedule()

    def add_hour(self):
        current_time = self.time_edit.time()

        # Перевірка, чи такий запис вже є в таблиці
        for row in range(self.table_widget.rowCount()):
            item = self.table_widget.item(row, 0)
            if item.text() == current_time.toString("HH:mm:ss"):
                QMessageBox.warning(self, 'Попередження', 'Ця година вже додана до графіку')
                return

        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(current_time.toString("HH:mm:ss")))

    def edit_hour(self):
        selected_row = self.table_widget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, 'Попередження', 'Спочатку оберіть годину для редагування')
            return

        current_time = self.time_edit.time()

        # Перевірка, чи такий запис вже є в таблиці (окрім поточного рядка)
        for row in range(self.table_widget.rowCount()):
            if row == selected_row:
                continue
            item = self.table_widget.item(row, 0)
            if item.text() == current_time.toString("HH:mm:ss"):
                QMessageBox.warning(self, 'Попередження', 'Ця година вже додана до графіку')
                return

        self.table_widget.item(selected_row, 0).setText(current_time.toString("HH:mm:ss"))

    def delete_hour(self):
        selected_row = self.table_widget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, 'Попередження', 'Спочатку оберіть годину для видалення')
            return

        self.table_widget.removeRow(selected_row)

    def save_schedule(self):
        schedule = []
        for row in range(self.table_widget.rowCount()):
            hour = self.table_widget.item(row, 0).text()
            schedule.append(hour)
        
        try:
            with open('schedule.json', 'w', encoding='utf-8') as f:
                json.dump(schedule, f, ensure_ascii=False, indent=4)
            QMessageBox.information(self, 'Успішно', 'Графік успішно збережено у файлі schedule.json')
        except Exception as e:
            QMessageBox.critical(self, 'Помилка', f'Під час збереження виникла помилка:\n{str(e)}')

    def load_schedule(self):
        try:
            with open('schedule.json', 'r', encoding='utf-8') as f:
                schedule = json.load(f)
                if not isinstance(schedule, list):
                    raise ValueError("Неправильний формат файлу schedule.json: очікується список рядків")

                for hour in schedule:
                    if not isinstance(hour, str):
                        raise ValueError("Неправильний формат часу у файлі schedule.json: очікується рядок")

                    row_position = self.table_widget.rowCount()
                    self.table_widget.insertRow(row_position)
                    item = QTableWidgetItem(hour)  # Передаємо рядок hour у якості тексту
                    self.table_widget.setItem(row_position, 0, item)
        except FileNotFoundError:
            pass  # Якщо файл не знайдено, просто пропускаємо
        except (ValueError, json.JSONDecodeError) as e:
            QMessageBox.critical(self, 'Помилка', f'Під час завантаження графіку виникла помилка: {str(e)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
