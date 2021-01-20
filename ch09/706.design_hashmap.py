# leetcode 706
import collections


class MyHashMap_0:

    def __init__(self):
        self.dict = collections.defaultdict()

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        try:
            return self.dict[key]
        except KeyError:
            return -1

    def remove(self, key):
        try:
            del self.dict[key]
        except KeyError:
            return -1


# seperate chaining
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap_A:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
             p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


if __name__ == "__main__":
    hashMap = MyHashMap_0()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    hashMap.get(1)
    hashMap.get(3)
    hashMap.put(2, 1)
    hashMap.get(2)
    hashMap.remove(2)
    hashMap.get(2)
