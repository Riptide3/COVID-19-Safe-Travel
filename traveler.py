import schedule
import logger


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

    def get_plan(self):
        route_schedule = schedule.Schedule(self.origin, self.destination, self.departure_time, self.time_limit)
        risk, route = route_schedule.get_schedule()
        return risk, route

    def construct_state(self):
        count = 0
        states = []
        for road in self.route[1:]:
            dt = road['departure_time']
            at = road['arrival_time']
            if at >= dt:
                for i in range(count, count+at-dt):
                    states.append(road)
                count += at - dt
            else:
                for i in range(count, count+at+(24-dt)):
                    states.append(road)
                count += at + (24 - dt)
        return states

    def get_state(self, n):
        return self.states[n]


if __name__ == '__main__':
    t = Traveler('yzy', 123456, '北京', '成都', 8, 50)
