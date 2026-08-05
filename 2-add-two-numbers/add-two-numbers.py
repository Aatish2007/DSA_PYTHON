# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head node to simplify list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop while there are nodes left in l1 or l2, or a remaining carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and update carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Attach the new digit node
            current.next = ListNode(digit)
            current = current.next
            
            # Advance pointers if nodes exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next