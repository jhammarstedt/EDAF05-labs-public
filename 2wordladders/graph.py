class Vertex:
    def __init__ (self,node):
        """Getting the id for the node and a adjacent 
        dict to store it's neighbours"""
        self.id = node
        self.adjacent = []
        self.visited = False

    def get_connections(self):
        return self.adjacent

    def print_connections(self):
        connections = [x.id for x in self.adjacent]
        print(self.id,' is connected to ', connections)

    def get_id(self):
        return self.id
    
    def add_neighbor(self, neighbor):
        self.adjacent.append(neighbor)
        
    def is_visited(self):
        return self.visited

    def set_visited(self):
        self.visited = True
    
    def remove_visited(self):
        self.visited = False

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

    def get_vertices(self):
        return self.vert_dict.keys()
    
    
