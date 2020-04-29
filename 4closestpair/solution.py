import sys


def init():
    raw_data = []                           
    for input in sys.stdin:
        raw_data.append(input.strip())                  # append every input line to raw_data



def main():              
    init()

if __name__== "__main__": main()

