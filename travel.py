import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import mainwindow
import os
import sys

def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mainwindow.MainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon(resource_path("./images/travel.png")))
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()

sys.exit(app.exec_())
