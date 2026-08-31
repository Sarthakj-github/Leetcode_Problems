# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        p=head.val
        L=[]
        i=1
        temp=head.next
        while temp.next!=None:
            if p<temp.val>temp.next.val or p>temp.val<temp.next.val:
                L.append(i)
            p=temp.val
            temp=temp.next
            i+=1
        if len(L)<2:
            return [-1,-1]
        l=len(L)
        m=i
        for i in range(1,l):
            m=min(L[i]-L[i-1],m)
        return [m,L[-1]-L[0]]
