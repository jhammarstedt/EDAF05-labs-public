import sys
from graph import Graph
from collections import deque

def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())

    metadata = [int(i) for i in raw_data.pop(0).split(' ')]
    nr_nodes = metadata[0]
    nr_edges = metadata[1]
    nr_routes = metadata[3]
    edges = [[int(i) for i in k.split(' ')] for k in raw_data[:nr_edges]]
    remove_list = [int(i) for i in raw_data[nr_routes:]]
    
    return metadata, edges, remove_list



def create_graph(nodes, edge_list):
    graph = Graph()

    # creates every node
    for i in range(nodes):                  
        graph.add_node(name=i)

    graph.select_source(0)
    graph.select_sink(nodes-1)

    # connects every edge
    for index, edge in enumerate(edge_list):
        graph.add_edge(edge_id=index, frm=edge[0], to=edge[1], capacity=edge[2]) 

    return graph



def BFS(graph):
    source_node = graph.get_source()

    queue = deque()
    queue.append(source_node)          
    parent = { source_node.id: None }   
    visited = {}
    while queue:
        v = queue.popleft()
        neighbours = v.get_edges()       
        for edge in neighbours:
            if edge.id not in visited and edge.is_available():
                visited[edge.id] = True
                queue.append(edge.cnode)  
                parent[edge.cnode.id] = { "node": v.id, "edge": edge.id }  
                #print(v.id)
                #print(edge.cnode.is_sink())
                if edge.cnode == graph.get_sink():
                    return parent
    return [] 



def ff_parse_bfs(graph, path):
    sink_id = graph.get_sink().id
    node_id = sink_id
    nodes = []
    edges = []

    while node_id != 0:
        edge_id = path[node_id]["edge"]
        nodes.append(node_id)
        edges.append(edge_id)
        node_id = path[node_id]["node"]
    nodes.append(0)
    return nodes, edges


def ff_find_min_flow(graph, edges):
    min_delta = sys.maxsize
    for edge_id in edges:
        edge = graph.get_edge(edge_id)
        min_delta = min(min_delta, edge.capacity - edge.flow)
    return min_delta


def ff_set_flow(graph, min_delta, edges):
    for edge_id in edges:
        graph.get_edge(edge_id).set_flow(min_delta)

def ff_create_residual_edges(graph, min_delta, nodes):
    edges = []
    for index in range(len(nodes)-1):
        u = index
        v = index + 1
        node = graph.add_edge(edge_id=sys.maxsize, frm=u, to=v, capacity=min_delta)
        edges.append(node)
    return edges

def ff_reset_graph(graph, residual_edges):
    graph.reset_edges()
    for edge in residual_edges:
        edge.disable() 


def ford_fulkerson(graph):
    path = BFS(graph)
    residual_edges = []
    min_flow = 0

    while path:
        nodes, edges = ff_parse_bfs(graph, path)

        min_flow = ff_find_min_flow(graph, edges)
        ff_set_flow(graph, min_flow, edges)
        residual_edges = ff_create_residual_edges(graph, min_flow, nodes)

        path = BFS(graph)

    ff_reset_graph(graph, residual_edges)
    return min_flow 



def remove_edges(graph, remove_list, threshold):
    edges_removed = 0
    max_flow = 0
    remove_edges = True

    while remove_edges:
        flow = ford_fulkerson(graph)

        if flow >= threshold:
            graph.disabled_edge(edges_removed)
            edges_removed += 1
            max_flow = flow
        else:
            remove_edges = False

    return str(edges_removed) + " " + str(max_flow)



def main():
    metadata, edge_list, remove_list = get_data()
    nodes = metadata[0]
    min_students = metadata[2]

    graph = create_graph(nodes, edge_list)
    result = remove_edges(graph, remove_list, min_students)

if __name__=='__main__': main()






def ford_fulkersson(start,stop,graph,token):

    #For each edge in edges set flow to 0, this is done when graph is created
    g_res = Residual_graph()
     #inte helt säker på vad vi ska göra med token här och hur vi ska spara path
     #implementerar den som att vi hade skapat en lista med noder p = [0,1,2] då kan vi gå mellan nod 0-1-2
    flag = True #set starting points
    while flag:
        #path = BFS(start=start,goal=goal,graph=g_res,token=??) 
        while path != "Impossible":
            delta = 10*100
            edges = []
            residual_edges = []
            for current in path[:-1]:                                              # All elements except the final node
                current_edge = graph[nodes][current].edges[path[current+1]]        #current +1 will be the next node, givnig us the correct path
                potential_inc = current_edge.capacity - current_edge.flow
                delta = min(delta,potential_inc)                                   #find the bottleneck
                
                edges.append(current_edge)
                residual_edges.append(g_res[nodes][current].edges[path[current+1]])       
            
            for current in edges:
                edges[current].update_flow(delta)                                   #updating G
                

