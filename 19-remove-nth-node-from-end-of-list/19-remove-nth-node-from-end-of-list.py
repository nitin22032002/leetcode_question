# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=self.length(head)
        return self.get(head,l-n)
    def get(self,head,n):
        if(head):
            if(n==0):
                return self.get(head.next,n-1)
            head.next=self.get(head.next,n-1)
        return head
    def length(self,head):
        if(head):
            return 1+self.length(head.next)
        return 0
            