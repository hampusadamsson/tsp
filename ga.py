from city import *
from random import shuffle
import random
import copy


class Ga:
    cities = []
    pop_size = 250
    generations = 250
    elitism = 4
    mutChance = 1
    nrMutates = 3

    def __init__(self, cit):
        self.cities = cit

    def run(self):
        sol = calc_solution(self.cities)
        print(sol)

        pop_size = int(len(self.cities) * 8)
        generations = len(self.cities) * 8
        elitism = int(pop_size * 0.1) + 1
        mut_rate = 0.1
        mut_count = int(len(self.cities)*0.3 + 1)

        pop = []
        for a in range(0, pop_size):
            tmp = create_ind(self.cities)
            pop.append(tmp)

        for a in range(0, generations):
            pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
            next_gen = []

        #    print("GEN: " + str(a) + ', POP: ' + str(len(pop)) + ', best: ' + str(pop[len(pop)-1].fit))

            # selection
            for i in range(elitism, pop_size):
                parents = self.select(pop)
                child = self.two_point(parents[0], parents[1])
                next_gen.append(child)
            # crossover

            # mutation
            for ind in next_gen:
                for i in range(0, mut_count):
                    val = random.uniform(0, 1)
                    if val < mut_rate:
                        self.mutate(ind)

            # elitism
            for i in range(0, elitism):
                next_gen.append(pop.pop())

            pop = next_gen
        pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
        return pop[len(pop)-1].cities

    def sel(self, pop):
        max_val = sum([(1/c.fit) for c in pop])
        pick = random.uniform(0, max_val)
        current = 0
        for chromosome in pop:
            current += (1/chromosome.fit)
            if current > pick:
                return chromosome

    def select(self, pop):
        ret = []
        while len(ret) != 2:
            selected = self.sel(pop)
            ret.append(selected)
            if len(ret) == 2 and ret[0] == ret[1]:
                ret.pop()
        return ret

    def one_point(self, ind1, ind2):
        new_ind = copy.deepcopy(ind1)
        p1 = random.randint(0, len(ind1.cities) - 2)
    #    print_sol(ind1.cities)
    #    print_sol(ind2.cities)
    #    print("--")
    #    print_sol(new_ind.cities)

        for i in range(p1, len(ind1.cities) - 1):
            for j in range(0, len(ind1.cities)-1):
                if new_ind.cities[i].index == ind2.cities[j].index:
                    id_swap = i
                    id_swap2 = j
                    new_ind.cities[id_swap], new_ind.cities[id_swap2] = new_ind.cities[id_swap2], new_ind.cities[id_swap]

    #    print_sol(new_ind.cities)
    #    print("done")
        new_ind.fit = calc_solution(new_ind.cities)
        return new_ind


    def two_point(self, ind1, ind2):
        new_ind = copy.deepcopy(ind1)
        p1 = random.randint(0, len(ind1.cities) - 1)
        p2 = random.randint(p1, len(ind1.cities) - 1)

        for i in range(p1, p2):
            for j in range(0, len(ind1.cities)-1):
                if new_ind.cities[i].index == ind2.cities[j].index:
                    id_swap = i
                    id_swap2 = j
                    new_ind.cities[id_swap], new_ind.cities[id_swap2] = new_ind.cities[id_swap2], new_ind.cities[id_swap]

        new_ind.fit = calc_solution(new_ind.cities)
        return new_ind

    # swaps 2 cities
    def mutate(self, ind):
        cities = ind.cities
        rand1 = random.randint(0, len(cities)-1)
        rand2 = rand1
        while rand1 == rand2:
            rand2 = random.randint(0, len(cities)-1)
        cities[rand2], cities[rand1] = cities[rand1], cities[rand2]
        ind.fit = calc_solution(cities)
        return ind


def make_ga(cities):
    gan = Ga(cities)
    return gan


class Individual:
    cities = []
    fit = 0

    def __init__(self, cit):
        self.cities = cit
        self.fit = calc_solution(cit)


def create_ind(cities):
    ind = copy.deepcopy(cities)
    shuffle(ind)
    new_individual = Individual(ind)
    return new_individual
