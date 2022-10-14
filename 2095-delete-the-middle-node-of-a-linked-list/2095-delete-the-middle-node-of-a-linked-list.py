# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.middle(head,self.length(head),0)
    def length(self,head):
        if(not head):
            return 0
        return 1+self.length(head.next)
    def middle(self,head,l,c):
        if(c==(l//2)):
            return head.next
        else:
            head.next=self.middle(head.next,l,c+1)
            return head