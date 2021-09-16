from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    root = prev = ListNode(None)
    while head and head.next:
        post = head.next
        head.next = post.next
        post.next = head

        prev.next = post

        head = head.next
        prev = prev.next.next

    return root.next


if __name__ == "__main__":
    head = [1, 2, 3, 4]

    p = ListNode(None)
    while head:
        node = ListNode(head.pop())
        node.next = p.next
        p.next = node

    p = p.next

    root = swapPairs(p)

    while root:
        print(root.val)
        root = root.next

