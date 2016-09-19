from math import cos, acos


class City:
    index = 0
    x = 0
    y = 0

    def __init__(self, index, x, y):
        self.index = index
        pi = 3.141592
        deg = int(x)
        mins = x - deg
        self.x = pi * (deg + 5.0 * mins / 3.0) / 180.0

        deg = int(y)
        mins = y - deg
        self.y = pi * (deg + 5.0 * mins / 3.0) / 180.0

    def close_neigh(self, cities):
        import sys
        me = sys.modules[__name__]
        best = sys.maxsize
        for c in cities:
            tmp = calc_dist(me.City, c)
            if (tmp < best) and (me != c):
                closest = c
                best = tmp
        return closest


def make_city(id, x, y):
    city = City(id, x, y)
    return city


def calc_dist(city1, city2):
    RRR = 6378.388
    q1 = cos(city1.y - city2.y)
    q2 = cos(city1.x - city2.x)
    q3 = cos(city1.x + city2.x)
    dij = int((RRR * acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0))
    return dij


def calc_solution(cities):
    prev_city = cities[-1]
    distance=0
    for c in range(0, len(cities)):
        cur_city = cities[c]
        distance += calc_dist(cur_city, prev_city)
        prev_city=cur_city
    return distance


def print_sol(cities):
    tmp=''
    for c in cities:
        tmp+='-'+str(c.index)

    print(tmp)
