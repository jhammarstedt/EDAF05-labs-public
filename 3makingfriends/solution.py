# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:31:38 2020

@author: johan
"""


import sys
import io
from graph import *

path = r"C:\Users\johan\Documents\GitHub\EDAF05-labs\3makingfriends\data\sample\1.in"
with open(path) as f:
    a= f.read().split("\n")
    print(a)
    
#%%
people = 4                                                      # how many people 
pairs = 4                                                       # how many connections we will do
all_data = [[1,2,1],
        [1,3,7],
        [2,3,4],
        [3,4,5]]       # 


all_data.sort(key=lambda x: x[2])                               #sorting the data according to weight
all_nodes= []
for i in range(0,people):                                       #init all nodes as empty sets O(n)
    all_nodes.append(node(id=(i+1)))

def krus(nodes,data):
    big_set = []
    edges = data.copy()
    while len(edges) !=0:
        current_edge = edges.pop(0)                             #taking out the first edge
        start_node = nodes[current_edge[0]-1]                   #for reference we take out the nodes as well
        end_node = nodes[current_edge[1]-1]
        #print(f'start_node id:{start_node.id} and set {start_node.set}')
        #print(f'end_node id:{end_node.id} and set {end_node.set}')
        if not union(start_node,end_node):                     #if they're not in the same set
            #print(f'Adding edge : {current_edge}')   
            if start_node.setsize < end_node.setsize:                   
                start_node.merge(end_node)
            else:
                end_node.merge(start_node)
            big_set.append(current_edge)                        #adding the edge to our final set
        #else do nothing since we don't want this node due to circut
    return big_set
final_set = krus(all_nodes,all_data)
total_cost = 0
for i in final_set:
    total_cost+=i[2]
print(f'total cost {total_cost}')  
#%%
"""This is just taken from his psudo code"""
def makeunionfind(S):
      
    x=2


def kruskal(G):
    """Psudo implementation of kruskal"""
    T = None
    B = E
    while len(B)!=0:
        #select edge e with minimal weight
        if not  union(B,e):
            #add e to T
            x=2
        #remove e from B
    return T
        
       
        
        
        
    