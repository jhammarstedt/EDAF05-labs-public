class Node:
    def __init__ (self,node):
        self.id = node                       
        self.connections = []                               

    def get_neighbours(self):           
        """ Returns every neighbour of the node. """
        return self.connections

    def print_connections(self):
        """ Prints every neighbour of the node. """
        neighbours = [[node[0].id,node[1]] for node in self.connections] #print each node with it's capacity
        print(self.id,' is connected to [x with capacity y]', neighbours)

    def add_connection(self, neighbour,capacity):
        """ Connects a neighbour to the node. """ 
        self.connections.append([neighbour,capacity])
  
    


class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def add_node(self, name):
        """ Adds a new vertex to the graph. """
        self.num_nodes += 1
        self.nodes[name] = Node(name)

    def get_node(self, name):
        """ Returns the vertex of id {name}, or None if {name} can't be found. """
        if name in self.nodes:
            return self.nodes[name]
        else:
            return None

    def add_edge(self, node1, node2,capacity):
        """ Creates an edge between the nodes {node1} and {node1} with given capacity. """
        self.nodes[node1].add_connection(self.nodes[node2],capacity)
        self.nodes[node2].add_connection(self.nodes[node1],capacity) #creating it twice for now since it's undirected
    def print_graph(self):
        """ Prints the graph. """
        for node in self.nodes:
            self.nodes[node].print_connections()        
    
