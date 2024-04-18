import heapq
import numpy as np


def dk(graph, src, tar):     # Dijkstra's algorithm
    dist = [float('inf')] * graph.V
    dist[src] = 0
    pred = [None] * graph.V
    pred[src] = src
    stp = [tar]  # initialize ShP
    pri_que = [(dist[src], src)]

    while pri_que:
        distance, node = heapq.heappop(pri_que)
        if node == tar:
            break
        if distance > dist[node]:
            continue
        for u, v, w in graph.edge:
            if u == node:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    heapq.heappush(pri_que, (dist[v], v))
    while stp[0] != src:
        stp.insert(0, pred[stp[0]])

    return dist[tar], stp


def bf(graph, src, tar):        # Bellman Ford algorithm
    dist = [float('inf')] * graph.V  # initialize distance
    dist[src] = 0
    pred = [None] * graph.V  # initialize predecessor
    pred[src] = src
    stp = [tar]  # initialize ShP

    for i in range(graph.V):
        for u, v, w in graph.edge:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u

                # Check for negative-weight cycles.
                if i == graph.V - 1:
                    print("Graph contains a negative-weight cycle.")
                    return 0, None
    while stp[0] != src:
        stp.insert(0, pred[stp[0]])

    return dist[tar], stp


def fw(graph, src, tar):         # Floyd Warshall algorithm
    dist = np.full((graph.V, graph.V), np.inf)         # initiate the distance matrix
    np.fill_diagonal(dist, 0)
    pred = [[None for _ in range(graph.V)] for _ in range(graph.V)]  # initiate predecessor matrix
    stp = [tar]

    for u, v, w in graph.edge:
        dist[u, v] = w
        pred[u][v] = u

    for j in range(graph.V):
        for i in range(graph.V):
            for k in range(graph.V):
                if dist[i, k] > dist[i, j] + dist[j, k]:
                    dist[i, k] = dist[i, j] + dist[j, k]
                    pred[i][k] = pred[j][k]
            if dist[i, i] < 0:
                print("Graph contains a negative-weight cycle.")
                return 0, None
    while stp[0] != src:
        stp.insert(0, pred[src][stp[0]])

    return dist[src, tar], stp

