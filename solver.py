from ga import make_ga
from LocalSearch import make_local_search
import sys


def ga_solver(prob, param):
    GA = make_ga(prob)
    GA.parse_input(param)

    best = GA.run()
    sol = best.fit
    best.save_sol()
    print(str(sol))


def local_search_solver(prob, param):
    sim = make_local_search(prob)
    sim.parse_input(param)

    best = sim.run()
    sol = best.fit
    best.save_sol()
    print(str(sol))


if sys.argv[1] == '-help' or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '--h':
    print("-z [alg], alg = s,a,l,t,ga")
    print("     (s)imulated annealing")
    print("     simul(a)ted annealing with 2-OPT")
    print("     (t)wo-OPT")
    print("     (ga) genetic algorithm")
    print("     hil(l) climb")
    print("-c cooling")
    print("-t temperature")
    print("-p for population size (-p 100)")
    print("-f for fitness evaluations / generations (-f 100)")
    print("-e for elitism (-e 25)")
    print("-m for mutation rate (-m 0.08) 8% chance of mutating")
    print('-r for amount of cities to mutate on mutation (-m 3) swaps 3 cities')
    print("-x for printing each generation")
    print("   eg.")
    print("python solver.py berlin52.tsp -p 20 -e 10 -f 500 -m 0.08 -r 2")
else:
    city = sys.argv[1]
    prob = ''.join(sys.argv)
    prob = prob.replace(" ", "")
    prob = prob.split("-")

    prob.reverse()
    prob.pop()
    if "ga" in sys.argv:
        ga_solver(city, prob)
    else:
        local_search_solver(city, prob)