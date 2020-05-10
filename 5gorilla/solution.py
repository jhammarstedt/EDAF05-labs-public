import sys
import pandas as pd
import numpy as np
sys.setrecursionlimit(3500)


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

    row, col = matrix.shape
    print(col) #=s
    print(row) #=t

    word_s = ""
    word_t = ""

    row -= 1
    col -= 1
    index = 0
    while(row and col):
        diag = matrix[row-1][col-1]
        col_plus = matrix[row][col-1]
        row_plus = matrix[row-1][col]
        
        comp = max(diag, col_plus, row_plus)

        if diag == comp:
            word_s += s[len(s)-col-1]
            word_t += t[len(t)-row-1]
            row -= 1
            col -= 1
        elif col_plus == comp:
            word_s += s[len(s)-col-1]
            word_t += '*'
            #row -= 1
            col -= 1
        else:
            word_s += '*'
            word_t += t[len(t)-row-1]
            row -= 1
            #col -= 1
        index += 1

    if row == 0 and col == 0:
        word_s += s[len(s)-col-1]
        word_t += t[len(t)-row-1]

    

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
    print("s:", word_s, "t:", word_t)
    return word_s + " " + word_t

def seq_align(s, t, costs):
    cache = np.zeros((len(s)+1, len(t)+1), dtype="int")

#    def opt(index_s, index_t):
#        delta = -4
#
#        if index_s < 0:
#            return (index_t+1) * delta
#        if index_t < 0:
#            return (index_s+1) * delta
#
#        if cache[index_s][index_t] != 0:
#            return cache[index_s][index_t]
#
#        letter_s = s[index_s]
#        letter_t = t[index_t]
#    
#        cache[index_s, index_t] = max(
#            opt(index_s-1, index_t-1) + costs.loc[letter_s, letter_t], 
#            opt(index_s, index_t-1) + delta,
#            opt(index_s-1, index_t) + delta
#        )
#        return cache[index_s, index_t]
#

#    def opt(index_s, index_t):
#        return 

    def make_table():
        col = 0
        delta = -4
        while col < cache.shape[0]:
            cache[col][0] = col * delta
            row = 0
            while row < cache.shape[1]:
                cache[0][row] = row * delta
                if col and row:
                    diag = cache[col-1][row-1] + costs.loc[s[col-1], t[row-1]]
                    prev_row = cache[col-1][row] + delta
                    prev_col = cache[col][row-1] + delta

                    cache[col][row] = max(diag, prev_row, prev_col)
                row += 1
            col += 1


    #opt(len(s)-1, len(t)-1)
    #words = traceback(s, t, cache)

    make_table()
    print(cache)
    return "hello world"


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    #print_results(results)


if __name__== "__main__": main()

