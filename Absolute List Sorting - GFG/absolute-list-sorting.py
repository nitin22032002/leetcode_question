#User function Template for python3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    
    def sortList(self,head):
        next=None
        prv=None
        while(head):
            tem=Node(head.data)
            if(head.data>=0):
                if(next==None):
                    next=tem
                    prv=tem
                else:
                    next.next=tem
                    next=tem
            else:
                if(prv==None):
                    next=tem
                    prv=tem
                else:
                    tem.next=prv
                    prv=tem
            head=head.next
        return prv


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.last=self.head

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.last=new_node
            return
        self.last.next=new_node
        self.last=self.last.next
        

    
def PrintList(head):
    while head:
        print(head.data,end=' ')
        head=head.next


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n=int(input())
        ll = LinkedList() # create a new linked list 'll1'.
        nodes_ll = list(map(int, input().strip().split()))
        for nodes in nodes_ll:
            ll.append(nodes)  # add to the end of the list
        ob=Solution()
        
        PrintList(ob.sortList(ll.head))
        print()


# } Driver Code Ends