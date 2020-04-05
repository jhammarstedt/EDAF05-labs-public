import sys

def get_data():
    raw_data = []                           
    for input in sys.stdin:
        for element in input.strip().split(" "):
            raw_data.append(int(element))       # O(n^2) - input as sequential array (to handle messy inputs)
                                                #          naive solution would still require O(n^2) for validity check    
    N = raw_data[0]                             # first element == N
    data = raw_data[1:]                         # p-list data

    women = [None] * (N+1)                      # empty woman array of size N (+ blank 0-index)
    men = [None] * (N+1)                        # empty men array of size N (+ blank 0-index)

    for i in range(N*2):                        # O(n) - for every N*2 person... 
        id = data[(N+1)*i]                      # id @ every (N+1)*i position
        pref_list = data[(N+1)*i+1:(N+1)*(i+1)]        
                                                # pref_list between every id 

        if women[id] == None:                   # 1st appearance => woman
            rank = pref_to_rank(pref_list, N)   # convert preference list to ranked list
            women[id] = rank                 
        elif men[id] == None:                   # 2nd appearence => man
            men[id] = pref_list 
        else:                                   # 3rd appearance => error 
            print("Error in input file!")

    return women, men

def pref_to_rank(list, N):                      
    rank = 1                                    # rank 1 = best rank
    ranking = [0] * (N+1)                       
    for e in list:                              
        ranking[e] = rank                       # set element e to rank 
        rank += 1                               # increment rank variable
    return ranking


def GS(w, m):
    mingle = range(1, len(m))                   # list of available men
    couples = [None] * (len(w))                 # list of man + woman combinations (currently empty)
    
    while len(mingle):                          # while still more proposals
        man = mingle.pop(0)                     # take out first man from mingle
        woman = m[man].pop(0)                   # the woman man prefers the most
                                                #         & man has not yet proposed to
        if couples[woman] == None:              # woman has no partner
            couples[woman] = man                # couple (man, woman) made
        elif w[woman][man] < w[woman][couples[woman]]: # woman perfers man over previous_man
            previous_man = couples[woman] 
            couples[woman] = man                # replace womans previous man
            mingle.append(previous_man)         # previous man back in mingle
        else:                                
            mingle.append(man)                  # put man back in mingle
    
    return couples


def print_results(c):
    for couple in c: 
        if couple: print(couple)

def main():                                     # O(2n^2 + n) == O(n^2)
    women, men = get_data()                     # O(n^2) - get data from standard input 
    couples = GS(women, men)                    # O(n^2) - match men and women
    print_results(couples)                      # O(n) - print results


if __name__== "__main__": main()
