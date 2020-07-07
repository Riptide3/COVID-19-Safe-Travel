# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import simulator
import datetime

class MainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self, '系统提示', '是否退出系统?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class Ui_MainWindow(object):
    def __init__(self):
        self.sim = simulator.Simulator()
        self.init_timer()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 986)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainGridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.mainGridLayout.setObjectName("mainGridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:100}\n"
"QTabBar::tab{height:40}")
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.gridLayoutWidget = QtWidgets.QWidget(self.main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 90, 261, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.travelerGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.travelerGridLayout.setContentsMargins(0, 0, 0, 0)
        self.travelerGridLayout.setObjectName("travelerGridLayout")
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.travelerGridLayout.addWidget(self.nameLabel, 1, 0, 1, 1)
        self.idLabel1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.idLabel1.setFont(font)
        self.idLabel1.setObjectName("idLabel1")
        self.travelerGridLayout.addWidget(self.idLabel1, 3, 0, 1, 1)
        self.idLineEdit1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.idLineEdit1.setFont(font)
        self.idLineEdit1.setObjectName("idLineEdit1")
        self.travelerGridLayout.addWidget(self.idLineEdit1, 3, 1, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.travelerGridLayout.addWidget(self.nameLineEdit, 1, 1, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.infoLabel.setFont(font)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.travelerGridLayout.addWidget(self.infoLabel, 0, 0, 1, 2)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.main)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(110, 220, 261, 111))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.InfoGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.InfoGridLayout.setContentsMargins(0, 0, 0, 0)
        self.InfoGridLayout.setObjectName("InfoGridLayout")
        self.destinationLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.destinationLabel.setFont(font)
        self.destinationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.destinationLabel.setObjectName("destinationLabel")
        self.InfoGridLayout.addWidget(self.destinationLabel, 2, 1, 1, 1)
        self.destinationCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.destinationCombo.setFont(font)
        self.destinationCombo.setObjectName("destinationCombo")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.destinationCombo.addItem("")
        self.InfoGridLayout.addWidget(self.destinationCombo, 3, 1, 1, 1)
        self.travelLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.travelLabel.setFont(font)
        self.travelLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.travelLabel.setObjectName("travelLabel")
        self.InfoGridLayout.addWidget(self.travelLabel, 0, 0, 1, 2)
        self.originLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.originLabel.setFont(font)
        self.originLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.originLabel.setObjectName("originLabel")
        self.InfoGridLayout.addWidget(self.originLabel, 2, 0, 1, 1)
        self.originCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.originCombo.setFont(font)
        self.originCombo.setObjectName("originCombo")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.originCombo.addItem("")
        self.InfoGridLayout.addWidget(self.originCombo, 3, 0, 1, 1)
        self.strategyLabel = QtWidgets.QLabel(self.main)
        self.strategyLabel.setGeometry(QtCore.QRect(193, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.strategyLabel.setFont(font)
        self.strategyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.strategyLabel.setObjectName("strategyLabel")
        self.hourSpin = QtWidgets.QSpinBox(self.main)
        self.hourSpin.setGeometry(QtCore.QRect(280, 450, 61, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.hourSpin.setFont(font)
        self.hourSpin.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.hourSpin.setMaximum(23)
        self.hourSpin.setObjectName("hourSpin")
        self.daySpin = QtWidgets.QSpinBox(self.main)
        self.daySpin.setGeometry(QtCore.QRect(200, 450, 61, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.daySpin.setFont(font)
        self.daySpin.setMaximum(2)
        self.daySpin.setObjectName("daySpin")
        self.timeLimitLabel = QtWidgets.QLabel(self.main)
        self.timeLimitLabel.setGeometry(QtCore.QRect(140, 456, 51, 20))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.timeLimitLabel.setFont(font)
        self.timeLimitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLimitLabel.setObjectName("timeLimitLabel")
        self.startButton = QtWidgets.QPushButton(self.main)
        self.startButton.setGeometry(QtCore.QRect(190, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.routeLabel = QtWidgets.QLabel(self.main)
        self.routeLabel.setGeometry(QtCore.QRect(200, 575, 91, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.routeLabel.setFont(font)
        self.routeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.routeLabel.setObjectName("routeLabel")
        self.routeTextBrowser = QtWidgets.QTextBrowser(self.main)
        self.routeTextBrowser.setGeometry(QtCore.QRect(20, 610, 461, 301))
        self.routeTextBrowser.setObjectName("routeTextBrowser")
        self.strategyRadioButton1 = QtWidgets.QRadioButton(self.main)
        self.strategyRadioButton1.setGeometry(QtCore.QRect(110, 410, 101, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.strategyRadioButton1.setFont(font)
        self.strategyRadioButton1.setObjectName("strategyRadioButton1")
        self.strategyRadioButton2 = QtWidgets.QRadioButton(self.main)
        self.strategyRadioButton2.setGeometry(QtCore.QRect(240, 410, 141, 19))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.strategyRadioButton2.setFont(font)
        self.strategyRadioButton2.setObjectName("strategyRadioButton2")
        self.timeLabel = QtWidgets.QLabel(self.main)
        self.timeLabel.setGeometry(QtCore.QRect(146, 40, 215, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.mapLabel = QtWidgets.QLabel(self.main)
        self.mapLabel.setGeometry(QtCore.QRect(600, -3, 1130, 950))
        self.mapLabel.setText("")
        self.mapLabel.setPixmap(QtGui.QPixmap("./images/map.png"))
        self.mapLabel.setObjectName("mapLabel")

        self.pathLabel = QtWidgets.QLabel(self.main)
        self.pathLabel.setGeometry(QtCore.QRect(600, -3, 1130, 950))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        self.painter = QtGui.QPainter()
        self.pen = QtGui.QPen(QtCore.Qt.red, 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
        self.cityCoordinates = {'澳门': QtCore.QPoint(813, 811), '北京': QtCore.QPoint(812, 361),
                                '成都': QtCore.QPoint(582, 607), '福州': QtCore.QPoint(920, 704),
                                '广州': QtCore.QPoint(797, 786), '贵阳': QtCore.QPoint(643, 711),
                                '哈尔滨': QtCore.QPoint(978, 198), '海口': QtCore.QPoint(721, 878),
                                '杭州': QtCore.QPoint(917, 606), '合肥': QtCore.QPoint(862, 562),
                                '呼和浩特': QtCore.QPoint(727, 349), '济南': QtCore.QPoint(845, 443),
                                '昆明': QtCore.QPoint(549, 748), '拉萨': QtCore.QPoint(309, 605),
                                '兰州': QtCore.QPoint(579, 478), '南昌': QtCore.QPoint(842, 648),
                                '南京': QtCore.QPoint(901, 561), '南宁': QtCore.QPoint(679, 803),
                                '上海': QtCore.QPoint(949, 567), '沈阳': QtCore.QPoint(945, 297),
                                '石家庄': QtCore.QPoint(789, 409), '台北': QtCore.QPoint(972, 726),
                                '太原': QtCore.QPoint(750, 422), '天津': QtCore.QPoint(842, 379),
                                '乌鲁木齐': QtCore.QPoint(291, 252), '武汉': QtCore.QPoint(803, 604),
                                '西安': QtCore.QPoint(682, 516), '西宁': QtCore.QPoint(534, 461),
                                '香港': QtCore.QPoint(784, 816), '银川': QtCore.QPoint(625, 409),
                                '长春': QtCore.QPoint(967, 245), '长沙': QtCore.QPoint(774, 663),
                                '郑州': QtCore.QPoint(776, 500), '重庆': QtCore.QPoint(637, 630)}
        self.tabWidget.addTab(self.main, "")
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.logGridLayout = QtWidgets.QGridLayout(self.log)
        self.logGridLayout.setContentsMargins(400, -1, 400, -1)
        self.logGridLayout.setObjectName("logGridLayout")
        self.logLabel = QtWidgets.QLabel(self.log)
        self.logLabel.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.logLabel.setFont(font)
        self.logLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logLabel.setObjectName("logLabel")
        self.logGridLayout.addWidget(self.logLabel, 0, 1, 1, 1)
        self.stateSearchLabel = QtWidgets.QLabel(self.log)
        self.stateSearchLabel.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.stateSearchLabel.setFont(font)
        self.stateSearchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stateSearchLabel.setObjectName("stateSearchLabel")
        self.logGridLayout.addWidget(self.stateSearchLabel, 2, 1, 1, 1)
        self.stateSearchIDLabel = QtWidgets.QLabel(self.log)
        self.stateSearchIDLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.stateSearchIDLabel.setFont(font)
        self.stateSearchIDLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stateSearchIDLabel.setObjectName("stateSearchIDLabel")
        self.logGridLayout.addWidget(self.stateSearchIDLabel, 4, 0, 1, 1)
        self.stateSearchIDLineEdit = QtWidgets.QLineEdit(self.log)
        self.stateSearchIDLineEdit.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.stateSearchIDLineEdit.setFont(font)
        self.stateSearchIDLineEdit.setObjectName("stateSearchIDLineEdit")
        self.logGridLayout.addWidget(self.stateSearchIDLineEdit, 4, 1, 1, 1)
        self.stateSearchButton = QtWidgets.QPushButton(self.log)
        self.stateSearchButton.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.stateSearchButton.setFont(font)
        self.stateSearchButton.setObjectName("stateSearchButton")
        self.logGridLayout.addWidget(self.stateSearchButton, 4, 2, 1, 1)
        self.stateSearchTextBrowser = QtWidgets.QTextBrowser(self.log)
        self.stateSearchTextBrowser.setMaximumSize(QtCore.QSize(800, 16777215))
        self.stateSearchTextBrowser.setObjectName("stateSearchTextBrowser")
        self.logGridLayout.addWidget(self.stateSearchTextBrowser, 3, 1, 1, 1)
        self.logTextBrowser = QtWidgets.QTextBrowser(self.log)
        self.logTextBrowser.setMaximumSize(QtCore.QSize(800, 16777215))
        self.logTextBrowser.setObjectName("logTextBrowser")
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(13)
        self.logTextBrowser.setFont(font)
        self.logGridLayout.addWidget(self.logTextBrowser, 1, 1, 1, 1)
        self.logGridLayout.setColumnStretch(0, 1)
        self.logGridLayout.setColumnStretch(1, 6)
        self.logGridLayout.setColumnStretch(2, 1)
        self.logGridLayout.setRowStretch(0, 1)
        self.logGridLayout.setRowStretch(1, 10)
        self.logGridLayout.setRowStretch(2, 1)
        self.logGridLayout.setRowStretch(3, 1)
        self.logGridLayout.setRowStretch(4, 1)
        self.tabWidget.addTab(self.log, "")
        self.mainGridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        # 连接槽函数
        self.daySpin.setEnabled(False)
        self.hourSpin.setEnabled(False)
        self.strategyRadioButton1.setChecked(True)
        self.strategyRadioButton2.toggled.connect(self.daySpin.setEnabled)
        self.strategyRadioButton2.toggled.connect(self.hourSpin.setEnabled)
        self.startButton.clicked.connect(self.startButton_clicked)
        self.stateSearchButton.clicked.connect(self.stateSearchButton_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "COVID-19安全旅行模拟系统"))
        self.nameLabel.setText(_translate("MainWindow", "    姓名:"))
        self.idLabel1.setText(_translate("MainWindow", "身份证号:"))
        self.infoLabel.setText(_translate("MainWindow", "旅客信息"))
        self.destinationLabel.setText(_translate("MainWindow", "目的地"))
        self.destinationCombo.setCurrentText(_translate("MainWindow", "北京"))
        self.destinationCombo.setItemText(0, _translate("MainWindow", "北京"))
        self.destinationCombo.setItemText(1, _translate("MainWindow", "天津"))
        self.destinationCombo.setItemText(2, _translate("MainWindow", "石家庄"))
        self.destinationCombo.setItemText(3, _translate("MainWindow", "济南"))
        self.destinationCombo.setItemText(4, _translate("MainWindow", "太原"))
        self.destinationCombo.setItemText(5, _translate("MainWindow", "郑州"))
        self.destinationCombo.setItemText(6, _translate("MainWindow", "合肥"))
        self.destinationCombo.setItemText(7, _translate("MainWindow", "南京"))
        self.destinationCombo.setItemText(8, _translate("MainWindow", "上海"))
        self.destinationCombo.setItemText(9, _translate("MainWindow", "西安"))
        self.destinationCombo.setItemText(10, _translate("MainWindow", "武汉"))
        self.destinationCombo.setItemText(11, _translate("MainWindow", "重庆"))
        self.destinationCombo.setItemText(12, _translate("MainWindow", "成都"))
        self.destinationCombo.setItemText(13, _translate("MainWindow", "杭州"))
        self.destinationCombo.setItemText(14, _translate("MainWindow", "兰州"))
        self.travelLabel.setText(_translate("MainWindow", "旅程信息"))
        self.originLabel.setText(_translate("MainWindow", "出发地"))
        self.originCombo.setItemText(0, _translate("MainWindow", "北京"))
        self.originCombo.setItemText(1, _translate("MainWindow", "天津"))
        self.originCombo.setItemText(2, _translate("MainWindow", "石家庄"))
        self.originCombo.setItemText(3, _translate("MainWindow", "济南"))
        self.originCombo.setItemText(4, _translate("MainWindow", "太原"))
        self.originCombo.setItemText(5, _translate("MainWindow", "郑州"))
        self.originCombo.setItemText(6, _translate("MainWindow", "合肥"))
        self.originCombo.setItemText(7, _translate("MainWindow", "南京"))
        self.originCombo.setItemText(8, _translate("MainWindow", "上海"))
        self.originCombo.setItemText(9, _translate("MainWindow", "西安"))
        self.originCombo.setItemText(10, _translate("MainWindow", "武汉"))
        self.originCombo.setItemText(11, _translate("MainWindow", "重庆"))
        self.originCombo.setItemText(12, _translate("MainWindow", "成都"))
        self.originCombo.setItemText(13, _translate("MainWindow", "杭州"))
        self.originCombo.setItemText(14, _translate("MainWindow", "兰州"))
        self.strategyLabel.setText(_translate("MainWindow", "策略选择"))
        self.hourSpin.setSuffix(_translate("MainWindow", "时"))
        self.daySpin.setSuffix(_translate("MainWindow", "天"))
        self.timeLimitLabel.setText(_translate("MainWindow", "限时:"))
        self.startButton.setText(_translate("MainWindow", "开始模拟"))
        self.routeLabel.setText(_translate("MainWindow", "旅行路线"))
        self.strategyRadioButton1.setText(_translate("MainWindow", "最少风险"))
        self.strategyRadioButton2.setText(_translate("MainWindow", "限时最少风险"))
        self.timeLabel.setText(_translate("MainWindow",
                                self.time_now.strftime("%Y{y}%m{m}%d{d}%H{h}").format(y="年", m="月", d="日", h="时")))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "模拟旅行"))
        self.logLabel.setText(_translate("MainWindow", "系统日志"))
        self.stateSearchLabel.setText(_translate("MainWindow", "旅客状态查询"))
        self.stateSearchIDLabel.setText(_translate("MainWindow", "身份证号:"))
        self.stateSearchButton.setText(_translate("MainWindow", "开始查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("MainWindow", "日志"))

    # 定时器初始化
    def init_timer(self):
        self.time_now = datetime.datetime.now()
        self.one_hour = datetime.timedelta(hours=1)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timed_tasks)
        self.timer.setInterval(10 * 1000)
        self.timer.start()

    # 定时任务
    def timed_tasks(self):
        self.timer.stop()
        self.time_now += self.one_hour
        states = self.sim.get_all_states(self.time_now)
        self.vehicle_move(states)
        self.log_update(states)
        self.draw_path(self.sim.get_all_routes())
        self.timeLabel.setText(self.time_now.strftime("%Y{y}%m{m}%d{d}%H{h}").format(y="年", m="月", d="日", h="时"))
        self.logTextBrowser.append(self.time_now.strftime("%Y{y}%m{m}%d{d}%H{h}").format(y="年", m="月", d="日", h="时"))
        self.timer.start()

    # 启停定时器时的一次性定时任务
    def one_time_tasks(self):
        self.time_now += self.one_hour
        states = self.sim.get_all_states(self.time_now)
        self.vehicle_move(states)
        self.log_update(states)
        self.draw_path(self.sim.get_all_routes())
        self.timeLabel.setText(self.time_now.strftime("%Y{y}%m{m}%d{d}%H{h}").format(y="年", m="月", d="日", h="时"))
        self.logTextBrowser.append(self.time_now.strftime("%Y{y}%m{m}%d{d}%H{h}").format(y="年", m="月", d="日", h="时"))
        self.timer.start()

    # 显示系统为旅客规划的路线
    def show_route(self, name, ID):
        d_date, risk, route = self.sim.get_plan(ID)
        text = ''
        one_day = datetime.timedelta(days=1)
        prev = int(d_date.strftime('%H'))
        E2C = {'BUS': '汽车', 'TRAIN': '火车', 'AIRPLANE': '飞机'}
        text += f'{name}，您好！\n\n'
        if len(route) > 0:
            text += f'为您规划的最佳路线如下：\n'
            for part in route:
                if part['origin'] != part['destination']:
                    if part['departure_time'] < prev:
                        d_date += one_day
                    text += f"{d_date.strftime('%m')}月{d_date.strftime('%d')}日{part['departure_time']:02}时 - "
                    if part['arrival_time'] < part['departure_time']:
                        d_date += one_day
                    text += f"{d_date.strftime('%m')}月{d_date.strftime('%d')}日{part['arrival_time']:02}时  " \
                            f"{part['origin']} --> {part['destination']}  {E2C[part['type']]}\n"
            text += f"该路线的风险总值为：{risk}"
        else:
            text += f'非常抱歉，基于您当前的选择，系统无法为您找到合适的路线。'

        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        self.routeTextBrowser.setFont(font)
        self.routeTextBrowser.setText(text)

    # 开始模拟按钮被点击
    def startButton_clicked(self):
        remainingTime = self.timer.remainingTime()
        self.timer.stop()
        name = self.nameLineEdit.text()
        ID = self.idLineEdit1.text()
        origin = self.originCombo.currentText()
        destination = self.destinationCombo.currentText()
        limit = self.strategyRadioButton2.isChecked()
        if limit:
            time_limit = int(self.daySpin.text()[:-1]) * 24 + int(self.hourSpin.text()[:-1])
        else:
            time_limit = 2 * 24  # 修改此处更改默认限时
        if name == '' or ID == '':
            QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '姓名和身份证号不能为空！',
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        elif origin == destination:
            QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '出发地和目的地不能相同！',
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        elif time_limit <= 0:
            QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '时间限制必须大于零！',
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:

            traveler = {'name': name, 'ID': ID, 'origin': origin, 'destination': destination,
                        'departure_date': self.time_now, 'time_limit': time_limit}
            self.nameLineEdit.clear()
            self.idLineEdit1.clear()
            self.sim.new_traveler(traveler)
            self.show_route(name, ID)
            self.draw_path(self.sim.get_all_routes())
            state = self.sim.get_state(ID, self.time_now)
            self.animation = self.anima(state, remainingTime - 25)
            self.animation.start()
            self.logTextBrowser.append(f"{name}(ID:{ID})开始旅行")
        self.timer.singleShot(remainingTime, self.one_time_tasks)

    # 获取某一旅客状态的按钮被点击
    def stateSearchButton_clicked(self):
        ID = self.stateSearchIDLineEdit.text()
        if ID == '':
            QtWidgets.QMessageBox.warning(self.centralwidget, '注意', '身份证号不能为空！',
                                          QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        else:
            state = self.sim.get_state(ID, self.time_now)
            font = QtGui.QFont()
            font.setFamily("新宋体")
            font.setPointSize(12)
            self.stateSearchTextBrowser.setFont(font)
            E2C = {'BUS': '汽车', 'TRAIN': '火车', 'AIRPLANE': '飞机'}
            if state['type'] == 'STAY':
                text = f"旅客当前停留在{state['origin']}"
            else:
                text = f"旅客当前处于{state['origin']}前往{state['destination']}的{E2C[state['type']]}上"
            self.stateSearchTextBrowser.setText(text)
            self.logTextBrowser.append(f"查询旅客(ID:{ID})状态，" + text)

    # 在地图上画出路线
    def draw_path(self, routes):
        pix = QtGui.QPixmap(1130, 950)
        pix.fill(QtCore.Qt.transparent)
        path = QtGui.QPainterPath()
        for route in routes:
            path.moveTo(self.cityCoordinates[route[0]['origin']])
            for part in route:
                if part['origin'] != part['destination']:
                    path.lineTo(self.cityCoordinates[part['destination']])
        self.painter.begin(pix)
        self.painter.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        self.painter.setPen(self.pen)
        self.painter.drawPath(path)
        self.painter.end()
        self.pathLabel.setPixmap(pix)

    # 更新系统日志
    def log_update(self, states):
        E2C = {'BUS': '汽车', 'TRAIN': '火车', 'AIRPLANE': '飞机'}
        if len(states) > 0:
            for state in states:
                if state['type'] == 'ARRIVAL':
                    self.logTextBrowser.append(f"{state['name']}(ID:{state['ID']})到达目的地{state['destination']}")
                elif state['type'] == 'STAY':
                    self.logTextBrowser.append(f"{state['name']}(ID:{state['ID']})当前停留在{state['origin']}")
                else:
                    self.logTextBrowser.append(f"{state['name']}(ID:{state['ID']})当前处于"
                                               f"{state['origin']}前往{state['destination']}的{E2C[state['type']]}上")

    # 交通工具移动动画
    def anima(self, state, duration):
        initPoint = QtCore.QPoint(600 - 15, -3 - 15)
        vehicleLabel = QtWidgets.QLabel(self.main)
        vehicleLabel.setGeometry(QtCore.QRect(600, -3, 30, 30))
        vehicleLabel.setText("")
        vehicleLabel.setObjectName("vehicleLabel")
        vehicleLabel.setPixmap(QtGui.QPixmap("./images/" + state["type"] + ".png"))
        vehicleLabel.show()
        animation = QtCore.QPropertyAnimation(vehicleLabel, b"pos")
        if state['arrival_time'] > state['departure_time']:
            total_time = state['arrival_time'] - state['departure_time']
            time_diff = int(self.time_now.strftime("%H")) - state['departure_time']
        else:
            total_time = state['arrival_time'] + 24 - state['departure_time']
            time_now = int(self.time_now.strftime("%H"))
            if time_now > state['departure_time']:
                time_diff = time_now - state['departure_time']
            else:
                time_diff = time_now + 24 - state['departure_time']
        ratio = time_diff / total_time
        total_dis = self.cityCoordinates[state["destination"]] - self.cityCoordinates[state["origin"]]
        start_point = self.cityCoordinates[state["origin"]] + ratio * total_dis + initPoint
        end_point = start_point + 1 / total_time * total_dis
        animation.setStartValue(start_point)
        animation.setEndValue(end_point)
        animation.setDuration(duration)
        animation.finished.connect(lambda: vehicleLabel.hide())
        return animation

    # 多旅客动画
    def vehicle_move(self, states):
        states = [s for s in states if s["type"] != "ARRIVAL"]
        if len(states) > 0:
            self.animations = QtCore.QParallelAnimationGroup()
            for i, state in enumerate(states):
                self.animations.addAnimation(self.anima(state, 10 * 1000 - 25))
            self.animations.start()
