#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        middle=self.middle(head)
        # print(middle.data)
        middle.next=self.reverse(middle.next)
        mid=middle.next
        m=mid
        # while(m):
        #     print(m.data,end=",")
        #     m=m.next
        # print()
        t1=head.next
        t2=mid
        while(t2 and t1!=mid):
            t3=t2.next
            t4=t1.next
            t2.next=t1
            t1.next=t3
            t1=t4
            t2=t3
        head.next=mid
        return head
    def reverse(self,head):
        p=head
        q=head
        if(q):
            q=q.next
        if(not q):
            return p
        while(q):
            t=q.next
            q.next=p
            p=q
            q=t
        head.next=None
        return p
    def middle(self,head):
        p=head
        q=head.next
        if(not q):
            return p
        else:
            q=q.next
        while(q):
            p=p.next
            q=q.next
            if(q):
                q=q.next
        return p


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends