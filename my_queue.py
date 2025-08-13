class MyQueue:
    def __init__(self, size):
        self.size = size
        self.used = 0
        self._list = []

    def enqueue(self, element):
        if self.used < self.size:
            self.used += 1
            self._list.append(element)

    def dequeue(self):
        if self.used > 0:
            self.used -= 1
            return self._list.pop(0)

    def peek(self):
        if self.used > 0:
            return self._list[0]


def test():
    my_queue = MyQueue(10)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    print(my_queue.peek())
    print(my_queue.dequeue())
    my_queue.enqueue(5)
    print(my_queue.peek())


if __name__ == '__main__':
    test()
