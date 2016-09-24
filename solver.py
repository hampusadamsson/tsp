from ga import make_ga
from simulated_annealing import make_sim_ann
import sys


def sim_a_solver(prob):
    sim = make_sim_ann(prob)
    print('SA - ' + prob)
    best = sim.run()
    sol = best.fit
    best.save_sol()
    print('FIT: ' + str(sol))
    print('----')
    plot_res(res)


def ga_solver(prob, param):
    GA = make_ga(prob)
    GA.parse_input(param)

    print('GA - ' + prob)
    best = GA.run()
    sol = best.fit
    best.save_sol()
    print('FIT: ' + str(sol))
    print('----')


#sim_a_solver(sys.argv[1])

if 1==1:
    if sys.argv[1] == '-help' or sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '--h':
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
        ga_solver(city, prob)
