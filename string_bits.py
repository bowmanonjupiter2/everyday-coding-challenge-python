import unittest


def string_bits(s: str) -> str:
    str_list = list(s)
    result_list = []
    for idx, v in enumerate(str_list):
        if idx % 2 == 0:
            result_list.append(v)
    return ''.join(result_list)


class TestStringBits(unittest.TestCase):
    def test_string_bits(self):
        # Test cases
        self.assertEqual(string_bits("hello"), "hlo")
        self.assertEqual(string_bits("abcdef"), "ace")
        self.assertEqual(string_bits("a"), "a")
        self.assertEqual(string_bits(""), "")
        self.assertEqual(string_bits("123456789"), "13579")
        self.assertEqual(string_bits("Python"), "Pto")


if __name__ == "__main__":
    unittest.main()
