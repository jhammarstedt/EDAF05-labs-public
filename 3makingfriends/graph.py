# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:00:31 2020

@author: johan
"""

def MakeUnionFind(S):
    class node:
        def __init__(self):
            self.point = None           #Points towards the set it's in, initialized to it's own
            


class Graph:
    def __init__(self,nodes):
        self.nodes= nodes                #Vertices
        self.components = []             #default dict to store graph
        
    
    def addEdge(self,u,v,weight):
        """Add an edge to graph"""
        self.graph.append([u,v,weight])
    
    def find(self,parent,v):
        """Find the canonical member of the set which v belongs to"""
        p = v
        while len(parent[p])!= 0:
            temp = parent[v]
            parent[v] = p
            v = temp
        return p
    
    def union(self,u,v):
        """Merge the two sets p_i and p_j represented by u and v into a new set p_k represented by u,
        and destroy p_i and p_j"""
        u_root = self.find(u)
        v_root = self.find(v)
        if len(u_root) < len(v_root): #this is probably wrong, should maybe be rank
            parent[u_root] = v_root
            #size(v) = size(u)+size(v)
            
        else:
            parent[v_root]=u_root
            #size(u)=size(u)+size(v)
     
