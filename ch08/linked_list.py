
# 1. LinkedList 로 연결리스트 구현
# 연결리스트 linked_list = LinkedList() 에서 linked_list.head 가 헤드 포인터 역할 (head_pointer = node)

# 2. ListNode 로 연결리스트 구현
# 더미노드 p = ListNode() 에서 p 가 헤드 포인터 역할 (head_pointer.next = node)
# 단 pointer = node 구현해야하므로, 맨 마지막에 p = p.next 로 더미 노드 다음 노드로 헤드포인터 수정 필요 (head_pointer = node)


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    # treat head/node/pre as pointer
    # use pointer with dot operator (.) instead of arrow operator (->) in Python

    def __init__(self):
        self.head = None

    def insert_first(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def insert(self, pre, val):
        node = ListNode(val)
        node.next = pre.next
        pre.next = node

    def delete_first(self):
        if self.head is not None:
            self.head = None
        removed = self.head
        self.head = removed.next
        return removed

    def delete(self, pre):
        removed = pre.next
        pre.next = removed.next
        return removed

    def print(self):
        p = self.head
        while p is not None:
            print(p.val, end='->')
            p = p.next
        # print None on the end of linked list
        print('None')


if __name__ == "__main__":
    linked_list = LinkedList()
    list = [1, 2, 4]

    # insert_first; insert all elements
    while list:
        linked_list.insert_first(list.pop())

    # insert; move head and insert the element
    p = linked_list.head
    while p.next.val != 4:
        p = p.next
    linked_list.insert(p, 5)

    # delete_first; delete all elements
    while linked_list.head:
        linked_list.delete_first()

    # delete; move head and delete the element
    p = linked_list.head
    while p.next.val != 4:
        p = p.next
    linked_list.delete(p)

    # print; print all elements
    linked_list.print()
