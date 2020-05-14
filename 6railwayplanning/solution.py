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
    N = attrib[0]                                  #number of stations, 
    for i in range(0,attrib[0]):                   #number of nodes we wish to create
        g.add_node(name=i)
    for i in nodes:
        g.add_edge(frm=i[0],to=i[1],capacity=i[2]) #first element contains from,second to, third capacity
        g.add_edge(frm=i[1],to=i[0],capacity=i[2]) 
    g.print_graph()
    e =g.nodes[0].get_edges()
    print(e[1].cnode.is_visited())

def BFS(start, goal, graph, token):
    start_node = graph.get_node(start)
    goal_node = graph.get_node(goal)

    if start == goal:                                   # early out, if same node
        return 0
    elif start_node == goal_node:                       # early out, if same tail+head combination
        return 1

    queue = collections.deque()
    queue.append(start_node)                            # queue <- first node
    level = { start_node:0 }                            # level(first node) <- 0

    #a bit unsure of this one
    while queue:
        v = queue.popleft()
        neighbours = v.get_edges()                 # get all neighbours
        for edge in neighbours:
            if not edge.cnode.is_visited(token):      # if the connected node not yet visited
                edge.cnode.set_visited(token)               
                queue.append(edge)                         # add node n to queue 
                level[edge.cnode.id] = level[v.id] +1                  # increment level value
                if edge.cnode == goal_node:
                    return level[edge.cnode.id]                     # goal found -> return level value
    return "Impossible"                                 # goal not found -> return "Impossible"


def main():
    info,nodes,removal=get_data()
    print(info)
    print(nodes)
    print(removal)
    graph = create_graph(info,nodes)

if __name__=='__main__': main()



def old_main_labb2():                                     
    elements, queries = get_data()                      # get data from standard input
    elements_set = create_set(elements)                 # create set of relevant elements
    graph = create_graph(elements_set)                  # create a graph of the elements from set

    results = []
    token = 1                                           # initiate visit token to 1
    for query in queries:
        start = query[0]                                # start node from query list
        goal = query[1]                                 # goal noded from query list
        results.append(BFS(start, goal, graph, token))  # BFS for every query in queries
        token += 1                                      # increment token

    print_results(results)   

