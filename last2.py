import unittest


def last2(s: str) -> int:
    if not s or len(s) <= 3:
        return 0
    front = s[:-2]
    target = s[-2:]
    return find_occurrence(front, target, 0)


def find_occurrence(source: str, target: str, k: int) -> int:
    target_index = source.find(target)
    if target_index == -1:
        return k
    else:
        new_source = source[target_index + 1:]
        return find_occurrence(new_source, target, k + 1)


class TestLast2(unittest.TestCase):
    def test_last2(self):
        # Test cases
        self.assertEqual(last2("hixxhi"), 1)  # "hi" appears once in the front
        self.assertEqual(last2("xaxxaxaxx"), 1)  # "xx" appears once in the front
        self.assertEqual(last2("axxxaaxx"), 2)  # "xx" appears twice in the front
        self.assertEqual(last2(""), 0)  # Empty string
        self.assertEqual(last2("a"), 0)  # String too short
        self.assertEqual(last2("ab"), 0)  # String too short
        self.assertEqual(last2("abcabcabc"), 2)  # "bc" appears twice in the front



if __name__ == "__main__":
    unittest.main()
