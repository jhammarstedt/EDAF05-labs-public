# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 21:00:31 2020

@author: johan
"""
def union(node1,node2):             #check if they are in the same set
    if (node1.set == node2.set):    #If both None they are not in the same set
        return True
    else: 
        return False

class node:
    def __init__(self,id):
        self.point = None       #The edge it's connected too -- Not used now, do we need it?      
        self.set = id           #The set it points towards, first to itself, the set is the id of a node in that set
        self.setsize = 1        #The size of the set
        self.id = id            #Just for own reference
 
        
    def merge(self,node2):
        self.set = node2.set    # Merge this node into the other nodes set
        node2.setsize +=1       # increment the setsize


    def addEdge(self,node2):    #not used, needed?
        self.point = node2      # make it point towards the new node

















        
#%%        
"""also from his psudo, not used"""      
class sets:
    def __init__(self,nodes):
        self.nodes= nodes                #Vertices
        #self.components = []             #default dict to store graph
        #self.set = None                 #The set in which the node is connected to
    
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
     
