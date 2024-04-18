import shtp

class Digraph:

    def __init__(self, vertices):
        self.V = vertices
        self.edge = []

    def add_edge(self, u, v, w=0):
        self.edge.append([u, v, w])

    def sh_path(self, src, tar, method='bf'):
        if method == 'dk':      # Dijkstra's algorithm
            return shtp.dk(self, src, tar)
        if method == 'bf':      # Bellman Ford algorithm
            return shtp.bf(self, src, tar)
        if method == 'fw':      # Floyd Warshall algorithm
            return shtp.fw(self, src, tar)

