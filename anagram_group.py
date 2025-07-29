from typing import List, Callable, Any, Union
import unittest

def anagram_group(words: List) -> List:
    anagram_dic = {}
    result_list = []
    for word in words:
        sum_of_hash = sum(hash(i) for i in list(word))
        key_hash = str(sum_of_hash)
        if key_hash in anagram_dic:
            anagram_dic[key_hash].append(word)
        else:
            anagram_dic[key_hash] = [word]

    result_list.extend(anagram_dic.values())

    return result_list


class TestAnagramGroup(unittest.TestCase):
    def test_anagram_group_basic(self):
        words = ["bat", "tab", "cat", "act", "dog"]
        result = anagram_group(words)
        expected = [["bat", "tab"], ["cat", "act"], ["dog"]]
        self.assertEqual(sorted([sorted(group) for group in result]), sorted([sorted(group) for group in expected]))

    def test_anagram_group_empty(self):
        words = []
        result = anagram_group(words)
        expected = []
        self.assertEqual(result, expected)

    def test_anagram_group_no_anagrams(self):
        words = ["apple", "banana", "cherry"]
        result = anagram_group(words)
        expected = [["apple"], ["banana"], ["cherry"]]
        self.assertEqual(sorted([sorted(group) for group in result]), sorted([sorted(group) for group in expected]))

    def test_anagram_group_single_word(self):
        words = ["word"]
        result = anagram_group(words)
        expected = [["word"]]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
