import sys
import math

def get_data():
    
    raw_data = []                           
    for input in sys.stdin:
        # append every input line to raw_data
        raw_data.append(input.strip())                                      
    
    # extract points (x, y) from raw_data
    points = [[int(i) for i in line.split(' ')] for line in raw_data[1:]]   
    
    return points


def closest_point(P):
    P_x = P
    P_y = P

    #Create two sorted arrays P_x and P_y.
    P_x = sorted(P_x,key=lambda x:x[0])
    P_y = sorted(P_y,key=lambda x:x[1])

    return closest(P_x, P_y, len(P))

def get_distance(p1,p2):
    """Get the distance between two points"""
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def closest(P_x, P_y, N):
    #print(N)
    if N==1:
        return None
    elif N ==2:
        return get_distance(P_x[0],P_x[1])
    elif N ==3:
        return min(get_distance(P_x[0],P_x[1]),get_distance(P_x[0],P_x[2]),
                   get_distance(P_x[1],P_x[2]))
    else:
        #Divide P_x into two arrays L_x and R_x (left and right)
        L_x,R_x = P_x[:int(len(P_x)/2)], P_x[int(len(P_x)/2):]
       
        L_y,R_y = P_y[:int(len(P_x)/2)],P_y[int(len(P_x)/2):]
        
        L = closest(L_x, L_y, int(N/2))
        R = closest(R_x, R_y, int(N/2))
        #Compute d as the minimum from these subproblems
        d = min(L, R)
       
        
        
        
        #Get the rightmost element in L_x. Since it's sorted it will be the last element, then get that x-value
        x_star = L_x[-1][0]  

        #Creating L         
        L= [[x_star,y[1]] for y in L_y]
        
        #Creating S = points in P wihtin distance d from L
        S = [point for point in P_x if abs(point[0]-x_star)<=d]
        
        
        
        #Create the set S_y from P_y
        S_y = sorted(S,key = lambda x: x[1])                        #sorting the elements in S by y cord
        
        
        inner_minimum = 10**1000
        
        #check the 15 closest points for all points s in S.
        for count,point in enumerate(S_y):
            for inner_count in range(0,min(len(S_y),15)):           #if S_y contains less than 15 points
                if count==inner_count:continue                      #don't compare same points
                
                inner_minimum= min(get_distance(point,S_y[inner_count]),inner_minimum)
                

        return min(inner_minimum,d)                                 #check which one is the smallest between delta and inner
        


def main():              
    points = get_data()
    #print(f'points are: {points}')
    distance = closest_point(points)
    print(round(distance,6))

if __name__== "__main__": main()

