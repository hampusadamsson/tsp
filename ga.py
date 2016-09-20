from chromosome import create_ind, create_empty_ind
import random
import copy


class Ga:
    cities = []
    pop_size = 250
    generations = 250
    elitism = 4
    mutChance = 1
    nrMutates = 3
    pop = []

    def run(self):
        pop_size = int(len(self.cities) * 14)
        generations = len(self.cities) * 14
        elitism = int(pop_size * 0.05) + 1
        mut_rate = 0.1
        mut_count = int(len(self.cities)*0.2 + 1)

        for a in range(0, pop_size):
            tmp = create_ind(self.pop[0])
            self.pop.append(tmp)

        for a in range(0, generations):
            self.pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
            next_gen = []

            print("GEN: " + str(a) + ', POP: ' + str(len(self.pop)) + ', best: ' + str(self.pop[len(self.pop)-1].fit))

            # selection
            # crossover

            for i in range(elitism, pop_size):
                parents = self.select()
                child = self.two_point(parents[0], parents[1])
                next_gen.append(child)

            # mutation
            for ind in next_gen:
                for i in range(0, mut_count):
                    val = random.uniform(0, 1)
                    if val < mut_rate:
                        self.mutate(ind)

            # elitism
            for i in range(0, elitism):
                next_gen.append(self.pop.pop())
            self.pop = next_gen
        self.pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
        ans = self.pop[len(self.pop)-1]
        self.pop = []
        return ans

    def sel(self):
        max_val = sum([(1/c.fit) for c in self.pop])
        pick = random.uniform(0, max_val)
        current = 0
        for chromosome in self.pop:
            current += (1/chromosome.fit)
            if current > pick:
                return chromosome

    def select(self):
        ret = []
        while len(ret) != 2:
            selected = self.sel()
            ret.append(selected)
            if len(ret) == 2 and ret[0] == ret[1]:
                ret.pop()
        return ret

    def one_point(self, ind1, ind2):
        new_ind = copy.deepcopy(ind1)
        p1 = random.randint(0, len(ind1.cities) - 1)

        for i in range(p1, len(ind1.cities) - 1):
            for j in range(0, len(ind1.cities)-1):
                if new_ind.cities[i].index == ind2.cities[j].index:
                    id_swap = i
                    id_swap2 = j
                    new_ind.cities[id_swap], new_ind.cities[id_swap2] = new_ind.cities[id_swap2], new_ind.cities[id_swap]

        new_ind.calc_solution(new_ind.cities)
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
        new_ind.calc_solution()
        return new_ind

    # swaps 2 cities
    def mutate(self, ind):
        cities = ind.cities
        rand1 = random.randint(0, len(cities)-1)
        rand2 = rand1
        while rand1 == rand2:
            rand2 = random.randint(0, len(cities)-1)
        cities[rand2], cities[rand1] = cities[rand1], cities[rand2]
        ind.calc_solution()
        return ind

    def load_cities(self, fname):
        self.pop = []
        chrome = create_empty_ind()
        chrome.load_file(fname)
        self.cities = chrome.cities
        if len(self.cities) != 0:
            chrome.calc_solution()
        self.pop.append(chrome)


def make_ga():
    gan = Ga()
    return gan


