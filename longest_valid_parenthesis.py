import copy
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        target = '()'
        i = 0
        idx_list = []
        result_list = []
        result = 0
        while i < len(s) - 1:
            found = s.find(target, i)
            if found != -1:
                idx_list.append(found)
            else:
                break
            i = found + 2
        for idx in idx_list:
            start = idx
            end = idx + 2
            mark_start = start
            mark_end = end
            while True:
                while start - 2 in idx_list:
                    start -= 2
                while end in idx_list:
                    end += 2
                while start > 0 and s[start - 1] == '(' and end < len(s) and s[end] == ')':
                    start -= 1
                    end += 1

                if mark_start == start and mark_end == end:
                    break
                else:
                    mark_start = start
                    mark_end = end

            if [start,end] not in result_list:
                result_list.append([start, end])

        for candidate in result_list:
            copied_list = copy.deepcopy(result_list)
            copied_list.remove(candidate)
            for copied_candidate in copied_list:
                if candidate[1] == copied_candidate[0]:
                    copied_list.remove(copied_candidate)
                    candidate = [candidate[0],copied_candidate[1]]
            if candidate[1] - candidate[0] > result:
                result = candidate[1] - candidate[0]

        return result


def test():
    s = Solution()
    test_input = ')(((((()())()()))()(()))('
    result = s.longestValidParentheses(test_input)
    print(f'{result}')


if __name__ == '__main__':
    test()
