# # Definition for singly-linked list.
# from typing import Optional
#
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head.next:
#             return True
#
#         stack = []
#         flag = False
#         while head:
#             if stack and stack[-1] == head.val:
#                 stack.pop()
#             elif stack and not flag:
#                 flag = True
#             else:
#                 stack.append(head.val)
#             head = head.next
#
#         if stack:
#             return False
#         else:
#             return True
#
#
# if __name__ == "__main__":
#     head = [1, 2, 2, 1]
#
#     root = start = ListNode(None)
#     for val in head:
#         start.next = ListNode(val)
#         start = start.next
#
#     root = root.next
#     solution = Solution()
#     print(solution.isPalindrome(root))
