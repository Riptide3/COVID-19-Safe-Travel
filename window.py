import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = mainwindow.MainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()

sys.exit(app.exec_())
