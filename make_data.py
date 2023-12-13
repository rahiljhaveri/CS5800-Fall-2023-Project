from geopy.distance import geodesic

import numpy as np
import pandas as pd
import random

def read_data():
    df = pd.read_csv('Hospitals.csv')
    df = df[df['STATE'] == 'ME']
    return df

def connected_nodes():
    adj_list = {}
    for i in range(49):
        x = list(range(0, 49))
        x.remove(i)
        adj_list[i] = random.sample(x, 10)
    return adj_list
        
def indexed_hosp(df):
    index_hosp = df[['NAME', 'LATITUDE', 'LONGITUDE']].sort_values(
        by=['NAME', 'LATITUDE', 'LONGITUDE']
    ).values.tolist()
    return index_hosp

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).miles

def weighted_adjmatrix(adj_list, index_hosp, nodes=range(49)):
    '''
    Returns a (weighted) adjacency matrix as a NumPy array.
    '''
    adj_mat = np.full(shape= (49,49), fill_value=9999, dtype=float)
    for node in nodes:
        weights = {
            endnode: calculate_distance(
                (index_hosp[node][1], index_hosp[node][2]), (index_hosp[endnode][1], index_hosp[endnode][2])
            ) for endnode in adj_list.get(node, {})
        }
        for endnode, val in weights.items():
            adj_mat[node][endnode] = val
            adj_mat[endnode][node] = val 
        adj_mat[node][node] = 0
    
    return adj_mat