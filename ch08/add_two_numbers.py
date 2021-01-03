# leetcode 2
from linked_list import *

# faster than 99.12% of python3 online submission!
def addTwoNumbers_0(l1, l2):
    p1, p2 = l1, l2
    while p1 or p2:
        p1.val += p2.val

        if not p1.next and p2.next:
            p1.next = ListNode()
            p1.next.val = 0
        elif p1.next and not p2.next:
            p2.next = ListNode()
            p2.next.val = 0
        elif not p1.next and not p2.next:
            if p1.val >= 10:
                p1.next = ListNode()
                p2.next = ListNode()
                p1.next.val = 0
                p2.next.val = 0

        if p1.val >= 10:
            p1.val -= 10
            p1.next.val += 1

        p1 = p1.next
        p2 = p2.next

    return l1


def add_two_numbers_A(l1, l2):
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
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    list1 = [2, 4, 3]
    list2 = [5, 6, 4]

    while list1:
        linked_list1.insert_first(list1.pop())
    while list2:
        linked_list2.insert_first(list2.pop())

    linked_list1.print()
    linked_list2.print()

    p = addTwoNumbers_0(linked_list1.head, linked_list2.head)
    while p:
        print(p.val, end='->')
        p = p.next
    print('None')