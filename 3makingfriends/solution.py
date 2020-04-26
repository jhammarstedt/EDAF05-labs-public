import sys

from collections import deque
from graph import Graph


def init():
    raw_data = []                           
    for input in sys.stdin:
        raw_data.append(input.strip())                                      # append every input line to raw_data

    num_of_nodes = int(raw_data[0].split(' ')[1])                           # extract number of nodes from first line
    edges = [[int(i) for i in line.split(' ')] for line in raw_data[1:]]    # extract [u, v, weight] arrays to edge array

    return edges, num_of_nodes


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])                                          # sort edges in order of weight
    edges = deque(edges)                                                    # place edges in work queue
    T = Graph(n)                                                            # initiate graph 
    mst_edges = []                                                          # list of edges part of minimal spanning tree 

    while edges:                                                            # iterate through queue of sorted edges
        current_edge = edges.popleft()
        if T.find(current_edge[0]) != T.find(current_edge[1]):              # if edges not part of same set...
            T.union(current_edge)                                           # ...add edge to T-graph
            mst_edges.append(current_edge)                                  # ...add edge to MST list
    return mst_edges


def print_cost(edges):
    total_cost= 0
    for e in edges:                                                         # iterate through MST list...
        total_cost += e[2]                                                  # calc sum of weights
    print(total_cost)
        

def main():              
    data, n = init()                                                        # O(2*n + 3*n) = O(n), where n = number of lines.
    mst_edges = kruskal(data, n)                                            # O(n*log(n)[sort] + n[loop] + [find] ) = O(n*log(n))
    final_cost = get_cost(mst_edges)                                        # O(n-1), where n = number of nodes.

if __name__== "__main__": main()

