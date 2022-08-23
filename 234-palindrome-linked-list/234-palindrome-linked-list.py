# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(not head.next):
            return True
        else:
            mid=self.getMiddle(head)
            p=self.reverse(mid.next)
            while(p):
                if(head.val!=p.val):
                    return False
                head=head.next
                p=p.next
            return True
    def getMiddle(self,head):
        t=head
        if(t):
            p=t.next
        else:
            return None
        if(p):
            p=p.next
        else:
            return t
        while(p):
            t=t.next
            if(p.next):
                p=p.next.next
            else:
                p=p.next
        return t
    def reverse(self,head):
        t=head
        if(t):
            p=tem=t.next
        else:
            return None
        while(t and p):
            tem=p.next
            p.next=t
            t=p
            p=tem
        head.next=None
        return t