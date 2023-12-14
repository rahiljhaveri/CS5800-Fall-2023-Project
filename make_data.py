from geopy.distance import geodesic

import numpy as np
import pandas as pd
import random

def read_data():
    df = pd.read_csv('Hospitals.csv')
    df = df[df['STATE'] == 'ME']
    return df


def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).miles

        
def indexed_hosp(df):
    index_hosp = df[['NAME', 'LATITUDE', 'LONGITUDE']].sort_values(
        by=['NAME', 'LATITUDE', 'LONGITUDE']
    ).values.tolist()
    return index_hosp


def create_adj_list(index_hosp):
    adj_list = {}
    for i in range(len(index_hosp)):
        x = list(range(0, 49))
        x.remove(i)
        random.seed(42)
        adj_list[i] = {
            r: calculate_distance((index_hosp[i][1], index_hosp[i][2]), (index_hosp[r][1], index_hosp[r][2])) 
            for r in random.sample(x, 10)
        }
    return adj_list


def create_adjmatrix(adj_list):
    '''
    Returns a (weighted) adjacency matrix as a NumPy array.
    '''
    total_nodes = len(adj_list)
    adj_mat = np.full(shape = (total_nodes, total_nodes), fill_value=float('inf'), dtype=float)
    for node, edge in adj_list.items():
        for conn, val in edge.items():
            adj_mat[node][conn] = val
            adj_mat[conn][node] = val 
        adj_mat[node][node] = 0
    
    return adj_mat