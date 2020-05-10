import sys
import pandas as pd
import numpy as np


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
    print("col:",s)
    print("row:",t)
    print(matrix)
#    row, col = matrix.shape
#    word1 = ""
#    word2 = ""
#    row -=1
#    col -=1
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
#    print(word2)
#
#    
#    if row == 0:
#        word1 = col*'*'+word1
#    if col == 0:
#        word2 = col*'*'+word2
#
#
#    print("word1:",word1 + " " + "word2:",word2)

    return s + " " + t

def seq_align(s, t, costs):
    cache = np.zeros((len(s), len(t)))

    def opt(index_s, index_t):
        delta = -4
        if cache[index_s][index_t] != 0:
            return cache[index_s][index_t]

        if index_s < 0:
            return (index_t+1) * delta
        if index_t < 0:
            return (index_s+1) * delta
       
        letter_s = s[index_s]
        letter_t = t[index_t]
    
        cache[index_s, index_t] = max(
            opt(index_s-1, index_t-1) + costs.loc[letter_s, letter_t], 
            opt(index_s, index_t-1) + delta,
            opt(index_s-1, index_t) + delta
        )
        return cache[index_s, index_t]

    opt(len(s)-1, len(t)-1)
    words = traceback(s, t, cache)

    return words


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    #print_results(results)


if __name__== "__main__": main()

