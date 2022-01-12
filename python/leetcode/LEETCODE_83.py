# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        prev: Optional[ListNode] = head        
        p: Optional[ListNode] = prev.next
        
        while p:
            
            if prev.val == p.val:
                prev.next = p.next
            else:
                prev = prev.next
            
            p = prev.next
            
        return head
