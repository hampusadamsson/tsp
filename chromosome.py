from random import shuffle
from city import make_city
import copy


class Chromosome:
    cities = []
    prob_type = 'EUC_2D'
    fit = 1

    def calc_solution(self):
        if len(self.cities) == 0:
            return 0

        prev_city = self.cities[-1]
        distance = 0
        for c in self.cities:
            cur_city = c
            if self.prob_type == 'GEO':
                distance += cur_city.calc_dist_geo(prev_city)
            elif self.prob_type == 'EUC_2D':
                distance += cur_city.calc_dist_euc2d(prev_city)
            prev_city = cur_city
        self.fit = distance

    def openGeo(self, ins):
        cities = []
        for line in ins:
            tmp = line.split(' ')
            tmp = [x for x in tmp if x]
            if len(tmp) == 3:
                try:
                    city = make_city(tmp[0], float(tmp[1]), float(tmp[2]))
                    if self.prob_type == 'GEO':
                        city.geo()
                    cities.append(city)
                except ValueError:
                    print(tmp)
        self.cities = cities

    def load_file(self, fname):
        with open(fname, "r") as ins:
            for line in ins:
                if "GEO" in line:
                    self.prob_type = "GEO"
                    break
                if "EUC_2D" in line:
                    self.prob_type = "EUC_2D"
                    break
            self.openGeo(ins)
            ins.close()


def create_ind(ind):
    new_ind = copy.deepcopy(ind)
    shuffle(new_ind.cities)
    new_ind.calc_solution()
    return new_ind


def create_empty_ind():
    new_individual = Chromosome()
    new_individual.calc_solution()
    return new_individual
