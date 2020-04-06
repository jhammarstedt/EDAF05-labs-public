import sys

def get_data():
    raw_data = []                           
    for input in sys.stdin:
        print(input)
        raw_data.append(input.strip())          # import every line from system in

    N = int(raw_data[0].split(" ")[0])          # extract N from the input data
    Q = int(raw_data[0].split(" ")[1])          # extract Q from the input data

    elements = raw_data[1:N+1]                  # extract the graph elements from the input data
    queries = raw_data[N+1:]                    # extract the queries from the input data
    
    return elements, queries

def split_array(queries):
    start = []
    goal = []
    for e in queries:
        start.append(e.split(" ")[0])
        goal.append(e.split(" ")[0])
    return start, goal


def BFS():
    # utför BFS för varje ord
    # spara resultat i ny databehållare: (ord, antal hopp)
    # returnera data behållaren
    return "bfs results" 

def print_results(x, results):
    for a, b in zip(x, results):
        print(f"a:{a} b:{b} ")
    # iterera igenom databehållaren, printa värdet.

def main():                                     
    elements, queries = get_data()
    start, goal = split_array(queries)
    results = BFS() 
    print_results(start, goal)                   


if __name__== "__main__": main()
