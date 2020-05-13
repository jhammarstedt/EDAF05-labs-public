import sys
from graph import *

def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    info = [int(i) for i in raw_data.pop(0).split(' ')]
    nr_nodes = info[0]
    nodes = [[int(i) for i in k.split(' ')] for k in raw_data[0:nr_nodes]]
    removal = [int(i) for i in raw_data[nr_nodes:]]
    
    return info,nodes,removal

def create_graph(attrib,nodes):
    """This function will take in the attributes from the input and the structure of the graph to create a graph object from the graph.py file"""
    g = Graph()
    for i in range(0,attrib[0]): #number of nodes we wish to create
        g.add_node(i)
    for i in nodes:
        g.add_edge(i[0],i[1],i[2])

    g.print_graph()
def main():
    info,nodes,removal=get_data()
    print(info)
    print(nodes)
    print(removal)
    graph = create_graph(info,nodes)

if __name__=='__main__': main()