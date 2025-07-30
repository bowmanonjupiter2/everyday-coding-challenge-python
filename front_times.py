import unittest


def front_times(s: str, n: int) -> str:
    str_list = list(s)
    head_list = str_list[:3]
    result_list = []
    for i in range(n):
        result_list.extend(head_list)
    return ''.join(result_list)


class TestFrontTimes(unittest.TestCase):
    def test_front_times(self):
        # Test cases
        self.assertEqual(front_times("Python", 3), "PytPytPyt")
        self.assertEqual(front_times("abc", 2), "abcabc")
        self.assertEqual(front_times("ab", 4), "abababab")
        self.assertEqual(front_times("", 5), "")
        self.assertEqual(front_times("a", 3), "aaa")
        self.assertEqual(front_times("Hello", 0), "")


if __name__ == "__main__":
    unittest.main()
