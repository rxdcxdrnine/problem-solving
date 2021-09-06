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
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev