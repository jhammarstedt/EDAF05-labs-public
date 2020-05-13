import sys
from graph import *
""""Get input"""
def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    info = [int(i) for i in raw_data.pop(0).split(' ')]
    nr_nodes = info[0]
    nr_edges = info[1]
    nodes = [[int(i) for i in k.split(' ')] for k in raw_data[0:nr_nodes]]
    removal = [int(i) for i in raw_data[nr_nodes:]]
    
    return info,nodes,removal

def create_graph(attrib,nodes):
    """This function will take in the attributes from the input and the structure of the graph to create a graph object from the graph.py file"""
    g = Graph()
    N = attrib[0]                   # number of stations, 
    for i in range(0,attrib[0]):    #number of nodes we wish to create
        if i ==0: 
            g.add_node(i,height=N)  #setting H(s)=N
        else:g.add_node(i)          # rest of nodes start at 0
    for i in nodes:
        g.add_edge(i[0],i[1],i[2])

    g.print_graph()

def push_ready(high_node,low_node):
    """This is on the residual graph"""
    residual_graf =' '
    if (high_node.exessive_flow > 0) and (high_node.height > low_node.height) and ((high_node and low_node) in residual_graf): #implementera
        return True 
    if check_forward_edge()
    

def push(preflow,height,node_v,node_w):
    if not push_ready(high_node=node_v,low_node=node_w): return 'Not ready to push'#Check 

def main():
    info,nodes,removal=get_data()
    print(info)
    print(nodes)
    print(removal)
    graph = create_graph(info,nodes)

if __name__=='__main__': main()