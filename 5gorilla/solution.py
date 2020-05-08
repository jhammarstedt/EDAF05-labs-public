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


def main():              
    costs, strings = get_data()
    


if __name__== "__main__": main()

