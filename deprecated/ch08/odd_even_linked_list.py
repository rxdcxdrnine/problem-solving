# leetcode 328
from linked_list import *

# time complexity in O(n) but too slow
def oddEvenList_0(head):
    p = root = head
    count = 0

    if not p or not p.next or not p.next.next:
        return root

    iter = 0
    while p:
        p = p.next
        iter += 1

    def swap(pre):
        cur, post = pre.next, pre.next.next
        pre.next, cur.next, post.next = post, post.next, cur

    iter = (iter - 1) // 2
    for i in range(iter, 0, -1):
        p = head
        count = 0
        while p.next and p.next.next:
            count += 1
            swap(p)
            p = p.next.next
            if count == i:
                break
        head = head.next

    return root


def oddEventList_A(head):
    if not head:
        return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


if __name__ == "__main__":
    linked_list = LinkedList()
    li = [1, 2, 3, 4, 5, 6, 7]

    while li:
        linked_list.insert_first(li.pop())
    linked_list.print()

    p1 = oddEvenList_0(linked_list.head)
    while p1:
        print(p1.val, end='->')
        p1 = p1.next
    print('None')
