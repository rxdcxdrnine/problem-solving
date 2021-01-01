# leetcode 206
from linked_list import *

def reverseList_0(head):
    # result is just a dummy node as a pointer (only use .next)
    # after inserting all the elements, execute result = result.next because result is dummy node
    result = ListNode()
    p = result

    while head:
        p_old = p.next
        p.next, head = head, head.next
        p.next.next = p_old

    result = result.next
    return result


def reverseList_A(head):
    def reverse(node, prev=None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)


def reveseList_B(head):
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev



if __name__ == "__main__":
    linked_list = LinkedList()
    list = [1, 2, 3, 4, 5]

    while list:
        linked_list.insert_first(list.pop())
    linked_list.print()

    p = reverseList(linked_list.head)
    while p:
        print(p.val, end='->')
        p = p.next
    print('None')