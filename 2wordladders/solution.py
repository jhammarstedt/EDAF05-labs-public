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
        
#%%%
   
    def connect():
      """This function will connect the words where the tail is present in the other node"""
        
      
      #there is still a bug here so matches it twice, but will give you an ide
        
        
        for current_node in list(g.get_vertices()): #O(n^2)
            
            print('current node ',current_node)
            tail = current_node[len(current_node)-4:]
            
            
            for potential_neighbour in set(list(g.get_vertices())).difference(set([current_node])) : #messy way to get all elements in list except the current one
                print('checking for match with: ',potential_neighbour)
                if set(tail) <= set(potential_neighbour): #if the letters of the tail are present in the neighbour, order does not matter
                    print(f'We have a match! Setting an edge from {current_node} to {potential_neighbour} \n')
                    g.add_edge(current_node,potential_neighbour)
     

    g = Graph()
    for word in words: #creating vertexes for all words
        g.add_vertex(word)           
    
    connect() #connecting the matching ones
    g.vert_dict['where'].get_connections() #test output
        
        
    
    
#%%

def BFS():
    print("BFS")


def print_results():
    print("results")

def main():                                     
    get_data()
    create_graph()                    
    BFS() 
    print_results()                   


if __name__== "__main__": main()
