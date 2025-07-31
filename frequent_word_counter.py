import unittest


def top_k_most_frequent_words(paragraph: str, k: int) -> list:
    paragraph_list = paragraph.split(" ")
    paragraph_list.sort()
    paragraph_dic = {}
    for word in paragraph_list:
        if word in paragraph_dic.keys():
            paragraph_dic[word] += 1
        else:
            paragraph_dic[word] = 1

    new_dic = dict(sorted(paragraph_dic.items(), key=lambda item: item[1]))
    new_list = list(new_dic.items())
    new_list.reverse()

    actual_k = min(k, len(new_list))
    top_k_list = new_list[:actual_k]
    top_k_words = list(map(lambda item: item[0], top_k_list))
    return top_k_words


class TestTopKMostFrequentWords(unittest.TestCase):
    def test_top_k_most_frequent_words(self):
        # Test cases
        self.assertEqual(
            top_k_most_frequent_words("apple banana apple orange banana apple", 2),
            ["apple", "banana"]
        )
        self.assertEqual(
            top_k_most_frequent_words("cat dog cat bird dog cat", 3),
            ["cat", "dog", "bird"]
        )
        self.assertEqual(
            top_k_most_frequent_words("repeat repeat repeat", 2),
            ["repeat"]
        )
        self.assertEqual(
            top_k_most_frequent_words("singleword", 1),
            ["singleword"]
        )


if __name__ == "__main__":
    unittest.main()
