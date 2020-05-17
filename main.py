import sys
import traveler
import simtimer

# from PyQt5.QtWidgets import QApplication, QMainWindow
# import mainwindow
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = mainwindow.Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#
# sys.exit(app.exec_())
from time import sleep


timer = simtimer.Timer()
timer.start()
travelers = {}
travelers.update({123456: traveler.Traveler('yzy', 123456, '北京', '成都', timer.time_now, 50)})
travelers.update({654321: traveler.Traveler('fqk', 654321, '济南', '成都', timer.time_now, 50)})
time_diff = 0

while True:
    for t in travelers.values():
        time_diff = timer.time_now - t.departure_date
        time_diff = time_diff.days * 24 + time_diff.seconds // 3600
        print(t.name)
        print(t.get_state(time_diff))
    sleep(10)
timer.end()

