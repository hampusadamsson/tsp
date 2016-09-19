from city import calc_solution
import copy
import random


def random(cities):
    best = calc_solution(cities)
    best_c = copy.deepcopy(cities)

    for count in range(1, 1000):
        random.shuffle(cities)  
        tmp = calc_solution(cities)
        if tmp < best:
            best_c = copy.deepcopy(cities)
            best = tmp
    return best_c


def closest_neighbur(cities):
    sol = []
    random.shuffle(cities)
    sol.append(cities.pop())

    while(len(cities)>0):
        tmp = sol[len(sol)-1].close_neigh(cities)
        sol.append(tmp)
        cities.remove(tmp)
    return sol