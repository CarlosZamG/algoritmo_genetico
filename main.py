from genetic_algorithm import find_roots
import matplotlib.pyplot as plt
import numpy as np

def run():
    f = lambda x: np.cos(x)
    limit_1 = -7
    limit_2 = 7
    roots = find_roots(f, limit_1, limit_2, 50, 8)
    fig, ax = plt.subplots()
    xplot = np.linspace(limit_1, limit_2)
    plt.grid()
    ax.plot(xplot, f(xplot))
    ax.scatter(roots, f(roots), c = roots.size*[3])
    plt.savefig("graph.svg")
    plt.close()




if __name__ == "__main__":
    run()