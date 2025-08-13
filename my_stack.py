class Stack:
    def __init__(self, size):
        self.size = size
        self.used = 0
        self._list = []

    def push(self, element):
        if self.used < self.size:
            self._list.append(element)
            self.used += 1

    def pop(self):
        if self.used > 0:
            self.used -= 1
            return self._list.pop()

    def peek(self):
        if self.used > 0:
            return self._list[-1]


def test():
    stack = Stack(10)
    stack.push(10)
    stack.push(1)
    stack.push(-2)
    stack.push(5)
    print(stack.pop())
    print(stack.peek())
    print(stack.pop())
    stack.push(4)
    print(stack.peek())


if __name__ == '__main__':
    test()
