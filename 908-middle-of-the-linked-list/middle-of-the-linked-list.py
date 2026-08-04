# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
        return slow
"""
n=0
temp=self.head
while temp is not None:
    n+=1
    temp.next
    #for even length
    temp=self.head
    for i in range(0,n//2):
        temp=temp.next
    return temp
"""

        