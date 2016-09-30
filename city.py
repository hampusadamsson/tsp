from math import sqrt


class City:
    id = 0
    x = 0
    y = 0

    def __init__(self, index, x, y):
        self.id = index
        self.x = x
        self.y = y

    # RETURN NEAREST NEIGHBOR
    def close_neigh(self, cities):
        import sys
        closest = 0
        me = sys.modules[__name__]
        best = sys.maxsize
        for c in cities:
            tmp = self.calc_dist_euc2d_swift(c)
            if (tmp < best) and (me != c):
                closest = c
                best = tmp
        return closest

    def calc_dist_euc2d(self, city2):
        if self.id == city2.id:
            return 99999999
        dist = sqrt((city2.x - self.x)**2 + (city2.y - self.y)**2)

        return dist

    # FASTER THAN calc_dist_euc2d AND PERSEVERE THE RELATION.
    def calc_dist_euc2d_swift(self, city2):
        if self.id == city2.id:
            return 99999999
        dist = ((city2.x - self.x)**2 + (city2.y - self.y)**2)
        return dist


def make_city(id, x, y):
    city = City(id, x, y)
    return city


def print_sol(cities):
    tmp = ''
    for c in cities:
        tmp += '-'+str(c.id)
    print(tmp)
