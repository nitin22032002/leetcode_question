#User function Template for python3

class Solution:
    def modify_the_list(self, head):
        mid=self.middle(head)
        nextP=mid.next
        if(not nextP):
            return head
        mid.next=self.reverse(nextP)
        nextP=mid.next
        end=nextP
        start=head
        while(start and end):
            v=start.data
            start.data=end.data-v
            end.data=v
            start=start.next
            end=end.next
        mid.next=self.reverse(nextP)
        return head
    def middle(self,head):
        p=head
        q=head.next
        if(q):
            q=q.next
        else:
            return q
        while(q):
            p=p.next
            q=q.next
            if(q):
                q=q.next
        return p
    
    def reverse(self,head):
        p=head
        q=head.next
        while(q):
            t=q.next
            q.next=p
            p=q
            q=t
        head.next=None
        return p
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends