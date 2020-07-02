import datetime
import threading


class Timer:
    def __init__(self):
        self.time_now = datetime.datetime.now()
        self.one_hour = datetime.timedelta(hours=1)
        self.timer = None

    def add(self):
        self.time_now += self.one_hour

    def _forever(self):
        print("计时")
        self.add()
        self.timer = threading.Timer(10, self._forever)
        self.timer.start()

    def start(self):
        print("重新计时")
        self.timer = threading.Timer(10, self._forever)
        self.timer.start()

    def end(self):
        self.timer.cancel()