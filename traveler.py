import schedule


class Traveler:
    def __init__(self, name, ID, origin, destination, departure_date, time_limit):
        self.name = name
        self.ID = ID
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.departure_time = int(departure_date.strftime('%H'))
        self.time_limit = time_limit
        self.risk, self.route = self.get_plan()
        self.states = self.construct_state()

    # 获取系统规划出的旅行路线
    def get_plan(self):
        route_schedule = schedule.Schedule(self.origin, self.destination, self.departure_time, self.time_limit)
        risk, route = route_schedule.get_schedule()
        return risk, route

    # 构造旅客全程的状态表
    def construct_state(self):
        states = []
        for road in self.route[1:]:
            dt = road['departure_time']
            at = road['arrival_time']
            if at >= dt:
                for i in range(0, at - dt):
                    states.append(road)
            else:
                for i in range(0, at + (24 - dt)):
                    states.append(road)
        return states

    # 获取旅客当前状态
    def get_state(self, n):
        return self.states[n]
