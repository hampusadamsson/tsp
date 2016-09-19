from city import *
from alg_random import *
from ga import *

def load_file(fname):
    with open(fname, "r") as ins:
        cities = []
        for line in ins:
            if "GEO" in line:
                cities = openGeo(ins, "GEO")
                break
            if "EUC_2D" in line:
                cities = openGeo(ins, "EUC_2D")
                break
        ins.close()
        return cities

def openGeo(ins, graph_type):
    cities = []
    for line in ins:
        tmp = line.split(' ')
        tmp = [x for x in tmp if x]
        if len(tmp) == 3:
            try:
                city = make_city(tmp[0], float(tmp[1]), float(tmp[2]))
                if graph_type == 'GEO':
                    city.geo()
                cities.append(city)
            except ValueError:
                print(tmp)
    return cities

from os import listdir
files = [f for f in listdir('data')]
for prob in files:
    cities = load_file('C:\\Users\\hampu\\PycharmProjects\\TSP\\data\\' + prob)
    if 75 > len(cities) > 0:
        print(prob)
        gan = Ga(cities)
        cities = gan.run()
        sol = calc_solution(cities)
        print(sol)
