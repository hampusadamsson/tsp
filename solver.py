from city import *
from alg_random import *
from ga import *

def load_file(fname):
    with open(fname, "r") as ins:
        cities = []
        for line in ins:
            tmp = line.split(" ")
            if len(tmp) == 4:
                city = make_city(tmp[1], float(tmp[2]), float(tmp[3]))
                cities.append(city)
        ins.close()
        return cities


fname = 'C:\\Users\\hampu\\Downloads\\ulysses16.opt.tour\\ulysses16mod.tsp'
fname = 'C:\\Users\\hampu\\Downloads\\ulysses16.opt.tour\\ulysses16.tsp'

cities = load_file(fname)
cities = ga(cities)
#print_sol(cities)
sol = calc_solution(cities)
print(sol)
