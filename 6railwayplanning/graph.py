class Node:
    def __init__ (self,node):
        self.id = node                                 
        self.token = 0  
        self.edges= {}                   

    def get_edges(self):           
        """ Returns every neighbour of the node. """
        return self.edges

    def print_edges(self):
        """ Prints every neighbour of the node. """
        #print(self.edges[1].cnode.id)
        neigh = [[self.edges[neighbour].cnode.id,self.edges[neighbour].capacity] for neighbour in self.edges.keys()]
        #neighbours = [åedge.cnode.id,edge.capacity] for edge in self.edges.keys]
        print(self.id,' is connected to ', neigh)

    def add_edge(self,to_node,capacity):
        """ Connects a neighbour to the node with an edge. """ 
        self.edges[to_node.id]=Edge(to_node=to_node,capacity=capacity)
        
    def is_visited(self, token):
        """ Checks if token has been used for visiting the node. """
        return token <= self.token

    def set_visited(self, token):
        """ Sets a new visit token. """
        self.token = token
    
class Edge:
    """Edges are connected through nodes and accessed from each nodes by a dict of edges"""
    def __init__(self,to_node,capacity):
        self.capacity= capacity             
        self.flow = 0                   #e
        self.cnode= to_node             #the other node which it is connected to 
    def update_flow(new_flow):
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

    def add_edge(self, frm, to,capacity):
        """ Creates an edge between the nodes {frm} and {to}. """
        self.nodes[frm].add_edge(to_node =self.nodes[to],capacity=capacity)

    def get_edge(self,frm,to):
        """Get edge from node to another"""
        #ed = self.nodes[frm].edges[to]
        #print(f'Getting edge from {self.nodes[frm].id} to {self.nodes[to].id} with capacity {ed.capacity}')
        return self.nodes[frm].edges[to]
    def print_graph(self):
        """ Prints the graph. """
        for node in self.nodes:
            self.nodes[node].print_edges()        

class Residual_graph(Graph):
      def __init__(self):
          super().__init__() #gets all the attributes from G


def old_extra_for_reference():
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
        
