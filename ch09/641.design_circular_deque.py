# leetcode 641

# circularDeque with python list
class MyCircularDeque_0:

    def __init__(self, k):
        self.size = k + 1
        self.deque = [None] * self.size

        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        else:
            self.deque[self.front] = value
            self.front = (self.front - 1 + self.size) % self.size
            return True

    def insertLast(self, value):
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.deque[self.rear] = value
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            self.deque[self.front] = None
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.deque[self.rear] = None
            self.rear = (self.rear - 1 + self.size) % self.size
            return True

    def getFront(self):
        if self.isEmpty():
            return -1
        else:
            return self.deque[(self.front + 1) % self.size]

    def getRear(self):
        if self.isEmpty():
            return -1
        else:
            return self.deque[self.rear]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


## circular deque with linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyCircularDeque_A:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    ## insert/delete Front/Rear 를 구현하기 앞서 _add, _del 을 먼저 구현
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k




if __name__ == "__main__":
    circularDeque = MyCircularDeque_0(3)
    circularDeque.insertLast(1)
    circularDeque.insertLast(2)
    circularDeque.insertFront(3)
    circularDeque.insertFront(4)
    circularDeque.getRear()
    circularDeque.isFull()
    circularDeque.deleteLast()
    circularDeque.insertFront(4)
    circularDeque.getFront()
