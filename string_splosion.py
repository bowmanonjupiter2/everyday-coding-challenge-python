import unittest


def string_splosion(s: str) -> str:
    result_str = ""
    for i in range(len(s)+1):
        result_str += s[:i]
    return result_str


class TestStringSplosion(unittest.TestCase):
    def test_string_splosion(self):
        # Test cases
        self.assertEqual(string_splosion("Code"), "CCoCodCode")
        self.assertEqual(string_splosion("abc"), "aababc")
        self.assertEqual(string_splosion("ab"), "aab")
        self.assertEqual(string_splosion("a"), "a")
        self.assertEqual(string_splosion(""), "")


if __name__ == "__main__":
    unittest.main()
