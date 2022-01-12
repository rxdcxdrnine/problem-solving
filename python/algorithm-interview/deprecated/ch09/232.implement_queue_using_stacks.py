# leetcode 232

class MyQueue_0:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        tmp = []    # stack
        while self.stack:
            x = self.stack.pop()
            if self.stack:
                tmp.append(x)

        while tmp:
            y = tmp.pop()
            self.stack.append(y)
        return x

    def peek(self):
        tmp = []  # stack
        while self.stack:
            x = self.stack.pop()
            tmp.append(x)

        while tmp:
            y = tmp.pop()
            self.stack.append(y)
        return x

    def empty(self):
        return not self.stack


class MyQueue_A:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []

if __name__ == "__main__":

    queue = MyQueue_0()
    queue.push(1)
    queue.push(2)
    queue.peek()
    queue.pop()
    queue.empty()