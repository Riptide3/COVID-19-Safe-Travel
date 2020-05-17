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
        self.add()
        self.timer = threading.Timer(10, self._forever)
        self.timer.start()

    def start(self):
        self.timer = threading.Timer(10, self._forever)
        self.timer.start()

    def end(self):
        self.timer.cancel()