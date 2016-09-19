from math import cos, acos, sqrt


class City:
    prob_type = 'EUC_2D'
    index = 0
    x = 0
    y = 0

    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y

    def geo(self):
        self.prob_type = 'GEO'
        pi = 3.141592
        deg = int(self.x)
        minutes = self.x - deg
        self.x = pi * (deg + 5.0 * minutes / 3.0) / 180.0

        deg = int(self.y)
        minutes = self.y - deg
        self.y = pi * (deg + 5.0 * minutes / 3.0) / 180.0

    def close_neigh(self, cities):
        import sys
        closest = 0
        me = sys.modules[__name__]
        best = sys.maxsize
        for c in cities:
            tmp = self.calc_dist_geo(c)
            if (tmp < best) and (me != c):
                closest = c
                best = tmp
        return closest

    def calc_dist_geo(self, city2):
        rrr = 6378.388
        q1 = cos(self.y - city2.y)
        q2 = cos(self.x - city2.x)
        q3 = cos(self.x + city2.x)
        dist = int((rrr * acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0))
        return dist

    def calc_dist_euc2d(self, city2):
        dist = sqrt((city2.x - self.x)**2 + (city2.y - self.y)**2)
        return dist

def calc_solution(cities):
    prev_city = cities[-1]
    distance = 0
    for c in range(0, len(cities)):
        cur_city = cities[c]
        if cur_city.prob_type == 'GEO':
            distance += cur_city.calc_dist_geo(prev_city)
        elif cur_city.prob_type == 'EUC_2D':
            distance += cur_city.calc_dist_euc2d(prev_city)

        prev_city = cur_city
    return distance

def make_city(id, x, y):
    city = City(id, x, y)
    return city

def print_sol(cities):
    tmp = ''
    for c in cities:
        tmp += '-'+str(c.index)
    print(tmp)
