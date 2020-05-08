import sys
import pandas as pd
import numpy as np

def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    
    letters= raw_data.pop(0).split(' ')
    inputs = [[int(x) for x in i.split(' ')] for i in raw_data[0:len(letters)]]
    strings = raw_data[len(letters)+1].split(' ')
    
    costs = pd.DataFrame(data=inputs,columns=letters,index=letters)
    print(costs)
    return costs, strings


def match_all(costs, strings):
    results = [] 
    for string in strings:
        results.append(seq_align(string[0], string[1]))
    return results


##################################
def opt(i_s, j_t, costs):
    
    #costs.loc[s[i_s],t[j_t]]
    
    delta = -4
    #if i == 0:  j = 0         
    #if j == 0:  i = 0
    if  j_t == 0:
        return i_s*delta
    if i_s == 0:
        return j_t *delta
   
    return min(costs.loc[s[i_s],t[j_t]]+ opt(i-1, j-1),
        delta + opt(i, j-1),
        delta + opt(i-1, j))

def seq_align(s, t):
    global s        #strings
    global t
    
    
        
        
    ## på något sätt, jämför s och t
    
    
 
    return [s, t] #returnera modifierade s och t


###################################


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    #print_results(results)
    #print_results([["AABC", "*ABC"], ["ABA", "ACA"]])
    


if __name__== "__main__": main()

