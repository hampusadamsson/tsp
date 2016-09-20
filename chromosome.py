from random import shuffle
import copy


class Chromosome:
    cities = []
    fit = 1

    def calc_solution(self):
        if len(self.cities) == 0:
            return 0
        prev_city = self.cities[-1]
        distance = 0
        for c in self.cities:
            cur_city = c
            distance += cur_city.calc_dist_euc2d(prev_city)
            prev_city = cur_city
        self.fit = distance

    def shuffle(self):
        shuffle(self.cities)


def create_ind(cities):
    new_ind = Chromosome()
    new_ind.cities = copy.deepcopy(cities)
    new_ind.calc_solution()
    return new_ind
