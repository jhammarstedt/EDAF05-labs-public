import sys
import pandas as pd
import numpy as np
#sys.setrecursionlimit(10000)



def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    
    letters= raw_data.pop(0).split(' ')
    inputs = [[int(x) for x in i.split(' ')] for i in raw_data[0:len(letters)]]

    strings = raw_data[len(letters)+1:] 
    strings = [i.split(' ') for i in strings]
    costs = pd.DataFrame(data=inputs,columns=letters,index=letters)
    
    return costs, strings


def match_all(costs, strings):
    results = [] 
    for string in strings:
        results.append(seq_align(string[0], string[1],costs))

    return results


##################################

def traceback(s, t, matrix):
    row, col = matrix.shape
    word1 = ""
    word2 = ""
    row -=1
    col -=1
    print(matrix) 
#    while(row and col):
#        #swap = matrix[row][col]
#        #missing_s = matrix[row][col-1]
#        #missing_t = matrix[row-1][col]
#        swap = matrix[row][col]
#        missing_s = matrix[row][col-1]
#        missing_t = matrix[row-1][col]
#     
#        temp = max(swap, missing_s, missing_t)
#        print(temp)
#        if swap == temp: 
#            #word1 = s[row] + word1
#            #word2 =t[col] + word2
#            row -= 1
#            col -= 1
#        elif missing_s == temp:
#            #word1 = "*" + word1
#            #word2 = t[col] + word2
#            col -= 1
#        else:
#            #word1= s[row] + word1
#            #word2='*' + word2
#            row -= 1
#    
#    print(word1)
    print(word2)

    
    if row == 0:
        word1 = col*'*'+word1
    if col == 0:
        word2 = col*'*'+word2


    print("word1:",word1 + " " + "word2:",word2)

    return word1 + " " + word2

def seq_align(s, t, costs):
    #print(word1)
    #print(word2)
#    global s
#    s = word1        #strings
#    global t 
#    t = word2
#    global costs
#    costs = icosts
#
#
    cache = np.zeros((len(s), len(t)))
    

    def opt(index_s, index_t):#, word1, word2):
        delta = -4
        if cache[index_s][index_t] != 0:
            return cache[index_s][index_t]

        #if index_s == 0 and index_t == 0:
        #    return 0, word1 + " " + word2
        if index_s < 0:
            return (index_t+1) * delta#, "*"*index_t + word1 + " " + t[index_t-1] + word2
        if index_t < 0:
            return (index_s+1) * delta#, s[index_s-1] + word1 + " " + "*"*index_s + word2
       
        letter_s = s[index_s]
        letter_t = t[index_t]
    
        #cost_1, word_1 = opt(index_s-1, index_t-1, letter_s + word1, letter_t+word2)
        #cost_2, word_2 = opt(index_s, index_t-1, '*'+word1, letter_t+ word2)
        #cost_3, word_3 = opt(index_s-1, index_t, letter_s+word1, '*'+word2)
        
        #cost_1 += costs.loc[letter_s, letter_t]
        #cost_2 += delta
        #cost_3 += delta
    
        #cache[index_s][index_t] = max(cost_1, cost_2, cost_3)
    
        #if cache[index_s][index_t] == cost_1: return cache[index_s][index_t], word_1
        #if cache[index_s][index_t] == cost_2: return cache[index_s][index_t], word_2
        #if cache[index_s][index_t] == cost_3: return cache[index_s][index_t], word_3
        cache[index_s, index_t] = max(costs.loc[letter_s, letter_t] + opt(index_s-1, index_t-1),
                delta + opt(index_s, index_t-1),
                delta + opt(index_s-1, index_t))
        return cache[index_s, index_t]


    opt(len(s)-1, len(t)-1) #, "", "")[1]
    return traceback(s, t, cache)


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    #print(strings)
    results = match_all(costs, strings)
    #print_results(results)
    #print_results(["AABC *ABC", "ABA ACA"])
    


if __name__== "__main__": main()

