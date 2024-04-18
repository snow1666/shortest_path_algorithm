import numpy as np
import time
from graph import Digraph

data = "graph2.txt"
g = Digraph(8)                                              # construction of graph
arcs = np.loadtxt(data, skiprows=2, delimiter=";")
for a, b, c in arcs:
    g.add_edge(int(a) - 1, int(b) - 1, c)

start_time_dk = time.time()
dist_dk, st_path_dk = g.sh_path(0, 7, method='dk')
end_time_dk = time.time()
runtime_dk = end_time_dk - start_time_dk
print("Dijkstra:\nA shortest %d-%d-path is:" % (1,8))
print(list(map(lambda x: x + 1, st_path_dk)))
print("with a total length of %0.1f" % dist_dk)
print("The computation took %0.6f seconds" % runtime_dk)
print("\n")

