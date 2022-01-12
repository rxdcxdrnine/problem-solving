# leetcode 23
import heapq

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def mergeKLists_0(lists):
    p1 = ListNode()
    p2 = p1

    # list 에서 반복문을 통해 조건을 만족하는 원소를 지워야 하는 경우,
    # 순서를 뒤집어 뒤에서부터 조건을 만족하는 원소를 제거  e.g.reverse(range(len(list)))
    for i in reversed(range(len(lists))):
        if not lists[i]:
            lists.pop(i)

    while lists:
        min_node = min(lists, key=lambda x: x.val)

        p2.next = ListNode(min_node.val)
        p2 = p2.next

        argmin = lists.index(min_node)
        if lists[argmin].next is None:
            lists.pop(argmin)
        else:
            lists[argmin] = lists[argmin].next

    p1 = p1.next
    return p1


def mergeKLists_A(lists):
    root = result = ListNode()
    heap = []

    for i in range(len(lists)):
        if list[i]:
            heapq.heappush(heap, (lists[i].val, i, list[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = []

    for i in range(len(lists)):
        p1 = ListNode()
        p2 = p1
        while lists[i]:
            p2.next = ListNode(lists[i].pop(0))
            p2 = p2.next
        p1 = p1.next
        linked_lists.append(p1)

    p = mergeKLists_0(linked_lists)

    while p:
        print(p.val, end='->')
        p = p.next
    print('None')