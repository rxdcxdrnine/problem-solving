# leetcode 225

class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        length = len(self.queue)
        for i in range(length):
            x = self.queue.pop(0)
            if i != length - 1:
                self.queue.append(x)
        return x

    def top(self):
        x = self.queue[-1]
        return x

    def empty(self):
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == "__main__":
    stack = MyStack()

    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())