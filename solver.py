from ga import make_ga
from simulated_annealing import make_sim_ann
from os import listdir
import time


def sim_a_solver(prob):
    sim = make_sim_ann('data\\' + prob)

    if 105 > len(sim.cities) > 0:
        start = time.time()
        print('SA - ' + prob)
        best = sim.run()
        sol = best.fit
        best.save_sol(prob + '_SA')
        print('SA - timing:' + str(time.time() - start))
        print('FIT: ' + str(sol))
        print('----')

def ga_solver(prob):
    GA = make_ga('data\\' + prob)
    if 105 > len(GA.cities) > 0:
        start = time.time()
        print('GA - ' + prob)
        best = GA.run()
        sol = best.fit
        best.save_sol(prob + '_GA')
        print('GA - timing:' + str(time.time() - start))
        print('FIT: ' + str(sol))
        print('----')


files = [f for f in listdir('data')]
for prob in files:
    sim_a_solver(prob)
    ga_solver(prob)
