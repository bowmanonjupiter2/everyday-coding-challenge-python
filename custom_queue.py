import unittest


class CustomQueue:
    def __init__(self, k: int):
        self.queue_length = k
        self.list = []
        self.sorted_list = []

    def enqueue(self, value: int):
        if len(self.list) < self.queue_length:
            self.list.append(value)
            self.sorted_list = sorted(self.list)

    def dequeue(self) -> int:
        if len(self.list) > 0:
            result = self.list.pop(0)
            self.sorted_list = sorted(self.list)
            return result
        else:
            return None

    def get_max(self) -> int:
        if len(self.sorted_list) > 0:
            return self.sorted_list[-1]
        else:
            return None


class TestCustomQueue(unittest.TestCase):
    def test_enqueue(self):
        queue = CustomQueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.list, [5, 10])

    def test_dequeue(self):
        queue = CustomQueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        result = queue.dequeue()
        self.assertEqual(result, 5)
        self.assertEqual(queue.list, [10])

    def test_get_max(self):
        queue = CustomQueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        self.assertEqual(queue.get_max(), 10)
        queue.dequeue()
        self.assertEqual(queue.get_max(), 10)

    def test_empty_dequeue(self):
        queue = CustomQueue(3)
        result = queue.dequeue()
        self.assertIsNone(result)

    def test_get_max_empty(self):
        queue = CustomQueue(3)
        self.assertIsNone(queue.get_max())


if __name__ == "__main__":
    unittest.main()
