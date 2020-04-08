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



def compare_strings(tail, unsorted_string):
    """
    i = 1
    while i < len(string):
        if tail[i-1] != string[i]:
            if tail[i-1] != string[0]:
                return False
        i += 1
    return True
    """
    string = sorted(unsorted_string)
    index = 0
    diff = 0
    while index + diff < len (tail):
        if tail[index] != string[index + diff]:
            diff += 1
        else:
            index += 1
        if diff > 1:
            return False
    return True


"""
    i = 0
    fail = 0
    while i + fail < len(string):
        if tail[i] != string[i+fail]:
            fail += 1
        i += 1
    return fail < 2
"""



def create_graph(elements):
    graph = Graph()                                 # empty graph
    
    for word in elements:
        graph.add_vertex(word)                      # create vertices for every word

    for word in elements:
        tail = word[1:]                             # the tail (last 4 letters) of the word
        for neighbour in elements:
            compare_strings(tail, neighbour)
            #if list(tail) > list(neighbour):         # if tail is a subset of neighbour...
            if compare_strings(tail, neighbour):         # if tail is a subset of neighbour...
                if word != neighbour:               # ... but not the same word as ...
                    graph.add_edge(word, neighbour) # ... then add the edge
    
    return graph
        
#    
#
#def BFS2(start, goal, graph):
#    start_node = graph.get_vertex(start)            # start node
#    goal_node = graph.get_vertex(goal)              # goal node
#    neighbours = start_node.get_connections()       # every neighbour of start node
#
#    if start_node == goal_node:
#        return 0
#
#    return BFSrecursive(start_node, goal_node, neighbours)
#
#
#def BFSrecursive(start_node, goal_node, nodes):
#    if nodes:
#        for node in nodes:
#            if node == goal_node:
#                return 1
#            elif not node.is_visited():
#                node.set_visited()
#                return 1 + int(BFSrecursive(node, goal_node, node.get_connections()))
#    return 200000
#   
def reset_visitors(visitors):
    for node in visitors:
        node.remove_visited()
token = 0
    
def BFS(start, goal, graph):
    start_node = graph.get_vertex(start)            # start node
    goal_node = graph.get_vertex(goal)              # goal node
    
    global token
    token = token + 1

    if start_node == goal_node:                     # early out, if start = goal
        return 0
    
    start_node.set_visited(token)                         #set the first node to true
    q = [start_node]
    #xvisited =[start_node]
    layer_count= 1
    level = {}
    level[start_node] = 0
    while q:

        v = q.pop(0)
        #v.print_connections()
        neighbours = v.get_connections()                #Get all neighbours
        for n in neighbours:
            if not n.is_visited(token):                        #if we havent checked it yet
                n.set_visited(token)               
                #visited.append(n)                          
                q.append(n)
                level[n] = level[v] +1
                #n.add_pred(v)
                if n == goal_node:
    #                print('Found path! Lenght: ',layer_count)    
                    #reset_visitors(visited)             #reset the checks so that all nodes are unvisited                                 
                    #return
                    return level[n]


        layer_count += 1
    #reset_visitors(visited)                             #if it was impossible to find a path we still want to reset
    return "Impossible" 


def print_results(results):
    for e in results:
        print(e)



def main():                                     
    elements, queries = get_data()                  # get data from standard input
    elements_set = create_set(elements)             # create set of relevant elements
    graph = create_graph(elements_set)              # create a graph
    #graph = create_graph(elements)

    #graph.print_graph()

    results = []
    for query in queries:
        start = sort_letters(query[0])              # start node converted to head + sorted(tail)
        goal = sort_letters(query[1])               # goal node converted to head + sorted(tail)
        #start = query[0]
        #goal = query[1]
        #print('Finding path from ',query[0],' to ',query[1])
        results.append(BFS(start, goal, graph))     # BFS for every query in queries

    print_results(results)                          # print results 

if __name__== "__main__": main()
