
from typing import Optional

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        mid=None
        i=1
        t=head
        while(i<=k):
            t=t.next
            i+=1
        mid=t
        root=self.solve(head,k)
        root2=self.solve(mid)
        head.next=root2
        mid.next=None
        return root
    def solve(self,head,k=-1):
        p=head
        q=head
        if(q):
            q=head.next
        while(q and k!=1):
            t=q.next
            q.next=p
            p=q
            q=t
            k-=1
        return p
        



#{ 
 # Driver Code Starts

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.reverse(head, k)
        
        printList(res)
        

# } Driver Code Ends