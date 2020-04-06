import sys

def get_data():
    print("get_data")
   
#%% 
N = 5
Q = 3
words = ['there','where','input','putin','hello']
queeries = [['there','where'],
            ['putin','input'],
            ['hello','putin']]   

def create_graph():
    class Vertex:
        def __init__ (self,node):
            """Getting the id for the node and a adjacent 
            dict to store it's neighbours"""
            self.id = node
            self.adjacent = []
        
        def get_connections(self):
            """display node connections"""
            connections = [x.id for x in self.adjacent]
            print(f'{self.id} is connected to {connections}')
            return self.adjacent
        def get_id(self):
            return self.id
        
        def add_neighbor(self, neighbor):
            self.adjacent.append(neighbor)
            
    
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
    
        def add_edge(self, frm, to, cost = 0):
            if frm not in self.vert_dict:
                self.add_vertex(frm)
            if to not in self.vert_dict:
                self.add_vertex(to)
    
            self.vert_dict[frm].add_neighbor(self.vert_dict[to])
            self.vert_dict[to].add_neighbor(self.vert_dict[frm])
    
        def get_vertices(self):
            return self.vert_dict.keys()
    
    #Testing to build some connections
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_edge('a', 'b') 
    g.vert_dict['a'].get_connections()
#%%

def BFS():
    print("BFS")


def print_results():
    print("results")

def main():                                     
    get_data()                    
    BFS() 
    print_results()                   


if __name__== "__main__": main()
