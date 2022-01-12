# Definition for singly-linked list.
import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    q = collections.deque()

    if not head:
        return True

    node = head
    while node:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True


if __name__ == "__main__":
    head = [1, 2, 2, 1]
    root = start = ListNode(None)
    for val in head:
        start.next = ListNode(val)
        start = start.next

    root = root.next
    print(isPalindrome(root))
