# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p: Optional[ListNode] = head
        visited: List[int] = []
            
        while p:
            p = p.next

            if id(p) in visited:
                return True
            else:
                visited.append(id(p))
                
        return False
