# leet code 24
from linked_list import *

def swapPairs_0(head):
    root = head

    if not head:
        return root

    while head.next:
        head.val, head.next.val = head.next.val, head.val
        if not head.next.next:
            break
        else:
            head = head.next.next

    return root


def swapPairs_A(head):
    cur = head

    while cur and cur.next:
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head


def swapPairs_B(head):
    root = prev = ListNode()
    prev.next = head

    while head and head.next:
        # swap head->b to b->head
        b = head.next
        head.next = b.next
        b.next = head

        # concat prev->b
        prev.next = b

        # move head and prev
        head = head.next
        prev = prev.next.next

    return root.next


def swapPairs_C(head):
    if head and head.next:
        p = head.next

        head.next = swapPairs_C(p.next)
        p.next = head
        return p

    return head

if __name__ == "__main__":
    linked_list = LinkedList()
    li = [1, 2, 3, 4]

    while li:
        linked_list.insert_first(li.pop())
    linked_list.print()

    p = swapPairs_0(linked_list.head)
    while p:
        print(p.val, end="->")
        p = p.next
    print("None")