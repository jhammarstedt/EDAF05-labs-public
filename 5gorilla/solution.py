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

def traceback(s, t, matrix,costs):
    row = matrix.shape[0] -1
    col = matrix.shape[1] -1
    delta = -4
    word_s = ""
    word_t = ""
    #print(matrix)
    while row >= 0 and col >= 0:
        if row == 0 and col ==0:
            break
        #print("row:",row,"col:",col)
        letter_s = s[row-1]
        letter_t = t[col-1]

        move_diag = matrix[row][col] + costs.loc[letter_s, letter_t]
        move_col = matrix[row][col-1] + delta
        move_row = matrix[row-1][col] + delta

        move = max(move_diag, move_col, move_row)

        if move_diag == move:
            row -= 1
            col -= 1
            word_s = letter_s + word_s
            word_t = letter_t + word_t
        elif move_col == move:
            #row -= 1
            col -= 1
            word_t = letter_t + word_t
            word_s = '*' + word_s
        else:
            row -= 1
            word_t = '*' + word_t
            word_s = letter_s + word_s
            #col -= 1

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


    make_table()
    words = traceback(s, t, cache,costs)
    return words


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    print_results(results)

if __name__== "__main__": main()

