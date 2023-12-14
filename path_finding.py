import sys

def minDistanceNode(dist, shortest_path_nodes):
    '''
    the dist list is used to check for the minimum distance 
    and return the node having that min distance if it is 
    not already a part of the shortest path nodes set
    '''
    min_dist = sys.maxsize
    
    for u in range(len(dist)):
        if dist[u] < min_dist and shortest_path_nodes[u] == False:
            min_dist = dist[u]
            min_node = u

    return min_node


def dijkstraWithPath(adj_mat, src):
    '''
    the dijkstra's single source shortest path algorithm is implemented
    on a graph represented as an adjacency matrix provided a source node.
    '''
    
    total_nodes = len(adj_mat)
    dist = [sys.maxsize] * total_nodes
    dist[src] = 0
    shortest_path_nodes = [False] * total_nodes
    parent_node = [src] * total_nodes

    for _ in range(total_nodes):
        x = minDistanceNode(dist, shortest_path_nodes)

        shortest_path_nodes[x] = True

        for y in range(total_nodes):
            dd = dist[x] + adj_mat[x][y]
            if adj_mat[x][y] > 0 and shortest_path_nodes[y] == False and dist[y] > dd:
                dist[y] = dd
                parent_node[y] = x
                
    return dist, parent_node


def floydWarshallWithPath(adj_mat):
    '''
    Floyd Warshall is an all source shortest path algorithm implemented on a graph
    represented as an adjacency matrix.
    This function returns the shortest path value and a back-tracked parent path.
    '''
    
    total_nodes = len(adj_mat)
    distance_matrix = list(map(lambda i: list(map(lambda j: j, i)), adj_mat))
    path_parent_matrix = [[i] * total_nodes for i in range(total_nodes)]
 
    for k in range(total_nodes):
        for i in range(total_nodes):
            for j in range(total_nodes):
                if distance_matrix[i][k] + distance_matrix[k][j] < distance_matrix[i][j]:
                    path_parent_matrix[i][j] = k
                    distance_matrix[i][j] = distance_matrix[i][k] + distance_matrix[k][j]
    
    return distance_matrix, path_parent_matrix
