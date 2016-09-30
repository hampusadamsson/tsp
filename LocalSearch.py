from chromosome import create_ind
from city import make_city
from plot import plot_res


class LocalSearch:
    cities = []
    individual = []
    optimal = 0
    rend = False
    dist_matrix = []
    function = "s"

    def __init__(self, fname):
        self.load_cities(fname)

    def run(self):
        res = []

        if self.function == "l":
            res = self.individual.local_search()
        elif self.function == "s":
            res = self.individual.simulated_annealing()
        elif self.function == "a":
            res = self.individual.simulated_annealing_two_opt()
        elif self.function == "t":
            res = self.individual.two_opt()

        if self.rend:
            plot_res(res, self.optimal)

        return self.individual

    def load_cities(self, fname):
        with open(fname, "r") as ins:
            cities = []
            for line in ins:
                tmp = line.split(' ')
                tmp = [x for x in tmp if x]
                if len(tmp) >= 3:
                    try:
                        city = make_city(int(tmp[0]), float(tmp[1]), float(tmp[2]))
                        cities.append(city)
                    except ValueError:
                        err = ValueError
        ins.close()
        self.cities = cities
        self.create_distance_matrix()
        self.individual = create_ind(self.cities, self.dist_matrix)

    def create_distance_matrix(self):
        self.dist_matrix.append(["E"])
        for c1 in self.cities:
            tmp = ["E"]
            for c2 in self.cities:
                val = (c1.calc_dist_euc2d(c2))
                tmp.append(val)
            self.dist_matrix.append(tmp)

    def parse_input(self, param):
        for p in param:
            par = (p[0])
            val = (p[1:])

            if par == 'f':
                self.individual.runs = int(val)
            elif par == 't':
                self.individual.temp = float(val)
            elif par == 'c':
                self.individual.cooling_dec = float(val)
            elif par == 'o':
                self.optimal = float(val)
            elif par == 'g':
                self.individual.group_size = int(val)
            elif par == 'x':
                self.rend = True
            elif par == 'z':
                self.function = val


def make_local_search(fname):
    obj = LocalSearch(fname)
    return obj