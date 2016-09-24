from chromosome import create_ind
from city import make_city
from plot import plot_res


class sim_ann:
    cities = []
    individual = []

    def __init__(self, fname):
        self.load_cities(fname)

    def run(self):
        self.individual = create_ind(self.cities)
        res = self.individual.simulated_annealing()
        plot_res(res)
        return self.individual

    def load_cities(self, fname):
        with open(fname, "r") as ins:
            cities = []
            for line in ins:
                tmp = line.split(' ')
                tmp = [x for x in tmp if x]
                if len(tmp) == 3:
                    try:
                        city = make_city(tmp[0], float(tmp[1]), float(tmp[2]))
                        cities.append(city)
                    except ValueError:
                        err = ValueError
        ins.close()
        self.cities = cities

def make_sim_ann(fname):
    obj = sim_ann(fname)
    return obj
