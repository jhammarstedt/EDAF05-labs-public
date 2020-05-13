class Node:
    def __init__ (self,node,height=0):
        self.id = node                       
        #self.connections = []
        self.height = height                             
        self.edges = {}
    def get_neighbours(self):           
        """ Returns every neighbour of the node. """
        return self.edges

    def print_connections(self):
        """ Prints every neighbour of the node. """
        neighbours = [[node[0].id,node[1]] for node in self.edges] #print each node with it's capacity
        print(self.id,' is connected to [x with capacity y]', neighbours)

    def add_connection(self, neighbour,capacity):
        """ Connects a neighbour to the node. So you can get this node by nodes[0].edges[neighbour] """
        self.edges[neighbour.id] = Edge(to_node=neighbour,capacity=capacity)
        #self.edges.append([neighbour,capacity])
  
    
class Edge:
    def __init__(self,to_node,capacity=0):

        self.capacity= capacity             
        self.flow = self.capacity       #should be set to capacity for all nodes connected to s (node 0 in our case), for the others it starts at 0
        self.delta=0                    #for the residual
    
    def update_flow(self,new_flow):
        """we will change the flow by delta"""
        self.flow = new_flow
        
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
    
