import unittest


def front3(s: str) -> str:
    str_list = list(s)
    head = str_list[:3]
    result = []
    result.extend(head)
    result.extend(head)
    result.extend(head)

    return ''.join(result)


class TestFront3(unittest.TestCase):
    def test_front3(self):
        # Test cases
        self.assertEqual(front3("Python"), "PytPytPyt")
        self.assertEqual(front3("abc"), "abcabcabc")
        self.assertEqual(front3("ab"), "ababab")
        self.assertEqual(front3(""), "")
        self.assertEqual(front3("a"), "aaa")


if __name__ == "__main__":
    unittest.main()
