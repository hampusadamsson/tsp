from city import *
from random import shuffle
import random
import copy

pop_size = 100
generations = 500
elitism = 10
mutChance = 1
nrMutates = 3


def ga(cities):
    pop = []
    for a in range(0, pop_size):
        tmp = create_ind(cities)
        pop.append(tmp)

    for a in range(0, generations):
        pop.sort(key=lambda chrom: chrom.fit, reverse=True)
        next_gen = []

        print("GEN: " + str(a) + ', POP: ' + str(len(pop)) + ', best: ' + str(pop[len(pop)-1].fit))

        # selection
        for i in range(elitism, pop_size):
            parents = select(pop)
            child = one_point(parents[0], parents[1])
            next_gen.append(child)
        # crossover

        # elitism
        for i in range(0, elitism):
            next_gen.append(pop.pop())

        # mutation
        for ind in pop:
            for i in range(0, nrMutates):
                val = random.uniform(0, 1)
                if val < mutChance:
                    mutate(ind)

#        pop.sort(key=lambda chrom: chrom.fit, reverse=True)
#        for x in range(len(next_gen), pop_size):
#            next_gen.append(pop[x])

        pop = next_gen
    pop.sort(key=lambda chrom: chrom.fit, reverse=True)
    return pop[len(pop)-1].cities


def sel(pop):
    max = sum([c.fit for c in pop])
    pick = random.uniform(0, max)
    current = 0
    for chrom in pop:
        current += chrom.fit
        if current > pick:
            return chrom


def select(popen):
    ret = []
    for i in range(0, 2):
        seled = sel(popen)
        ret.append(seled)
    return ret

def one_point(ind1, ind2):
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


def two_point(ind1, ind2):
    new_ind = copy.deepcopy(ind1)
    p1 = random.randint(0, len(ind1.cities) - 1)
    p2 = random.randint(p1, len(ind1.cities) - 1)

    print_sol(new_ind.cities)

    for i in range(p1, p2):
        cities = new_ind.cities
        for j in range(0, len(new_ind.cities)-1):
            if ind2.cities[j].index == ind2.cities[i].index:
                id_swap = j
        cities[id_swap], cities[i] = cities[i], cities[id_swap]

    print_sol(new_ind.cities)
    new_ind.fit = calc_solution(new_ind.cities)
    return new_ind

# swaps 2 cities
def mutate(ind):
    cities = ind.cities
    rand1 = random.randint(0, len(cities)-1)
    rand2 = rand1
    while(rand1 == rand2):
        rand2 = random.randint(0, len(cities)-1)
    cities[rand2], cities[rand1] = cities[rand1], cities[rand2]
    ind.fit = calc_solution(cities)
    return ind


# CLASS
#
#
class individual:
    cities = []
    fit = 0

    def __init__(self, cit):
        self.cities = cit
        self.fit = calc_solution(cit)


def create_ind(cities):
    ind = copy.deepcopy(cities)
    shuffle(ind)
    individ = individual(ind)
    return individ
