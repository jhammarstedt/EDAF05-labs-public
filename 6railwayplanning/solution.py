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
    remove_list = [int(i) for i in raw_data[nr_edges:]]
    
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
        i = index+1
        graph.add_edge(edge_id=i, frm=edge[0], to=edge[1], capacity=edge[2]) 
        graph.add_edge(edge_id=-i, frm=edge[1], to=edge[0], capacity=edge[2]) 
    return graph



def BFS(graph):
    source_node = graph.get_source()

    queue = deque()
    queue.append(source_node)          
    parent = {}   
    visited = {}

    while queue:
        v = queue.popleft()
        neighbours = v.get_edges()       
        for edge in neighbours:
            if edge.cnode.id not in visited and edge.is_available():
                visited[edge.cnode.id] = True
                queue.append(edge.cnode)  
                parent[edge.cnode.id] = { "node": v.id, "edge": edge.id }  
                if edge.cnode == graph.get_sink():
                    return parent
    return [] 



def ff_parse_bfs(graph, path):
    sink_id = graph.get_sink().id
    source_id = graph.get_source().id
    node_id = sink_id
    nodes = []
    edges = []
    while node_id != source_id:
        edge_id = path[node_id]["edge"]
        nodes.append(node_id)
        edges.append(edge_id)
        node_id = path[node_id]["node"] 
    nodes.append(0)
    return nodes, edges


def ff_find_min_flow(graph, edges):
    min_delta = sys.maxsize
    for edge_id in edges:
        edge = graph.get_edge_by_id(edge_id)
        min_delta = min(min_delta, edge.is_available())
    return min_delta


def ff_set_flow(graph, min_delta, edges, nodes):
    # forward edge
    for edge_id in edges:
        graph.get_edge_by_id(edge_id).add_flow(min_delta)

    # back edge
    node_index = graph.get_edge_count()
    for index in range(len(nodes)-1):
        u = nodes[index] 
        v = nodes[index + 1]
        edge = graph.get_edge_by_node(u,v)
        edge.add_flow(-min_delta)



def ford_fulkerson(graph):
    path = BFS(graph)
    min_flow = 0
    delta = 0
    while path:
        nodes, edges = ff_parse_bfs(graph, path)

        min_flow = ff_find_min_flow(graph, edges)
        ff_set_flow(graph, min_flow, edges, nodes)
        delta += min_flow
        
        path = BFS(graph)
    graph.reset_edges()
    return delta 



def remove_edges(graph, remove_list, threshold):
    edges_removed = 0
    flow = threshold
    max_flow = 0
    first_list = remove_list
    second_list = remove_list

    while first_list and second_list:
        flow = ford_fulkerson(graph)
        if flow >= threshold:
            max_flow = flow
            half = len(second_list) // 2
            first_list = second_list[:half]
            second_list = second_list[half:]
            for index in first_list:
                graph.disable_edge(index+1)
                graph.disable_edge(-(index+1))
            edges_removed += len(first_list)
        
        else:
            half = len(first_list) // 2
            second_list = first_list[half:]
            first_list = first_list[:half]
            for index in second_list:
                graph.enable_edge(index+1)
                graph.enable_edge(-(index+1))
            edges_removed -= len(second_list)
        
    return str(edges_removed) + " " + str(max_flow)



def main():
    metadata, edge_list, remove_list = get_data()
    nodes = metadata[0]
    min_students = metadata[2]

    graph = create_graph(nodes, edge_list)
    result = remove_edges(graph, remove_list, min_students)
    print(result)

if __name__=='__main__': main()

