from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1:
        return l2

    if not l2:
        return l1

    root = p = ListNode(None)
    while l1 or l2:
        if not l1:
            p.next = l2
            l2 = l2.next
        elif not l2:
            p.next = l1
            l1 = l1.next
        else:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next

        p = p.next

    return root.next


if __name__ == "__main__":
    l1, l2 = [1, 2, 4], [1, 3, 4]

    root_1 = start_1 = ListNode(None)
    root_2 = start_2 = ListNode(None)

    for val in l1:
        start_1.next = ListNode(val)
        start_1 = start_1.next

    for val in l2:
        start_2.next = ListNode(val)
        start_2 = start_2.next

    root_1 = root_1.next
    root_2 = root_2.next

    root = mergeTwoLists(root_1, root_2)

    while root:
        print(root.val)
        root = root.next


