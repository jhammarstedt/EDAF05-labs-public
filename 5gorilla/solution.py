import sys

def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    
    letters= raw_data.pop(0).split(' ')
    inputs = [[int(x) for x in i.split(' ')] for i in raw_data[0:len(letters)]] #O(alf^2) :afl = words in alfab

    strings = raw_data[len(letters)+1:] 
    strings = [i.split(' ') for i in strings]   

    costs = {letter: {letter:0 for letter in letters } for letter in letters}
    for letter1,numbers in zip(costs.keys(),inputs):
        for letter2,number2 in zip(costs[letter1].keys(),numbers):
            costs[letter1][letter2]= number2
    
    return costs, strings



def match_all(costs, strings):
    results = [] 
    for string in strings:
        results.append(seq_align(string[0], string[1],costs))

    return results



def seq_align(s, t, costs):
    cache = [([0] * (len(t)+1)) for k in range(len(s)+1)]

    def make_table():
        col = 0
        delta = -4
        while col < len(cache): 
            cache[col][0] = col * delta
            row = 0
            while row < len(cache[0]): 
                cache[0][row] = row * delta
                if col and row:
                    diag = cache[col-1][row-1] + costs[s[col-1]][t[row-1]]
                    prev_row = cache[col-1][row] + delta
                    prev_col = cache[col][row-1] + delta

                    cache[col][row] = max(diag, prev_row, prev_col)
                row += 1
            col += 1
    

    def traceback():
        row = len(s)
        col = len(t) 
        delta = -4
        word_s = word_t = ""
    
        move_diag = 1
        move_col = move_row = 0
        while row and col:
            move = max(move_diag, move_col, move_row)
            if move_diag == move: 
                word_s = s[row-1] + word_s
                word_t = t[col-1] + word_t
                row -= 1
                col -= 1
            elif move_row == move:
                word_s = s[row-1] + word_s
                word_t = '*' + word_t
                row -= 1
            elif move_col == move:
                word_s = '*' + word_s
                word_t = t[col-1] + word_t
                col -= 1
            
            move_diag = cache[row-1][col-1] + costs[s[row-1]][t[col-1]]
            move_row = cache[row-1][col] + delta
            move_col = cache[row][col-1] + delta
    
        if row and not col:
            while row:
                word_s = s[row-1] + word_s
                word_t = '*'+ word_t
                row -= 1
        if col and not row:
            while col:
                word_s = '*'+ word_s
                word_t = t[col-1] + word_t
                col -= 1
    
        return word_s + " " + word_t

    make_table()
    return traceback()


def print_results(results):
    for result in results:
        print(result)

def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    print_results(results)

if __name__== "__main__": main()

