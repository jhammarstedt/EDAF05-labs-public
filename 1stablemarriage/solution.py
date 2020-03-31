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

#Todo:
# 1 mangage input from system arguments
# 2 Clean all messy input and sort
# 3 Convert the preference list of women to be inversed

#%%
def fix_messy(lists):
    x=2 #fix here


def get_data(folder,name):
    inp_file = fr"C:\Users\johan\Documents\GitHub\EDAF05-labs\1stablemarriage\data\{folder}\{name}"
    with open(inp_file) as f:
        lines = f.read().strip().split('\n')
   
    #take out N
    couples = lines.pop(0)  
    
    #fix the data so we get separate inner lists consiting of ints
    lines = [i.split() for i in lines] 
    lines = [list(map(int,i)) for i in lines]
    
        
    men = []
    man_count =1 #To sort out all the males
    reset = 0 #add a counter that will increment if our list is not sorted
    
    #All prints in here are used for debugging, will be removed
    
    
    while man_count <= int(couples): #check the list until we have all males
        if int(lines[reset][0]) == man_count:
            if man_count=='bug':
                print('Index of man: ',lines[reset][0])
                print('man index matches with count')
                print('Current lines',lines)
            men.append(lines.pop(reset))
            if man_count=='bug':
                print('man is now: ',men)
                print('after pop: ',lines)
            
            man_count+=1
            if man_count=='bug':
                print('man count: ',man_count,'\n')
            reset=0
        else:
            reset+=1 #if 
            #print('No match, reset at ', reset,'\n')
               
    women =lines 
    
    
    return men,women,couples,lines
    
M,unsorted_women,N,lines = get_data('secret','4testhuge.in')


def create(list_of_women,N):
    Wom = {woman[0]: {'pref':woman[1:N+1],'pair':None} for woman in list_of_women}
    return Wom
    
W = create(unsorted_women,int(N))

#%%
N= len(M)

mingle=M.copy() # the list which will represent men who have not found a stable match 


#The proposals list contains the index of which order on the 
# preference list man i can propose to. So if proposals[0]=1 the man will propose to his 2nd choice
proposals = [0 for i in range(0,int(N))]

def get_top_woman(man):
    """
    Function that takes in man i and his preferences. Then uses the proposals list to 
    get the top woman on his list which he has not proposed to already.       
    
    """
    global proposals #Since we want to modify the global list inside our function
    
    #separate the man and his preference list
    current_man = man[0]-1 #get index of current man  
    preference_list = man[1:]
    
    #get the index of his preference list which he has yet to propose to
    current_top_pick = proposals[current_man] 
    
    #get the top available woman
    propose_to = preference_list[current_top_pick]
    
    proposals[current_man]+=1 #'Cross' that position of his list
    
    return propose_to
    
   
while len(mingle)!= 0:

    m = mingle.pop(0)
    
    w_index = get_top_woman(m) #get the top woman in his list
    
    w = W[w_index]
    
    if w['pair']==None: #if woman is free
        w['pair']=m  #pair woman up with man 
    
    #check if the position of the current man is worse than this man
    elif w['pref'][w['pair'][0]-1]> w['pref'][m[0]-1]:
        mingle.append(w['pair']) #put the less prefered man back 
        w['pair'] = m #create a new pair
    
    else:
        #print(m)
        mingle.append(m) #add this man back to the p list
       
#Produce output   
for i in W.keys():
    print(W[i]['pair'][0])



#%%
#TEST case   

def create_W(l1,l2,l3,l4):
    W= {1:{'pref':l1, 
           'pair':None
           },
        2:{'pref':l2,
           'pair':None},
        3:{'pref':l3,
           'pair':None},
        4:{'pref':l4,
           'pair':None}}
    return W

L1= [4,2,1,3] #list represents the order that they prefer, so man 1 is 4th here
L2= [2,1,3,4]
L3=[4,1,2,3]
L4= [1,4,2,3]

W = create_W(L1,L2,L3,L4)


M = [[1,3,4,2,1],
     [2,3,4,1,2],
     [3,1,4,2,3],
     [4,2,1,4,3]]

#%%