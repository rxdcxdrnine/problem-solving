from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList_0(head: Optional[ListNode]) -> Optional[ListNode]:
    stack = []

    while head:
        stack.append(head)
        head = head.next

    root = p = ListNode(None)
    while stack:
        p.next = stack.pop()
        p = p.next
    p.next = None

    return root.next


def reverseList_1(head: Optional[ListNode]) -> Optional[ListNode]:
    root = p = ListNode(None)

    while head:
        p_old = p.next
        p.next, head = head, head.next
        p.next.next = p_old

    return root.next

if __name__ == "__main__":
    head = [1, 2, 3, 4, 5]

    root = start = ListNode(None)
    for val in head:
        start.next = ListNode(val)
        start = start.next

    root = root.next
    head = reverseList_1(root)

    while head:
        print(head.val)
        head = head.next
