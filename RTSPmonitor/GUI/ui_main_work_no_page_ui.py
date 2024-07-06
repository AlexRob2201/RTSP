# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_work_no_page.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1490, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"#title_bar {\n"
"    background-color: #2C3F44;\n"
"    color: white;\n"
"    height: 40px;\n"
"    font-size: 16pt;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgba(42, 62, 73, 1);\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #2C3F44;\n"
"	font-weight:bold;\n"
"}")
        MainWindow.setIconSize(QSize(20, 20))
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"padding: 5px;")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(0, 720))
        self.icon_name_widget.setStyleSheet(u"QWidget {\n"
"paddind: 5px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 text-align:left;\n"
"	 padding-left: 15%;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #2C3F44;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(14)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 7, -1, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    border-radius: 7px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u043a\u0440\u0430\u0457\u0432 \u0434\u043b\u044f \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u043a\u0440\u0443\u0433\u043b\u043e\u0457 \u0444\u043e\u0440\u043c\u0438 */\n"
"    border: 2px solid #000;   /* \u0414\u043e\u0434\u0430\u0432\u0430\u043d\u043d\u044f \u0440\u0430\u043c\u043a\u0438 */\n"
"    background-color: none;   /* \u0412\u0456\u0434\u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c \u0444\u043e\u043d\u0443 */\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QLabel::SetPixmap {\n"
"    border-radius: 7px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u043a\u0440\u0430\u0457\u0432 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f */\n"
"}\n"
"")
        self.label_2.setPixmap(QPixmap(u":/img/main_icon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(120, 60))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.dashboard_button_1 = QPushButton(self.icon_name_widget)
        self.dashboard_button_1.setObjectName(u"dashboard_button_1")
        self.dashboard_button_1.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(10)
        self.dashboard_button_1.setFont(font1)
        self.dashboard_button_1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/img/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboard_button_1.setIcon(icon)
        self.dashboard_button_1.setIconSize(QSize(30, 30))
        self.dashboard_button_1.setCheckable(True)
        self.dashboard_button_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_button_1)

        self.connect_ftp_button_1 = QPushButton(self.icon_name_widget)
        self.connect_ftp_button_1.setObjectName(u"connect_ftp_button_1")
        self.connect_ftp_button_1.setMaximumSize(QSize(200, 60))
        self.connect_ftp_button_1.setFont(font1)
        self.connect_ftp_button_1.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/img/ftp.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.connect_ftp_button_1.setIcon(icon1)
        self.connect_ftp_button_1.setIconSize(QSize(30, 30))
        self.connect_ftp_button_1.setCheckable(True)
        self.connect_ftp_button_1.setAutoExclusive(True)
        self.connect_ftp_button_1.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.connect_ftp_button_1)

        self.addScheduleButton_1 = QPushButton(self.icon_name_widget)
        self.addScheduleButton_1.setObjectName(u"addScheduleButton_1")
        self.addScheduleButton_1.setMaximumSize(QSize(200, 60))
        self.addScheduleButton_1.setFont(font1)
        self.addScheduleButton_1.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/img/schedule.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addScheduleButton_1.setIcon(icon2)
        self.addScheduleButton_1.setIconSize(QSize(30, 30))
        self.addScheduleButton_1.setCheckable(True)
        self.addScheduleButton_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.addScheduleButton_1)

        self.verticalSpacer_2 = QSpacerItem(20, 235, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.content_widget = QWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.content_widget.setMinimumSize(QSize(0, 700))
        self.content_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #2C3F44;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.content_widget)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.content_widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.switch_menu_button = QPushButton(self.widget_4)
        self.switch_menu_button.setObjectName(u"switch_menu_button")
        self.switch_menu_button.setMinimumSize(QSize(30, 30))
        self.switch_menu_button.setMaximumSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/img/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.switch_menu_button.setIcon(icon3)
        self.switch_menu_button.setIconSize(QSize(22, 22))
        self.switch_menu_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.switch_menu_button)

        self.horizontalSpacer = QSpacerItem(468, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search = QLineEdit(self.widget_4)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 30))
        self.search.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.search)

        self.search_button = QPushButton(self.widget_4)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setMinimumSize(QSize(30, 30))
        self.search_button.setMaximumSize(QSize(30, 30))
        self.search_button.setStyleSheet(u"QPushButton::pressed {\n"
"background-color: rgba(42, 62, 73, 1);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/img/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button.setIcon(icon4)
        self.search_button.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.search_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.stackedWidget = QStackedWidget(self.content_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QLineEdit, QComboBox {\n"
"	 background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 text-align:left;\n"
"	 padding-left: 15%;\n"
"	font-size: 16pt;\n"
"	color: white;\n"
"	padding-left: 10px;\n"
"	width: 120;\n"
"	height: 45;\n"
"}")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_page.setStyleSheet(u"QPushButton:pressed{\n"
"	background-color: #2C3F44;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 2)
        self.tableWidget = QTableWidget(self.dashboard_page)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget {\n"
"    padding: 5px;\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"	gridline-color: transparent;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    width: 30px;\n"
"    text-align: left;\n"
"    padding-left: 5px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"	border-bottom: 1px solid rgba(255, 255, 255, 40);\n"
"}\n"
"QTableView::item:selected{\n"
"	color: rgb(255, 255, 255);\n"
"	font-weight:bold;\n"
"    background-color: rgba(42, 62, 73, 1);;\n"
"}\n"
"QTableWidget::item:first-child {\n"
"    border-left: 7px; /* \u0417\u0430\u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u0434\u043b\u044f \u0432\u0435\u0440\u0445\u043d\u044c\u043e\u0433\u043e \u043f\u0440\u0430\u0432\u043e\u0433\u043e \u043a\u0443\u0442\u0430 */\n"
"}\n"
"\n"
"QTableWidget::item:last-child {\n"
"    border-right: 7px; /* \u0417\u0430\u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u0434\u043b\u044f \u043d\u0438\u0436\u043d\u044c\u043e\u0433\u043e \u043f\u0440"
                        "\u0430\u0432\u043e\u0433\u043e \u043a\u0443\u0442\u0430 */\n"
"}\n"
"\n"
"QHeaderView {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: none; /* \u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c color: black; \u0430\u0431\u043e \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0432\u0430\u043c \u043a\u043e\u043b\u0456\u0440 */\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: none; /* \u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c color: white; \u0430\u0431\u043e \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0438\u0439 \u0432\u0430\u043c \u043a\u043e\u043b\u0456\u0440 */\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 7px;\n"
"    margin: 5px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal {\n"
"    background-color: rgba(42, 62, 73, 1);\n"
"    color: white;\n"
"    width: 30px;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QHeaderView::section"
                        ":vertical {\n"
"    background-color: rgba(42, 62, 73, 1);\n"
"    color: white;\n"
"    width: 20px;\n"
"    height: 50px;\n"
"    font-size: 12pt;\n"
"    text-align: center;\n"
"	padding-left: 12px;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"QTableCornerButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.tableWidget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 7)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.add_device_1 = QPushButton(self.dashboard_page)
        self.add_device_1.setObjectName(u"add_device_1")
        self.add_device_1.setMaximumSize(QSize(160, 60))
        self.add_device_1.setFont(font1)
        self.add_device_1.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/img/add-list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_device_1.setIcon(icon5)
        self.add_device_1.setIconSize(QSize(30, 30))
        self.add_device_1.setCheckable(False)
        self.add_device_1.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.add_device_1)

        self.change_device_1 = QPushButton(self.dashboard_page)
        self.change_device_1.setObjectName(u"change_device_1")
        self.change_device_1.setMaximumSize(QSize(160, 60))
        self.change_device_1.setFont(font1)
        self.change_device_1.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/img/alter.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.change_device_1.setIcon(icon6)
        self.change_device_1.setIconSize(QSize(30, 30))
        self.change_device_1.setCheckable(False)
        self.change_device_1.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.change_device_1)

        self.delete_device_1 = QPushButton(self.dashboard_page)
        self.delete_device_1.setObjectName(u"delete_device_1")
        self.delete_device_1.setMaximumSize(QSize(160, 60))
        self.delete_device_1.setFont(font1)
        self.delete_device_1.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/img/trash.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_device_1.setIcon(icon7)
        self.delete_device_1.setIconSize(QSize(30, 30))
        self.delete_device_1.setCheckable(False)
        self.delete_device_1.setAutoExclusive(False)

        self.horizontalLayout_6.addWidget(self.delete_device_1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButton_3 = QPushButton(self.dashboard_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(160, 60))
        self.pushButton_3.setMaximumSize(QSize(160, 60))
        self.pushButton_3.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.dashboard_page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(160, 60))
        self.pushButton_4.setMaximumSize(QSize(160, 60))
        self.pushButton_4.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.add_device_page = QWidget()
        self.add_device_page.setObjectName(u"add_device_page")
        self.verticalLayout_3 = QVBoxLayout(self.add_device_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.add_device_page)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"font-weight:bold;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)

        self.back_dashdoard_button = QPushButton(self.add_device_page)
        self.back_dashdoard_button.setObjectName(u"back_dashdoard_button")
        self.back_dashdoard_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_dashdoard_button.sizePolicy().hasHeightForWidth())
        self.back_dashdoard_button.setSizePolicy(sizePolicy)
        self.back_dashdoard_button.setMinimumSize(QSize(60, 60))
        self.back_dashdoard_button.setMaximumSize(QSize(60, 60))
        self.back_dashdoard_button.setStyleSheet(u"background: none;\n"
"border: none;")
        icon8 = QIcon()
        icon8.addFile(u":/img/back-button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_dashdoard_button.setIcon(icon8)
        self.back_dashdoard_button.setIconSize(QSize(60, 60))
        self.back_dashdoard_button.setCheckable(False)
        self.back_dashdoard_button.setAutoExclusive(False)

        self.horizontalLayout_7.addWidget(self.back_dashdoard_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_5 = QSpacerItem(947, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.device_name_text = QLineEdit(self.add_device_page)
        self.device_name_text.setObjectName(u"device_name_text")
        self.device_name_text.setMinimumSize(QSize(0, 60))
        self.device_name_text.setMaximumSize(QSize(16777215, 60))
        self.device_name_text.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.device_name_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.device_name_text)

        self.rtsp_string_text = QLineEdit(self.add_device_page)
        self.rtsp_string_text.setObjectName(u"rtsp_string_text")
        self.rtsp_string_text.setMinimumSize(QSize(0, 60))
        self.rtsp_string_text.setMaximumSize(QSize(16777215, 60))
        self.rtsp_string_text.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.rtsp_string_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.rtsp_string_text)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.folder_path_text = QLineEdit(self.add_device_page)
        self.folder_path_text.setObjectName(u"folder_path_text")
        self.folder_path_text.setMinimumSize(QSize(0, 60))
        self.folder_path_text.setMaximumSize(QSize(16777215, 60))
        self.folder_path_text.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.folder_path_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.folder_path_text)

        self.select_folder = QPushButton(self.add_device_page)
        self.select_folder.setObjectName(u"select_folder")
        self.select_folder.setMinimumSize(QSize(60, 60))
        self.select_folder.setMaximumSize(QSize(60, 60))
        self.select_folder.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u":/img/cursor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_folder.setIcon(icon9)
        self.select_folder.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.select_folder)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.comboBox = QComboBox(self.add_device_page)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.verticalSpacer_3 = QSpacerItem(20, 108, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.add_new_device_button = QPushButton(self.add_device_page)
        self.add_new_device_button.setObjectName(u"add_new_device_button")
        self.add_new_device_button.setMinimumSize(QSize(200, 60))
        self.add_new_device_button.setMaximumSize(QSize(200, 60))
        self.add_new_device_button.setFont(font1)
        icon10 = QIcon()
        icon10.addFile(u":/img/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_new_device_button.setIcon(icon10)

        self.horizontalLayout_5.addWidget(self.add_new_device_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_4 = QSpacerItem(947, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.add_device_page)
        self.change_device_page = QWidget()
        self.change_device_page.setObjectName(u"change_device_page")
        self.verticalLayout_4 = QVBoxLayout(self.change_device_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.change_device_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"background-color: none;\n"
"font-weight:bold;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_6)

        self.back_dashdoard_button_2 = QPushButton(self.change_device_page)
        self.back_dashdoard_button_2.setObjectName(u"back_dashdoard_button_2")
        self.back_dashdoard_button_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.back_dashdoard_button_2.sizePolicy().hasHeightForWidth())
        self.back_dashdoard_button_2.setSizePolicy(sizePolicy)
        self.back_dashdoard_button_2.setMinimumSize(QSize(60, 60))
        self.back_dashdoard_button_2.setMaximumSize(QSize(60, 60))
        self.back_dashdoard_button_2.setStyleSheet(u"background: none;\n"
"border: none;")
        self.back_dashdoard_button_2.setIcon(icon8)
        self.back_dashdoard_button_2.setIconSize(QSize(60, 60))
        self.back_dashdoard_button_2.setCheckable(False)
        self.back_dashdoard_button_2.setAutoExclusive(False)

        self.horizontalLayout_10.addWidget(self.back_dashdoard_button_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_8 = QSpacerItem(947, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.device_name_text_2 = QLineEdit(self.change_device_page)
        self.device_name_text_2.setObjectName(u"device_name_text_2")
        self.device_name_text_2.setMinimumSize(QSize(0, 60))
        self.device_name_text_2.setMaximumSize(QSize(16777215, 60))
        self.device_name_text_2.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.device_name_text_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.device_name_text_2)

        self.rtsp_string_text_2 = QLineEdit(self.change_device_page)
        self.rtsp_string_text_2.setObjectName(u"rtsp_string_text_2")
        self.rtsp_string_text_2.setMinimumSize(QSize(0, 60))
        self.rtsp_string_text_2.setMaximumSize(QSize(16777215, 60))
        self.rtsp_string_text_2.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.rtsp_string_text_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.rtsp_string_text_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.folder_path_text_2 = QLineEdit(self.change_device_page)
        self.folder_path_text_2.setObjectName(u"folder_path_text_2")
        self.folder_path_text_2.setMinimumSize(QSize(0, 60))
        self.folder_path_text_2.setMaximumSize(QSize(16777215, 60))
        self.folder_path_text_2.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"width: 120;\n"
"height: 45;")
        self.folder_path_text_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.folder_path_text_2)

        self.select_folder_2 = QPushButton(self.change_device_page)
        self.select_folder_2.setObjectName(u"select_folder_2")
        self.select_folder_2.setMinimumSize(QSize(60, 60))
        self.select_folder_2.setMaximumSize(QSize(60, 60))
        self.select_folder_2.setFont(font1)
        self.select_folder_2.setIcon(icon9)
        self.select_folder_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.select_folder_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.comboBox_2 = QComboBox(self.change_device_page)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_4.addWidget(self.comboBox_2)

        self.verticalSpacer_6 = QSpacerItem(1048, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.add_new_device_button_2 = QPushButton(self.change_device_page)
        self.add_new_device_button_2.setObjectName(u"add_new_device_button_2")
        self.add_new_device_button_2.setMinimumSize(QSize(200, 60))
        self.add_new_device_button_2.setMaximumSize(QSize(200, 60))
        self.add_new_device_button_2.setFont(font1)
        self.add_new_device_button_2.setIcon(icon10)

        self.horizontalLayout_8.addWidget(self.add_new_device_button_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_7 = QSpacerItem(947, 74, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.stackedWidget.addWidget(self.change_device_page)
        self.connect_ftp_page = QWidget()
        self.connect_ftp_page.setObjectName(u"connect_ftp_page")
        self.gridLayout_2 = QGridLayout(self.connect_ftp_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.connect_ftp_page)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(32)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.connect_ftp_page)
        self.add_schedule_page = QWidget()
        self.add_schedule_page.setObjectName(u"add_schedule_page")
        self.stackedWidget.addWidget(self.add_schedule_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.content_widget, 0, 2, 1, 1)

        self.icon_widget = QWidget(self.centralwidget)
        self.icon_widget.setObjectName(u"icon_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(70)
        sizePolicy1.setHeightForWidth(self.icon_widget.sizePolicy().hasHeightForWidth())
        self.icon_widget.setSizePolicy(sizePolicy1)
        self.icon_widget.setMinimumSize(QSize(70, 720))
        self.icon_widget.setStyleSheet(u"QWidget {\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	 text-align:left;\n"
"	 padding-left: 15%;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #2C3F44;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.icon_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label = QLabel(self.icon_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"QLabel {\n"
"    border-radius: 7px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u043a\u0440\u0430\u0457\u0432 \u0434\u043b\u044f \u0441\u0442\u0432\u043e\u0440\u0435\u043d\u043d\u044f \u043a\u0440\u0443\u0433\u043b\u043e\u0457 \u0444\u043e\u0440\u043c\u0438 */\n"
"    border: 2px solid #000;   /* \u0414\u043e\u0434\u0430\u0432\u0430\u043d\u043d\u044f \u0440\u0430\u043c\u043a\u0438 */\n"
"    background-color: none;   /* \u0412\u0456\u0434\u0441\u0443\u0442\u043d\u0456\u0441\u0442\u044c \u0444\u043e\u043d\u0443 */\n"
"	padding: 1px;\n"
"}\n"
"\n"
"QLabel::SetPixmap {\n"
"    border-radius: 7px;       /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f \u043a\u0440\u0430\u0457\u0432 \u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u043d\u044f */\n"
"}\n"
"")
        self.label.setPixmap(QPixmap(u":/img/main_icon.png"))
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.dashboard_button = QPushButton(self.icon_widget)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setMinimumSize(QSize(60, 60))
        self.dashboard_button.setMaximumSize(QSize(60, 60))
        self.dashboard_button.setStyleSheet(u"")
        self.dashboard_button.setIcon(icon)
        self.dashboard_button.setIconSize(QSize(30, 30))
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_button)

        self.connect_ftp_button = QPushButton(self.icon_widget)
        self.connect_ftp_button.setObjectName(u"connect_ftp_button")
        self.connect_ftp_button.setMinimumSize(QSize(60, 60))
        self.connect_ftp_button.setMaximumSize(QSize(60, 60))
        self.connect_ftp_button.setStyleSheet(u"")
        self.connect_ftp_button.setIcon(icon1)
        self.connect_ftp_button.setIconSize(QSize(30, 30))
        self.connect_ftp_button.setCheckable(True)
        self.connect_ftp_button.setAutoExclusive(True)
        self.connect_ftp_button.setAutoDefault(False)

        self.verticalLayout.addWidget(self.connect_ftp_button)

        self.addScheduleButton = QPushButton(self.icon_widget)
        self.addScheduleButton.setObjectName(u"addScheduleButton")
        self.addScheduleButton.setMinimumSize(QSize(60, 60))
        self.addScheduleButton.setMaximumSize(QSize(60, 60))
        self.addScheduleButton.setStyleSheet(u"")
        self.addScheduleButton.setIcon(icon2)
        self.addScheduleButton.setIconSize(QSize(30, 30))
        self.addScheduleButton.setCheckable(True)
        self.addScheduleButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.addScheduleButton)

        self.verticalSpacer = QSpacerItem(20, 138, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_8.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.icon_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.switch_menu_button.toggled.connect(self.icon_widget.setHidden)
        self.switch_menu_button.toggled.connect(self.icon_name_widget.setVisible)
        self.dashboard_button.toggled.connect(self.dashboard_button_1.setChecked)
        self.connect_ftp_button.toggled.connect(self.connect_ftp_button_1.setChecked)
        self.addScheduleButton.toggled.connect(self.addScheduleButton_1.setChecked)
        self.dashboard_button_1.toggled.connect(self.dashboard_button.setChecked)
        self.connect_ftp_button_1.toggled.connect(self.connect_ftp_button.setChecked)
        self.addScheduleButton_1.toggled.connect(self.addScheduleButton.setChecked)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.dashboard_button_1.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.connect_ftp_button_1.setText(QCoreApplication.translate("MainWindow", u"Connect FTP", None))
        self.addScheduleButton_1.setText(QCoreApplication.translate("MainWindow", u"Add schedule", None))
        self.switch_menu_button.setText("")
        self.search_button.setText("")
        self.add_device_1.setText(QCoreApplication.translate("MainWindow", u"Add device", None))
        self.change_device_1.setText(QCoreApplication.translate("MainWindow", u"Change device", None))
        self.delete_device_1.setText(QCoreApplication.translate("MainWindow", u"Delete Device", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"      Add device", None))
        self.back_dashdoard_button.setText("")
        self.device_name_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.rtsp_string_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RTSP string", None))
        self.folder_path_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to folder", None))
        self.select_folder.setText("")
        self.add_new_device_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"      Change device", None))
        self.back_dashdoard_button_2.setText("")
        self.device_name_text_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.rtsp_string_text_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RTSP string", None))
        self.folder_path_text_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to folder", None))
        self.select_folder_2.setText("")
        self.add_new_device_button_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SOON", None))
        self.label.setText("")
        self.dashboard_button.setText("")
        self.connect_ftp_button.setText("")
        self.addScheduleButton.setText("")
    # retranslateUi

