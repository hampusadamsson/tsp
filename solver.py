from city import *
from ga import make_ga

from os import listdir
files = [f for f in listdir('data')]
for prob in files:
    GA = make_ga()
    GA.load_cities('C:\\Users\\hampu\\PycharmProjects\\TSP\\data\\' + prob)
    if 50 > len(GA.cities) > 0:
        print(prob)
        print(len(GA.cities))
        best = GA.run()
        sol = best.fit
        print(sol)