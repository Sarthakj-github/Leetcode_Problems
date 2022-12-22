# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        l=0
        while temp!=None:
            l+=1
            temp=temp.next

        temp=head
        if n==l:
            return head.next
        for i in range(l-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head
