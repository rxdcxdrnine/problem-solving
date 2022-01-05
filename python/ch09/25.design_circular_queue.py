class MyCircularQueue:

    def __init__(self, k):
        self.size = k + 1
        self.array = [None] * self.size

        self.front = 0
        self.rear = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.array[self.rear] = value
            return True

    def deQueue(self):
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.size
            self.array[self.front] = None
            return True

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.array[(self.front + 1) % self.size]

    def Rear(self):
        if self.isEmpty():
            return -1
        else:
            return self.array[self.rear % self.size]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


if __name__ == "__main__":
    myCircularQueue = MyCircularQueue(3)
    myCircularQueue.enQueue(3)
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.enQueue(1)
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.enQueue(2)
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.enQueue(3)
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.enQueue(4)
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.deQueue()
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    print(myCircularQueue.Front())
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    print(myCircularQueue.Rear())
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.isEmpty()
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
    myCircularQueue.isFull()
    print(myCircularQueue.array, myCircularQueue.front, myCircularQueue.rear)
