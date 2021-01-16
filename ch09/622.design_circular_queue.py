# leetcode 622

class MyCircularQueue_0:

    def __init__(self, k):
        self.size = k + 1
        self.queue = [0] * self.size

        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            return True

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front + 1]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear % self.size]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


class MyCircularQueue_A:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value):
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None

"""
MyCircularQueue_0)
배열의 크기를 원형 큐의 크기보다 1칸 만큼 크게 할당
front 포인터를 맨 처음 원소보다 1칸 앞의 위치에 정의
rear 포인터를 맨 마지막 원소의 위치에 정의

배열이 비었을 때 -> front 포인터와 rear 포인터 동일
배열이 가득찼을 때 -> front 포인터가 rear 포인터의 1칸 앞에 위치 (배열의 크기가 원형 큐의 크기보다 1칸 더 크기 때문)
=> 비열이 비었을 때/가득찼을 때, front 포인터와 rear 포인터의 동일 여부 다름

MyCircularQueue_A)
배열의 크기를 원형 큐의 크기와 동일하게 정의
front 포인터를 맨 처음 원소의 위치에 정의
rear 포인터를 맨 마지막 원소보다 1칸 뒤의 위치에 정의

배열이 비었을 때 -> front 포인터와 rear 포인터 동일 + front 포인터에 None 원소 위치
배열이 가득찼을 때 -> front 포인터와 rear 포인터 동일 + front 포인터에 None 이 아닌 원소 위치
=> 배열이 비었을 때/가득찼을 때, front 포인터와 rear 포인터의 동일 여부 같으므로 구분할 기준이 하나 더 필요
"""



if __name__ == "__main__":
    circularQueue = MyCircularQueue_0(3)
    circularQueue.enQueue(1)
    circularQueue.enQueue(2)
    circularQueue.enQueue(3)
    circularQueue.enQueue(4)
    circularQueue.Rear()
    circularQueue.isFull()
    circularQueue.deQueue()
    circularQueue.enQueue(4)
    circularQueue.Rear()
