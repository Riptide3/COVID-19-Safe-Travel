import traveler
import simtimer
import threading
from PyQt5 import QtCore


class Simulator:
    def __init__(self):
        self.travelers = {}
        self.timer = simtimer.Timer()
        self.timer.start()
        self.forever_timer = None

    def get_all_state(self):
        if len(self.travelers) > 0:
            for t in self.travelers.values():
                time_diff = self.timer.time_now - t.departure_date
                time_diff = time_diff.days * 24 + time_diff.seconds // 3600
                print(t.name)
                print(t.get_state(time_diff))

    def _forever(self):
        self.get_all_state()
        self.forever_timer = threading.Timer(10, self._forever)
        self.forever_timer.start()

    def forever(self):
        self.get_all_state()
        self.forever_timer = threading.Timer(10, self._forever)
        self.forever_timer.start()

    def end(self):
        self.timer.end()
        self.forever_timer.cancel()

    def new_traveler(self, t):
        nt = traveler.Traveler(t['name'], t['ID'], t['origin'], t['destination'], self.timer.time_now, t['time_limit'])
        self.travelers.update({t['ID']: nt})
        # self.end() # FIXME:删除这里的

    def get_plan(self, ID):
        return self.travelers[ID].departure_date, self.travelers[ID].risk, self.travelers[ID].route

    def get_state(self, ID):
        time_diff = self.timer.time_now - self.travelers[ID].departure_date
        time_diff = time_diff.days * 24 + time_diff.seconds // 3600
        return self.travelers[ID].get_state(time_diff)