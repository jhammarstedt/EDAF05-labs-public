import sys
#import pandas as pd
#import numpy as np
def get_data():
    raw_data=[]
    
    for input in sys.stdin:
        raw_data.append(input.strip())
    
    letters= raw_data.pop(0).split(' ')
    inputs = [[int(x) for x in i.split(' ')] for i in raw_data[0:len(letters)]]
    antal = raw_data[len(letters)]
    strings = raw_data[len(letters)+1].split(' ')
    
    costs = pd.DataFrame(data=inpus,columns=letters,index=letters)
    # costs som dataframe, strings som array [ord1, ord2]
    return costs, strings,antal


def main():              
    costs, strings,antal = get_data()
    print(costs)
    print(strings)
    print(antal)
    


if __name__== "__main__": main()

