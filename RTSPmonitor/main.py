from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
import sys 
from content import MySideBar


app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()