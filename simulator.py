import traveler


class Simulator:
    def __init__(self):
        self.travelers = {}

    # 获取所有旅客的当前状态
    def get_all_states(self, time_now):
        states = []
        if len(self.travelers) > 0:
            for t in list(self.travelers.values()):
                time_diff = time_now - t.departure_date
                time_diff = time_diff.days * 24 + time_diff.seconds // 3600
                if time_diff >= len(t.states):
                    self.travelers.pop(t.ID)
                    state = {"ID": t.ID, "name": t.name, "type": "ARRIVAL", "destination": t.destination}
                    states.append(state)
                    continue
                else:
                    state = t.get_state(time_diff)
                    state.update({"ID": t.ID, "name": t.name})
                    states.append(state)
        return states

    # 获取当前存在的所有旅行路线
    def get_all_routes(self):
        routes = []
        for traveler in self.travelers.values():
            routes.append(traveler.route)
        return routes

    # 添加新的旅客
    def new_traveler(self, t):
        newTraveler = traveler.Traveler(t['name'], t['ID'], t['origin'], t['destination'], t['departure_date'], t['time_limit'])
        self.travelers.update({t['ID']: newTraveler})

    # 根据ID获取系统为某一旅客规划出的旅行路线
    def get_plan(self, ID):
        return self.travelers[ID].departure_date, self.travelers[ID].risk, self.travelers[ID].route

    # 根据ID获取某一旅客当前状态
    def get_state(self, ID, time_now):
        time_diff = time_now - self.travelers[ID].departure_date
        time_diff = time_diff.days * 24 + time_diff.seconds // 3600
        return self.travelers[ID].get_state(time_diff)
