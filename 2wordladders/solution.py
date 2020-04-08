import sys
from graph import Vertex, Graph


def get_data():
    """ Returns the formatted data fetched from stdin. """
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


def sort_tail(word):
    """ Sorts the tail (every letter but the first) in alphabetical order. """
    return word[0] + ''.join(sorted(word[1:]))  


def create_set(elements):
    """ Creates a unique set of elements, elements with the same head+tail combination are ignored. """
    element_set = set()                      
    for e in elements:
        element_set.add(sort_tail(e))       
    return element_set


def compare_strings(tail, unsorted_string):
    string = sorted(unsorted_string)
    index = 0
    diff = 0
    while index < len (tail):
        if tail[index] != string[index + diff]:
            diff += 1
        else:
            index += 1
        if diff > 1:
            return False
    return True



def create_graph(elements):
    graph = Graph()                                     # empty graph
    
    for word in elements:
        graph.add_vertex(word)                          # create vertices for every word

    for word in elements:
        tail = word[1:]                                 # the tail (last 4 letters) of the word
        for neighbour in elements:
            compare_strings(tail, neighbour)
            if compare_strings(tail, neighbour):        # if tail is a subset of neighbour...
                if word != neighbour:                   # ... but not the same word as ...
                    graph.add_edge(word, neighbour)     # ... then add the edge
    return graph
        
    
def BFS(start, goal, graph, token):
    start_node = graph.get_vertex(sort_tail(start))     # start node
    goal_node = graph.get_vertex(sort_tail(goal))       # goal node

    if start == goal:                                   # early out, if same node
        return 0
    elif start_node == goal_node:                       # early out, if same tail+head combination
        return 1

    queue = [start_node]                                # queue <- first node
    level = { start_node:0 }                            # level(first node) <- 0

    while queue:
        v = queue.pop(0)
        neighbours = v.get_neighbours()                 # get all neighbours
        for n in neighbours:
            if not n.is_visited(token):                 # if neighbour not yet visited
                n.set_visited(token)               
                queue.append(n)                         # add node n to queue 
                level[n] = level[v] +1                  # increment level value
                if n == goal_node:
                    return level[n]                     # goal found -> return level value
    return "Impossible"                                 # goal not found -> return "Impossible"


def print_results(results):
    """ Prints the result. """
    for e in results:
        print(e)



def main():                                     
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

    print_results(results)                              # print results 

if __name__== "__main__": main()
