import time
import heapq
import logger


class Schedule:
    def __init__(self, origin, destination, departure_time, time_limit):
        self.origin = origin + '_0'
        self.destination = destination
        self.departure_time = departure_time
        self.time_limit = time_limit
        self.cities = ['北京', '天津', '石家庄', '济南', '太原', '郑州', '合肥', '南京',
                       '上海', '西安', '武汉', '重庆', '成都', '杭州', '兰州']
        self.city_risk = {'北京': 0.9, '天津': 0.5, '石家庄': 0.5, '济南': 0.2, '太原': 0.2, '郑州': 0.5, '合肥': 0.2,
                          '南京': 0.5, '上海': 0.9, '西安': 0.2, '武汉': 0.9, '重庆': 0.9, '成都': 0.9, '杭州': 0.5, '兰州': 0.2}
        self.vehicle_risk = {'BUS': 2, 'TRAIN': 5, 'AIRPLANE': 9}
        self.timetable = []
        with open(r'TimeTable.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                item = line.split()
                self.timetable.append({'origin': item[0], 'destination': item[1],
                                       'departure_time': int(item[2]), 'arrival_time': int(item[3]),
                                       'type': item[4]})
        self.inf = 999
        self.graph = self.construct_graph(self.departure_time, self.time_limit)

    def construct_graph(self, departure_time, time_limit):
        graph = {}
        time_limit = time_limit * 24
        for city in self.cities:
            start = city
            graph.update(
                {start + '_0': {start + '_0': {'origin': start, 'destination': start, 'departure_time': departure_time,
                                               'arrival_time': departure_time, 'type': 'STAY','risk': 0}}})
            for i in range(time_limit):
                vertex_i = city + '_' + str(i)
                for edge in self.timetable:
                    if edge['origin'] == city and edge['departure_time'] == ((departure_time + i) % 24):
                        if i + edge['arrival_time'] - edge['departure_time'] > time_limit:
                            continue
                        risk = (self.city_risk[city] * self.vehicle_risk[edge['type']] *
                                (edge['arrival_time'] - edge['departure_time']))
                        edge.update({'risk': risk})
                        vertex_j = edge['destination'] + '_' + str(i + edge['arrival_time'] - edge['departure_time'])
                        if vertex_i in graph.keys():
                            graph[vertex_i].update({vertex_j: edge})
                        else:
                            graph.update({vertex_i: {vertex_j: edge}})

                vertex_j = city + '_' + str(i + 1)
                edge = {'origin': city, 'destination': city, 'departure_time': ((departure_time + i) % 24),
                        'arrival_time': ((departure_time + i + 1) % 24), 'type': 'STAY', 'risk': self.city_risk[city]}
                if vertex_i in graph.keys():
                    graph[vertex_i].update({vertex_j: edge})
                else:
                    graph.update({vertex_i: {vertex_j: edge}})

            vertex_j = city + '_' + str(time_limit)
            edge = {'origin': city, 'destination': city, 'departure_time': ((departure_time + time_limit) % 24),
                    'arrival_time': ((departure_time + time_limit) % 24), 'type': 'STAY', 'risk': 0}
            graph.update({vertex_j: {vertex_j: edge}})
        return graph

    def dijkstra(self, graph, start):  # dijkstra算法
        dis = dict((key, self.inf) for key in graph)  # start到每个点的距离
        dis[start] = 0
        vis = dict((key, False) for key in graph)  # 是否访问过，1位访问过，0为未访问
        # 堆优化
        pq = []  # 存放排序后的值
        heapq.heappush(pq, [dis[start], start])

        t_start = time.time()
        path = dict((key, [graph[start][start]]) for key in graph)  # 记录到每个点的路径
        while len(pq) > 0:
            v_dis, v_i = heapq.heappop(pq)  # 未访问点中距离最小的点和对应的距离
            if vis[v_i]:
                continue
            vis[v_i] = True
            path_v_i = path[v_i].copy()  # 到v的最短路径
            for v_j in graph[v_i]:  # 与v直接相连的点
                new_dis = dis[v_i] + float(graph[v_i][v_j]['risk'])
                if new_dis < dis[v_j] and (not vis[v_j]):  # 如果与v直接相连的vertex通过v到src的距离小于dis中对应的vertex的值,则用小的值替换
                    dis[v_j] = new_dis  # 更新点的距离
                    #  dis_un[v_j][0] = new_dis    #更新未访问的点到start的距离
                    heapq.heappush(pq, [dis[v_j], v_j])
                    path_v_j = path_v_i.copy()
                    path_v_j.append(graph[v_i][v_j])  # 更新vertex的路径
                    path[v_j] = path_v_j  # 将新路径赋值给temp

        t_end = time.time()
        print('Dijkstra算法所用时间:', t_end - t_start)
        return dis, path

    def get_schedule(self):
        distance, path = self.dijkstra(self.graph, self.origin)
        dists = []
        for i in range(self.time_limit + 1):
            dists.append(distance[self.destination + '_' + str(i)])

        if min(dists) == self.inf:
            min_risk = 0
            min_risk_route = []
        else:
            min_risk = round(distance[self.destination + '_' + str(dists.index(min(dists)))], 1)
            min_risk_route = path[self.destination + '_' + str(dists.index(min(dists)))]
        # for route in path[self.destination + '_' + str(dists.index(min(dists)))]:
        #     if route['origin'] == route['destination']:
        #         continue
        #     else:
        #         min_risk_route.append(route)

        return min_risk, min_risk_route


if __name__ == '__main__':
    travel_schedule = Schedule('北京', '成都', 8, 50)
    mr, mrr = travel_schedule.get_schedule()
#     for route in mrr:
#         print(str(route['departure_time']) + '--' + str(route['arrival_time']) + '\t' +
#               route['origin'] + '--->' + route['destination'] + '\t' + route['type'])