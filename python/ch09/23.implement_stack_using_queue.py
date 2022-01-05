from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_1 = deque()
        self.queue_2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue_1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        top = None
        while self.queue_1:
            top = self.queue_1.popleft()
            if not self.queue_1:
                continue
            self.queue_2.append(top)

        while self.queue_2:
            self.queue_1.append(self.queue_2.popleft())

        return top


    def top(self) -> int:
        """
        Get the top element.
        """
        top = None
        while self.queue_1:
            top = self.queue_1.popleft()
            self.queue_2.append(top)

        while self.queue_2:
            self.queue_1.append(self.queue_2.popleft())

        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue_1) == 0


if __name__ == "__main__":
    myStack = MyStack()
    myStack.push(1)
    myStack.push(2)
    print(myStack.top())
    print(myStack.pop())
    print(myStack.empty())
