class Graph:
    def __init__(self, size):
        self.edge_roots = [0] * (size + 2)                  # empty int[] to store roots


    def find(self, node):
        if self.edge_roots[node] == 0:                      # if node not in edge_roots...
            self.edge_roots[node] = node                    # ...node is it's own root

        root = self.edge_roots[node]                        

        if root == node:                                    
            return node                                     # stop resursive search when root == node

        self.edge_roots[node] = self.find(root)             # [RECURSIVE] node.root <- root.root
        return self.edge_roots[node]

    
    def union(self, edge):
        u = min(edge[0], edge[1])                           # node u of edge (u, v)
        v = max(edge[0], edge[1])                           # node v of edge (u, v)

        if self.edge_roots[v] != 0:                         # if v is already in graph, and already has a root...
            self.edge_roots[self.find(v)] = self.find(u)    # ...set that root to the root of u
        else:
            self.edge_roots[v] = self.find(u)               # ...otherwise v.root <- u.root


