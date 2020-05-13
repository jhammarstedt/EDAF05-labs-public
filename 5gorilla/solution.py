import sys
#import pandas as pd
#import numpy as np
sys.setrecursionlimit(3500)


def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    
    letters= raw_data.pop(0).split(' ')
    inputs = [[int(x) for x in i.split(' ')] for i in raw_data[0:len(letters)]] #O(alf^2) :afl = words in alfab

    strings = raw_data[len(letters)+1:] 
    strings = [i.split(' ') for i in strings]   

    #costs = pd.DataFrame(data=inputs,columns=letters,index=letters)
    
    costs = {letter: {letter:0 for letter in letters } for letter in letters}
    for letter1,numbers in zip(costs.keys(),inputs):
        for letter2,number2 in zip(costs[letter1].keys(),numbers) :
            costs[letter1][letter2]= number2
    
    #costs = costs.to_dict()
    #print(costs)
    return costs, strings


def match_all(costs, strings):
    results = [] 
    for string in strings:
        results.append(seq_align(string[0], string[1],costs))

    return results


##################################

def traceback(s, t, matrix,costs):
    row = len(s)
    col = len(t) 
    delta = -4
    
    word_s = word_t = " "

    move_diag = 1
    move_col = move_row = 0
    while row and col:
        #print("row:",row,"col:",col)
        #if row < 1:
        #    move_row = move
        #    move_col = not move
            #return word_s + " " + '*'*(col-1) + word_t

        #if col <= 0:
            #return '*'*(row-1) + word_s + " " + word_t
        #    move_row = not move
        #    move_col = move
        #print(s[-1])
#        letter_s = s[row-1]
 #       letter_t = t[col-1]
        #print("s",letter_s,"t",letter_t)

        move = max(move_diag, move_col, move_row)

        if 1 != 1:
            print("hello")

        elif move_col == move:
            #row -= 1
            #word_t = letter_t + word_t
            word_t = t[col-1] + word_t
            word_s = '*' + word_s # C
            col -= 1

        elif move_diag == move: 
            word_s = s[row-1] + word_s  # swap
            word_t = t[col-1] + word_t
            row -= 1
            col -= 1
    #    print(word_s," ",word_t)

        elif move_row == move:
            word_t = '*' + word_t
            #word_s = letter_s + word_s
            word_s = s[row-1] + word_s
            row -= 1
            #col -= 1
        else:
            print("hello")
        
        if not col or not row:
            move_diag = -10
        else:
            move_diag = matrix[row-1][col-1] + costs[s[row-1]][t[col-1]]#costs.loc[letter_s, letter_t]
        move_col = matrix[row][col-1] + delta
        move_row = matrix[row-1][col] + delta

    if row and not col:
    
        word_s = s[row] + word_s
        word_t = '*'+ word_t
        #print("row")
    if col and not row:
#    while row >= 0 and col >= 0:
        word_t = t[col] + word_t
        word_s = '*'+ word_s
#        if row == 0 and col ==0:
#            break
#        #print("row:",row,"col:",col)
#        letter_s = s[row-1]
#        letter_t = t[col-1]
#        #print("row:",row,"letter_s:",letter_s)
#        #print("col:",col,"letter_t:",letter_t)
#        if row > 1 and col > 1:
#            move_diag = matrix[row-1][col-1] + costs[letter_s][letter_t]#costs.loc[letter_s, letter_t]
#        else:
#            move_diag = -10
#        move_col = matrix[row][col-1] + delta
#        move_row = matrix[row-1][col] + delta
#
#        
#

    return word_s + " " + word_t

def seq_align(s, t, costs):
    #cache = np.zeros((len(s)+1, len(t)+1), dtype="int")
    cache = [[0 for i in range(0,len(t)+1)] for k in range(0,len(s)+1)]
    def make_table():
        col = 0
        delta = -4
        while col < len(cache): #cache.shape[0]:
            cache[col][0] = col * delta
            row = 0
            while row < len(cache[0]): #cache.shape[1]:
                cache[0][row] = row * delta
                if col and row:
                    diag = cache[col-1][row-1] + costs[s[col-1]][t[row-1]]
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

