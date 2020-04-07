import sys
from graph import Vertex, Graph


def get_data():
    raw_data = []                           
    for input in sys.stdin:
        raw_data.append(input.strip())              # import every line from system in
    
    N = int(raw_data[0].split(" ")[0])              # extract N from the input data
    Q = int(raw_data[0].split(" ")[1])              # extract Q from the input data
   
    elements = raw_data[1:N+1]                      # extract the graph elements from the input data
    query_list = raw_data[N+1:]                     # extract the queries from the input data
    
    queries = []
    for query in query_list:                    
        queries.append(query.split(" "))            # split query string into array

    return elements, queries                        # return graph elements and queries



def sort_letters(word):
    return word[0] + ''.join(sorted(word[1:]))      # head + sorted(tail)



def create_set(elements):
    element_set = set()                             # empty set
    for e in elements:
        element_set.add(sort_letters(e))            # add every sorted element to set
    return element_set



def create_graph(elements):
    graph = Graph()                                 # empty graph

    for word in elements:
        graph.add_vertex(word)                      # create vertices for every word

    for word in elements:
        tail = word[1:]                             # the tail (last 4 letters) of the word
        for neighbour in elements:
            if set(tail) <= set(neighbour):         # if tail is a subset of neighbour...
                if word != neighbour:               # ... but not the same word as ...
                    graph.add_edge(word, neighbour) # ... then add the edge
    
    return graph
        
    

def BFS2(start, goal, graph):
    start_node = graph.get_vertex(start)            # start node
    goal_node = graph.get_vertex(goal)              # goal node
    neighbours = start_node.get_connections()       # every neighbour of start node

    if start_node == goal_node:
        return 0

    return BFSrecursive(start_node, goal_node, neighbours)


def BFSrecursive(start_node, goal_node, nodes):
    if nodes:
        for node in nodes:
            if node == goal_node:
                return 1
            elif not node.is_visited():
                node.set_visited()
                return 1 + int(BFSrecursive(node, goal_node, node.get_connections()))
    return 200000
   

def BFS(start, goal, graph):
    start_node = graph.get_vertex(start)            # start node
    goal_node = graph.get_vertex(goal)              # goal node

#print('Finding path from ',start_node.id, 'to ', goal_node.id)
    
    start_node.check = True                         #set the first node to true
    q = [start_node]
    
    while len(q) != 0:
        v = q.pop(0)
        neighbours = v.get_connections()                #Get all neighbours
        for granne in neighbours:
            if not granne.check:                        #if we havent checked it yet
                granne.check=True
                q.append(granne)
                if granne == goal_node:
                    print('Found path! Lenght: ',len(q))
                    return len(q)
    
    return "Impossible" 
  


def print_results(results):
    for e in results:
        print(e)



def main():                                     
    elements, queries = get_data()                  # get data from standard input
    elements_set = create_set(elements)             # create set of relevant elements
    graph = create_graph(elements_set)              # create a graph

    results = []
    for query in queries:
        start = sort_letters(query[0])              # start node converted to head + sorted(tail)
        goal = sort_letters(query[1])               # goal node converted to head + sorted(tail)
        print('Finding path from ',query[0],' to ',query[1])
        results.append(BFS(start, goal, graph))     # BFS for every query in queries

    print_results(results)                          # print results 

if __name__== "__main__": main()
