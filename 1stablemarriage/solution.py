# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:22:05 2020

@author: johan
"""

"""
Implement algo 
debugg code
structure code in logical fashion
Parsing messy input
Reason about correctness of algo
reason about upper bounds for time complexity


You are given each man’s and woman’s preference lists. 
Given these lists ﬁnd a stable matching, meaning that there do not exist two 
man-woman-pairs (m1,w1),(m2,w2) such that w2 is higher ranked on m1’s preference 
list than w1 and simultaneously m1 is higher ranked on w2’s preference list than m2 
(thus that both m1 and w2 would prefer to change partner).


Input:
python3 solution_ﬁle < input_ﬁle 

    First line:
        - single int N from 1-3000, number of men and women
        - Preference list:
            total: (N+1)* 2N
    Then:       
        Structured in 2N chunks of N+1 int each:
            first: Index of the person i (int)
            2nd: N (distinct int) preference list of i 
    
    EX:
        2
        1 1 2
        2 2 1
        1 1 2
        2 2 1
    
    first two rows are for man 1 and 2, then comes women 1 and 2

output:
    N rows with one int each:
        index of man paired with woman i
    
    So for:
        input:
            2
            1 1 2
            2 2 1
            1 1 2
            2 2 1
    
        output:
            1  (woman 1 was paired with man 1)
            2  (woman 2 was paried with man 2)
                
"""
import sys
#%%
def later():
    #Fix the input and sorting :
        
    def test():
        
        
        inp_file = sys.argv[1]
        with open(inp_file) as f: 
            lines = f.read().strip().split('\n')
            print(lines)
        
        N = int(lines[0])
    
    
    def x():
        inp_file = r"C:\Users\johan\Documents\GitHub\EDAF05-labs\1stablemarriage\data\sample\1.in"
        m =[]
        w=[]
        with open(inp_file) as f:
            lines = f.read().strip().split('\n')
            #print(lines)
        
        N = lines.pop(0)
        x = [] #empty list to separate all lines
        for i in lines:
            x.append(i.split())
        #M = {1:[1,2],2:[2,1]}
        #W = [[1,1,2],[2,2,1]]
            
    W= {1:{'pref':[2,1], #man 1 at index 1, man 2 at index 2
           'pair':None
           },
        2:{'pref':[1,2], #man 2 at index 1
           'pair':None}}
    
    M = [[1,1,2],[2,2,1]]
#%%
#Here's the code for now with a 4x4 preference list

N=4
def create_W(l1,l2,l3,l4):
    W= {1:{'pref':l1, #man 1 at index 1, man 2 at index 2
           'pair':None
           },
        2:{'pref':l2, #man 2 at index 1
           'pair':None},
        3:{'pref':l3,
           'pair':None},
        4:{'pref':l4,
           'pair':None}}
    return W
        
L1= [4,2,1,3]
L2= [2,1,3,4]
L3=[4,1,2,3]
L4= [1,4,2,3]

W = create_W(L1,L2,L3,L4)


M = [[1,3,4,2,1],
     [2,3,4,1,2],
     [3,1,4,2,3],
     [4,2,1,4,3]]

p=M.copy()


#add a check to see who has proposed to who
proposals = [0 for i in range(0,int(N))]

def get_top_woman(man):
    """
    Function that takes in the man and his preference list, and also the
    proposals list which contains the index of which woman currently can propose too
    """
    global proposals #Since we want to modify the global list inside our function
    
    #separate the man and his preference list
    current_man = man[0]-1 #get index of current man  
    preference_list = man[1:]
    
    #get the index of his preference list which he has yet to propose to
    current_top_pick = proposals[current_man] 
    
    #get the top available woman
    propose_to = preference_list[current_top_pick]
    
    proposals[current_man]+=1 #Cross that position of his list
    
    return propose_to
    
   
while len(p)!= 0:

    m = p.pop(0)
    
    w_index = get_top_woman(m) #get the top woman in his list
    
    w = W[w_index]
    
    if w['pair']==None:
        w['pair']=m  #pair woman up with man 
    
    #check if the position of the current man is worse than this man
    elif w['pref'][w['pair'][0]-1]> w['pref'][m[0]-1]:
        p.append(w['pair']) #put the less prefered man back 
        w['pair'] = m #create a new pair
    
    else:
        #print(m)
        p.append(m) #add this man back to the p list
       
#Produce output   
for i in W.keys():
    print(W[i]['pair'][0])
