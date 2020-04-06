import sys

def get_data():
    print("get_data")
   
#%% 
N = 5
Q = 3
words = ['there','where','input','putin','hello']
queeries = [['there','where'],
            ['putin','input'],
            ['hello','putin']]   
def build_graph():
    print('Building graph')
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def printing(self):
        printing = self.head
        while printing is not None:
            print(printing.data)
            printing = printing.next
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
    
        #Update the new nodes next to existing ndoe
        NewNode.next = self.head
        self.head = NewNode
#
ll = LinkedList()
ll.head = Node(1)
n2 = Node(2)
n3 = Node(3)
ll.head.next= n2
n2.next=n3
#build_graph()
#%%

def BFS():
    print("BFS")


def print_results():
    print("results")

def main():                                     
    get_data()                    
    BFS() 
    print_results()                   


if __name__== "__main__": main()
