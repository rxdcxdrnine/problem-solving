from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers_0(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0

    root = p = ListNode(None)
    while l1 or l2:
        if not l1:
            p.next = ListNode(l2.val)
            l2 = l2.next
        elif not l2:
            p.next = ListNode(l1.val)
            l1 = l1.next
        else:
            p.next = ListNode(l1.val + l2.val)
            l1 = l1.next
            l2 = l2.next

        if carry:
            p.next.val += 1

        if p.next.val >= 10:
            carry = 1
            p.next.val -= 10
        else:
            carry = 0

        p = p.next

    if carry:
        p.next = ListNode(1)

    return root.next


def addTwoNumbers_1(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next

if __name__ == "__main__":
    l1, l2 = [2, 4, 3], [1, 6, 6, 4]

    p1 = ListNode(None)
    while l1:
        node = ListNode(l1.pop())
        node.next = p1.next
        p1.next = node

    p2 = ListNode(None)
    while l2:
        node = ListNode(l2.pop())
        node.next = p2.next
        p2.next = node

    p1 = p1.next
    p2 = p2.next

    root = addTwoNumbers_0(p1, p2)
    while root:
        print(root.val)
        root = root.next