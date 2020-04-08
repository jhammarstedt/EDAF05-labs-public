class Vertex:
    def __init__ (self,node):
        """Getting the id for the node and a adjacent 
        dict to store it's neighbours"""
        self.id = node
        self.adjacent = []
        self.token = -1
        self.pred = []

    def get_connections(self):
        return self.adjacent

    def print_connections(self):
        connections = [x.id for x in self.adjacent]
        print(self.id,' is connected to ', connections)

    def get_id(self):
        return self.id
    
    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)
        
    def is_visited(self, token):
        return token <= self.token

    def set_visited(self, token):
        self.token = token
    
    def remove_visited(self):
        self.token = -1

    def add_pred(self, node):
        self.pred.append(node)

    def get_level(self):
        return len(self.pred)

    def clear_pred(self):
        self.pred = []

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0


    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to])

    def print_graph(self):
        for node in self.vert_dict:
            self.vert_dict[node].print_connections()        
    
    def get_vertices(self):
        return self.vert_dict.keys()
    
    
