from make_data import calculate_distance

import heapq
import pandas as pd

def floydWarshall(graph, nodes=49):
    
    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(nodes):
 
        # pick all vertices as source one by one
        for i in range(nodes):
 
            # Pick all vertices as destination for the above picked source
            for j in range(nodes):
 
                # If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    
    return pd.DataFrame(distance_matrix)


def shortestPath(adj_list, index_hosp, src: int):
    # Create a priority queue to store vertices that are being preprocessed
    pq = []
    heapq.heappush(pq, (0, src))

    # Create a vector for distances and initialize all distances as infinite (INF)
    dist = [float('inf')] * 49
    dist[src] = 0

    while pq:
        # The first vertex in pair is the minimum distance
        # vertex, extract it from priority queue.
        # vertex label is stored in second of pair
        d, u = heapq.heappop(pq)

        for v in adj_list[u]:
            weight = calculate_distance(
                (index_hosp[u][1], index_hosp[u][2]), (index_hosp[v][1], index_hosp[v][2])
            
            )
            # If there is shorted path to v through u.
            if dist[v] > dist[u] + weight:
                # Updating distance of v
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist