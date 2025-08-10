import copy


class Solution:
    def tryFind(self, candidates: list, target: int, step: int) -> bool:
        if len(candidates) == 0:
            return True

        copied_candidates = copy.deepcopy(candidates)
        for candidate in copied_candidates:
            if target in candidate:
                copied_candidates.remove(candidate)
                if len(copied_candidates) == 0:
                    return True
                else:
                    return self.tryFind(copied_candidates, target + step, step)
        return False

    def findAllIndexes(self, s: str, word: str) -> list:
        result_list = []
        start_idx = 0
        found_dix = s.find(word, start_idx)
        while found_dix != -1:
            result_list.append(found_dix)
            start_idx = found_dix + 1
            found_dix = s.find(word, start_idx)
        return result_list

    def findSubstring(self, s: str, words: list[str]) -> list:
        result_list = []
        found_idx_words_list = []
        for word in words:
            found_idx_words_list.append(self.findAllIndexes(s, word))
        filtered_found_idx_words_list = list(filter(lambda x: len(x) > 0, found_idx_words_list))
        if len(filtered_found_idx_words_list) < len(words):
            return result_list
        else:
            step = len(words[0])
            for found_idx_word_list in filtered_found_idx_words_list:
                for found_dix in found_idx_word_list:
                    copied_filtered_found_idx_words_list = copy.deepcopy(filtered_found_idx_words_list)
                    copied_filtered_found_idx_words_list.remove(found_idx_word_list)
                    if self.tryFind(copied_filtered_found_idx_words_list, found_dix + step, step):
                        result_list.append(found_dix)
        return sorted(list(set(result_list)))


def test():
    solution = Solution()
    test_str = 'a'
    test_words = ['a']
    result = solution.findSubstring(test_str, test_words)
    print(result)


if __name__ == '__main__':
    test()
