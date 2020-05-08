import sys
import numpy as np
import pandas as pd

def get_data():
    raw_data = []                           
    for input in sys.stdin:
        # append every input line to raw_data
        raw_data.append(input.strip())                                      


    
    # costs som dataframe, strings som array [ord1, ord2]
    return costs, strings



def match_all(costs, strings):
    results = []
    for string in strings:
        results = seq_align(string[0], string[1])
    return results


##################################


def seq_align(s, t):
    ## på något sätt, jämför s och t
    return [s, t] #returnera modifierade s och t


    def opt(i, j, costs):
        #if i == 0:  j = 0         
        #if j == 0:  i = 0        
        delta = -4

        min(costs(x_i,y_i) + opt(i-1, j-1),
        delta + opt(i, j-1),
        delta + opt(i-1, j))
        return min() #kostnad för alla alternativ



###################################


def print_results(results):
    for result in results:
        print(result)


def main():              
    costs, strings = get_data()
    results = match_all(costs, strings)
    print_results(results)


if __name__== "__main__": main()

