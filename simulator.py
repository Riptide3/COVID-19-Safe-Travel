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

    # 获取所有旅客的当前状态
    def get_all_state(self):
        if len(self.travelers) > 0:
            for t in list(self.travelers.values()):
                time_diff = self.timer.time_now - t.departure_date
                time_diff = time_diff.days * 24 + time_diff.seconds // 3600
                if time_diff < len(t.states):
                    # state = t.get_state(time_diff)
                    # print(f'{t.name}从{t.origin}出发
                    print(end='')
                else:
                    self.travelers.pop(t.ID)
                    print(f'{t.name}到达目的地{t.destination}')
                    continue
                print(f'{t.name}: {t.get_state(time_diff)}')

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
        newTraveler = traveler.Traveler(t['name'], t['ID'], t['origin'], t['destination'], t['departure_date'], t['time_limit'])
        self.travelers.update({t['ID']: newTraveler})

    # 获取系统规划出的旅行路线
    def get_plan(self, ID):
        return self.travelers[ID].departure_date, self.travelers[ID].risk, self.travelers[ID].route

    # 根据ID获取某一旅客当前状态
    def get_state(self, ID):
        time_diff = self.timer.time_now - self.travelers[ID].departure_date
        time_diff = time_diff.days * 24 + time_diff.seconds // 3600
        return self.travelers[ID].get_state(time_diff)