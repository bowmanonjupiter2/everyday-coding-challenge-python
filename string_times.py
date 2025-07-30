import unittest


def string_times(s: str, n: int) -> str:
    result_list = []
    for i in range(n):
        result_list.extend(list(s))
    return ''.join(result_list)


class TestStringTimes(unittest.TestCase):
    def test_string_times(self):
        # Test cases
        self.assertEqual(string_times("abc", 3), "abcabcabc")
        self.assertEqual(string_times("a", 5), "aaaaa")
        self.assertEqual(string_times("", 4), "")
        self.assertEqual(string_times("xyz", 0), "")
        self.assertEqual(string_times("test", 1), "test")


if __name__ == "__main__":
    unittest.main()
