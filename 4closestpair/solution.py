import sys

def get_data():
    raw_data = []                           
    for input in sys.stdin:
        # append every input line to raw_data
        raw_data.append(input.strip())                                      
    
    # extract points (x, y) from raw_data
    points = [[int(i) for i in line.split(' ')] for line in raw_data[1:]]   

    return points


def closest_point(P):
    P_x = []
    P_y = []

    #Create two sorted arrays P_x and P_y.
    for point in P:
        P_x.append(P[0])
        P_y.append(P[1])

    return closest(P_x, P_y, len(P))

def check_border(points, d):
    return d

def closest(P_x, P_y, N):
    #Divide P_x into two arrays L_x and R_x (left and right)
    L_x = P_x[:N] 
    R_x = P_x[N:]
    #Divide P_y into two arrays L_y and R_y (left and right)
    L_y = P_y[:N] 
    R_y = P_y[N:]
    
    L = closest(L_x, L_y, int(N/2))
    R = closest(R_x, R_y, int(N/2))

    #Compute d as the minimum from these subproblems
    d = min(L, R)

    #Create the set S_y from P_y
    S_y = set(P_y)

    #Check each point in S_y to see if any nearby point is closer than d
    d = check_border(S_y, d)

    return d


def main():              
    points = get_data()
    distance = closest_point(points)
    print(distance)

if __name__== "__main__": main()

