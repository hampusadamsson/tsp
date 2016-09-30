import matplotlib.pyplot as plt


def plot_res(val1, optimal):
    plt.plot(val1, color='g')
    plt.plot(([int(optimal)] * len(val1)), color='r')
    plt.ylabel('Fitness')
    plt.xlabel('Generations')
    plt.show()