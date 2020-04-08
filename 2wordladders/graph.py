class Vertex:
    def __init__ (self,node):
        self.id = node                       
        self.adjacency_list = []            
        self.token = 0                     

    def get_neighbours(self):           
        """ Returns every neighbour of the node. """
        return self.adjacency_list

    def print_connections(self):
        """ Prints every neighbour of the node. """
        neighbours = [node.id for node in self.adjacency_list]
        print(self.id,' is connected to ', neighbours)

    def add_neighbour(self, neighbour):
        """ Connects a neighbour to the node. """ 
        self.adjacency_list.append(neighbour)
        
    def is_visited(self, token):
        """ Checks if token has been used for visiting the node. """
        return token <= self.token

    def set_visited(self, token):
        """ Sets a new visit token. """
        self.token = token
    


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def add_vertex(self, name):
        """ Adds a new vertex to the graph. """
        self.num_vertices += 1
        self.vertices[name] = Vertex(name)

    def get_vertex(self, name):
        """ Returns the vertex of id {name}, or None if {name} can't be found. """
        if name in self.vertices:
            return self.vertices[name]
        else:
            return None

    def add_edge(self, frm, to):
        """ Creates an edge between the nodes {frm} and {to}. """
        self.vertices[frm].add_neighbour(self.vertices[to])

    def print_graph(self):
        """ Prints the graph. """
        for node in self.vert_dict:
            self.vert_dict[node].print_neightbours()        
    
