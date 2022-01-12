import heapq
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists_0(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    p1 = p2 = ListNode()

    for i in reversed(range(len(lists))):
        if not lists[i]:
            lists.pop(i)

    while lists:
        min_node = min(lists, key=lambda x: x.val)

        p2.next = min_node
        p2 = p2.next

        argmin = lists.index(min_node)
        if not min_node.next:
            lists.pop(argmin)
        else:
            lists[argmin] = lists[argmin].next

    return p1.next


def mergeKLists_1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (list[i].val, i, lists[i]))

