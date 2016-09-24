from chromosome import create_ind
from city import make_city
import random
from plot import plot_res
import copy


class Ga:
    rend = False
    cities = []
    pop_size = 25
    generations = 1000
    elitism = 5
    mut_rate = 0.08
    mut_count = 3
    pop = []
    solutions = []
    trash = []

    def __init__(self, fname):
        self.pop = []
        self.load_cities(fname)

    def run(self):
        for a in range(0, self.pop_size):
            tmp = create_ind(self.cities)
            tmp.shuffle()
            self.pop.append(tmp)

            tmp = create_ind(self.cities)
            self.trash.append(tmp)

        for a in range(0, self.generations):
            self.pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
            next_gen = []

            #  Write out each generation
            if self.rend:
                print("GEN: " + str(a) + ', POP: ' + str(len(self.pop)) + ', best: ' + str(self.pop[len(self.pop)-1].fit))

            self.solutions.append(self.pop[len(self.pop)-1].fit)

            #  save to file
            #self.pop[len(self.pop) - 1].save_sol()

            #  selection
            #  crossover
            for i in range(self.elitism, self.pop_size):
                parents = self.select()
#                child = self.two_point(parents[0], parents[1])
                child = self.scx(parents[0], parents[1])
                next_gen.append(child)

            #  mutation
            for ind in next_gen:
                for i in range(0, self.mut_count):
                    val = random.uniform(0, 1)
                    if val < self.mut_rate:
                        ind.mutate()

            #  elitism
            for i in range(0, self.elitism):
                next_gen.append(self.pop.pop())

            self.trash = self.pop
            self.pop = next_gen

        self.pop.sort(key=lambda chromosome: chromosome.fit, reverse=True)
        ans = self.pop[len(self.pop)-1]
        if self.rend:
                plot_res(self.solutions)
        return ans

    def proportionate_select(self):
        max_val = sum([25000/c.fit for c in self.pop])
        pick = random.uniform(0, max_val)
        current = 0
        for chromosome in self.pop:
            current += (25000/chromosome.fit)
            if current > pick:
                return chromosome

    def rank_select(self):
        total = sum(range(0, len(self.pop) + 1))
        r = random.uniform(0, total)
        tot = 0
        for c in range(1, len(self.pop) + 1):
            if tot + c >= r:
                return self.pop[c - 1]
            tot += c

    def random_select(self):
        r = int(random.uniform(0, len(self.pop)-1))
        return self.pop[r]

    def select(self):
        ret = []
        while len(ret) != 2:
            selected = self.rank_select()
            #selected = self.proportionate_select()
            #selected = self.random_select()
            ret.append(selected)
            if len(ret) == 2 and ret[0] == ret[1]:
                ret.pop()
        return ret

    def scx(self, ind1, ind2):
        new_ind = self.trash.pop()
        new_ind.cities = [copy.copy(ind1.cities[0])]

        while len(ind1.cities) != len(new_ind.cities):

            cand1 = scx_h(ind1, new_ind)
            cand2 = scx_h(ind2, new_ind)

            if new_ind.cities[-1].calc_dist_euc2d_swift(cand1) <= new_ind.cities[-1].calc_dist_euc2d_swift(cand2):
                new_ind.cities.append(copy.copy(cand1))
            else:
                new_ind.cities.append(copy.copy(cand2))
        new_ind.calc_solution()
        return new_ind



    def two_point(self, ind1, ind2):
        new_ind = self.trash.pop()
        p1 = random.randint(0, len(ind1.cities) - 1)
        p2 = random.randint(p1, len(ind1.cities) - 1)

        #for i in range(0, len(new_ind.cities)-1):
        #    new_ind.cities[i] = copy.copy(ind1.cities[i])
        new_ind.cities = copy.copy(ind1.cities)

        for i in range(p1, p2):
            for j in range(0, len(ind1.cities)-1):
                if new_ind.cities[i].id == ind2.cities[j].id:
                    id_swap = i
                    id_swap2 = j
                    new_ind.cities[id_swap], new_ind.cities[id_swap2] = new_ind.cities[id_swap2], new_ind.cities[id_swap]
        new_ind.calc_solution()
        return new_ind

    def load_cities(self, fname):
        with open(fname, "r") as ins:
            cities = []
            for line in ins:
                tmp = line.split(' ')
                tmp = [x for x in tmp if x]
                if len(tmp) >= 3:
                    try:
                        city = make_city(tmp[0], float(tmp[1]), float(tmp[2]))
                        cities.append(city)
                    except ValueError:
                        err = ValueError
        ins.close()
        self.cities = cities
        self.pop_size = int(len(self.cities) * 1)
        self.generations = len(self.cities) * 12
        self.elitism = int(self.pop_size * 0.1) + 1
        self.mut_rate = 0.083
        self.mut_count = int(len(self.cities)*0.13 + 1)

    def parse_input(self, param):
        for p in param:
            par = (p[0])
            val = (p[1:])

            if par == 'p':
                self.pop_size = int(val)
            elif par == 'f':
                self.generations = int(val)
            elif par == 'e':
                self.elitism = int(val)
            elif par == 'm':
                self.mut_rate = float(val)
            elif par == 'r':
                self.mut_count = int(val)
            elif par == 'x':
                self.rend = True


def scx_h(ind, new_ind):
    for i in range(0, len(ind.cities)-2):
        if ind.cities[i].id == new_ind.cities[-1].id:
            cand = ind.cities[i+1]
            dupid = cand.id

            dup = False
            for child in new_ind.cities:
                if dupid == child.id:
                    dup = True
                    break
            if dup == False:
                return cand

    for parent in ind.cities:
        dup = False
        for child in new_ind.cities:
            if parent.id == child.id:
                dup = True
                break
        if dup == False:
            cand = parent
            break
    return cand


def make_ga(fname):
    gan = Ga(fname)
    return gan


