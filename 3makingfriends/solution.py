# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:31:38 2020

@author: johan
"""


from graph import union,node
import sys
def get_local_data():
    """ Returns the formatted data fetched from local. """
         
    #path = r"C:\Users\johan\Documents\GitHub\EDAF05-labs\3makingfriends\data\sample\1.in"
    path= r"C:\Users\johan\Documents\GitHub\EDAF05-labs\3makingfriends\data\sample\1.in"
    with open(path) as f:
        raw_data= f.read().split("\n")
    info = raw_data[0].split(' ')
    people = int(info[0])
    pairs = int(info[1])
    
    all_data = [[int(i) for i in x.split(' ')] for x in raw_data[1:]]
    #print(all_data)
    all_nodes= []
    for i in range(0,people):                                       #init all nodes as empty sets O(n)
        all_nodes.append(node(id=(i+1))) 
    return all_data,people,pairs,all_nodes 


def get_data():
    """ Returns the formatted data fetched from stdin. """
    raw_data = []                           
    for input in sys.stdin:
        raw_data.append(input.strip())     

    info = raw_data[0].split(' ')
    people = int(info[0])
    pairs = int(info[1])
    
    all_data = [[int(i) for i in x.split(' ')] for x in raw_data[1:]]
    #print(all_data)
    all_data.sort(key=lambda x: x[2])                                                   #sorting the data according to weight
    all_nodes= []
    for i in range(0,people):                                                           #init all nodes as empty sets O(n)
        all_nodes.append(node(id=(i+1))) 
        
    return all_data,people,pairs,all_nodes


def krus(nodes,data):
    big_set = []
    edges = data.copy()
    print(f'Edges going in {edges}')
    while len(edges) !=0:
        current_edge = edges.pop(0)                                                    #taking out the first edge
        start_node = nodes[current_edge[0]-1]                                          #for reference we take out the nodes as well
        end_node = nodes[current_edge[1]-1]
        #print('start_node id :',{start_node.id}, 'and set ',start_node.set)
        #print(f'end_node id:{end_node.id} and set {end_node.set}')
        if not union(start_node,end_node):                                             #if they're not in the same set
            #print(f'Adding edge : {current_edge}')   
            if start_node.setsize < end_node.setsize:                                  #BUG: need to update the sets so the other elements in that set also connects, NEED A POINTER HERE so it keeps track of the slot instead of the value.       
                start_node.merge(end_node)
            else:
                end_node.merge(start_node)
            big_set.append(current_edge)                                                #adding the edge to our final set
        #else do nothing since we don't want this node due to circut
    return big_set

def get_cost(graph):
    total_cost= 0
    for i in graph:                                                                 #Getting the total cost for the optimal graph
        total_cost+=i[2]
    return total_cost



    
        
def main():                                     
    data,people,pairs,nodes = get_data()
    final_graph = krus(data= data,nodes=nodes)
    final_cost = get_cost(final_graph)
    print(f'Final graph {final_graph}')
    print(final_cost)
if __name__== "__main__": main()
     
        
 



"""THIS SECTION CONTAINS NOT USED CODE"""

#%%
"""This is just taken from his psudo code, not used"""
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
        
       