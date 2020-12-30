# leetcode 234
import collections

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next  ## next: ListNode

class Solution:
    def isPalindrome_A(self, head):
        q = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while q:
            if q.pop(0) != q.pop():
                return False
        return True

    def isPalindrome_B(self, head):
        q = collections.deque()

        if not head:
            return True

        node = head
        while head is not None:
            q.append(node.val)
            node = node.next

        while q:
            if q.popleft() != q.pop()
                return False
        return True

    def isPalindrome_C(self, head):
        

