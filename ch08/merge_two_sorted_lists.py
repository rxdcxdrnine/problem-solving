# leet code 21
from linked_list import *

def mergeTwoLists_0(l1, l2):
    # arguments are linked list head pointer
    p1, p2 = l1, l2

    # head is not a pointer here, just a dummy node
    # after merging the two sorted lists, execute head = head.next because head is dummy node
    head = ListNode()
    p = head

    while p1 or p2:
        if p1 is None:
            p.next = p2
            p2 = p2.next
        elif p2 is None:
            p.next = p1
            p1 = p1.next
        else:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
        p = p.next

    head = head.next
    return head


def mergeTwoLists_A(l1, l2):
    # arguments are linked list pointer here
    # always smaller element in l1; if l1.val > l2.val, swap l1 and l2
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists_A(l1.next, l2)
    return l1


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    while list1:
        linked_list1.insert_first(list1.pop())
    while list2:
        linked_list2.insert_first(list2.pop())

    linked_list1.print()
    linked_list2.print()

    p = mergeTwoLists_0(linked_list1.head, linked_list2.head)
    while p is not None:
        print(p.val, end='->')
        p = p.next
    print('None')