class Graph:
    def __init__(self):
        self.nodes = {}
        self.all_edges = {}
        self.source_node = None
        self.sink_node = None

    def add_node(self, name):
        """ Adds a new node to the graph. """
        self.nodes[name] = Node(name)

    def get_node(self, name):
        """ Returns the node of id {name}, or None if {name} can't be found. """
        if name in self.nodes:
            return self.nodes[name]
        else:
            return None

    def print_weights(self):
        for node in self.nodes:
            for edge in self.nodes[node].edges:
                flow = edge.flow
                cap = edge.capacity
                print("node:",node,"to",edge.cnode.id,"edge_id",edge.id,"flow:",flow,"cap:",cap)


    def add_edge(self, edge_id, frm, to, capacity):
        """ Creates an edge between the nodes {frm} and {to}. """
        new_edge = self.nodes[frm].add_edge(edge_id=edge_id, to_node=self.nodes[to], capacity=capacity)
        self.all_edges[edge_id] = new_edge
        return new_edge

    def get_edge_by_node(self,frm,to):
        """Get edge from node to another"""
        #print("from:",frm,"nodes:",self.nodes.edge_map)
        return self.nodes[frm].edge_map[to]

    def get_edge_by_id(self, edge_id):
        return self.all_edges[edge_id]

    def print_graph(self):
        """ Prints the graph. """
        for node in self.nodes:
            self.nodes[node].print_edges()        

    def select_source(self, node_id):
        self.source_node = self.nodes[node_id]

    def get_source(self):
        return self.source_node

    def select_sink(self, node_id):
        self.sink_node = self.nodes[node_id]

    def get_sink(self):
        return self.sink_node

    def disable_edge(self, edge_id):
        self.all_edges[edge_id].disable()

    def enable_edge(self, edge_id):
        self.all_edges[edge_id].enable()

    def reset_edges(self):
        for edge_id in self.all_edges:
            self.all_edges[edge_id].set_flow(0)
    
    def get_edge_count(self):
        return len(self.all_edges)

class Node:
    def __init__ (self,node):
        self.id = node
        self.edges = [] 
        self.edge_map = {}

    def get_edges(self):           
        """ Returns every neighbour of the node. """
        return self.edges

    def print_edges(self):
        """ Prints every neighbour of the node. """
        neigh = [edge.cnode.id for edge in self.edges]
        #neigh = [[self.edges[neighbour].cnode.id, self.edges[neighbour].capacity] for neighbour in self.edges.keys()]
        print(self.id, 'is connected to', neigh)

    def add_edge(self, edge_id, to_node, capacity):
        """ Connects a neighbour to the node with an edge. """ 
        new_edge = Edge(edge_id=edge_id, to_node=to_node,capacity=capacity)
        self.edge_map[to_node.id] = new_edge
        self.edges.append(new_edge)
        return new_edge

    #def is_visited(self, token):
    #    """ Checks if token has been used for visiting the node. """
    #    return token <= self.token

    #def set_visited(self, token):
    #    """ Sets a new visit token. """
    #    self.token = token
    

class Edge:
    """Edges are connected through nodes and accessed from each nodes by a dict of edges"""
    def __init__(self, edge_id, to_node, capacity):
        self.id = edge_id
        self.capacity = capacity             
        self.flow = 0                   #e
        self.cnode= to_node             #the other node which it is connected to 
        self.cache = capacity
   
    def disable(self):
        self.capacity = 0

    def enable(self):
        self.capacity = self.cache

    def get_capacity(self):
        return self.capacity

    def set_flow(self, new_flow):
        self.flow = new_flow

    def add_flow(self, new_flow):
        self.flow += new_flow

    def get_flow(self):
        return self.flow
    
    def is_available(self):
        return self.capacity - self.flow

