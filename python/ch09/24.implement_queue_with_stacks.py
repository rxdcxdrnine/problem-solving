class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        peek = None
        while self.stack_1:
            peek = self.stack_1.pop()
            if not self.stack_1:
                continue
            self.stack_2.append(peek)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return peek

    def peek(self) -> int:
        """
        Get the front element.
        """
        peek = None
        while self.stack_1:
            peek = self.stack_1.pop()
            self.stack_2.append(peek)

        while self.stack_2:
            self.stack_1.append(self.stack_2.pop())

        return peek

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack_1) == 0


if __name__ == "__main__":
    myQueue = MyQueue();
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())
