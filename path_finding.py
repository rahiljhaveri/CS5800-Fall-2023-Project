import heapq
import sys

def min_distance_node(dist, shortest_path_nodes):
    min_dist = sys.maxsize
    
    for u in range(len(dist)):
        if dist[u] < min_dist and shortest_path_nodes[u] == False:
            min_dist = dist[u]
            min_node = u

    return min_node


def dijkstra(adj_mat, src):
    dist = [sys.maxsize] * len(adj_mat)
    dist[src] = 0
    shortest_path_nodes = [False] * len(adj_mat)

    for _ in range(49):
        x = min_distance_node(dist, shortest_path_nodes)

        shortest_path_nodes[x] = True

        for y in range(49):
            dd = dist[x] + adj_mat[x][y]
            if adj_mat[x][y] > 0 and shortest_path_nodes[y] == False and dist[y] > dd:
                dist[y] = dd
                
    return dist


def floydWarshall(graph, nodes=49):
    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
    
    return distance_matrix
