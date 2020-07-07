import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mainwindow.MainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("./images/travel.png"))
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()

sys.exit(app.exec_())
