def find_longest_non_repeating_substring(s: str) -> str:
    str_list = list(s)
    current_longest_substring_list = []

    result_list = []
    for char in str_list:

        if char not in current_longest_substring_list:
            current_longest_substring_list.append(char)
        else:
            if len(current_longest_substring_list) > len(result_list):
                result_list = current_longest_substring_list

            new_idx = current_longest_substring_list.index(char)
            current_longest_substring_list = current_longest_substring_list[new_idx + 1:]
            current_longest_substring_list.append(char)

    return ''.join(result_list)


def test():
    test_str = "brkaabcdefghijjxxx"
    result_str = find_longest_non_repeating_substring(test_str)
    print(result_str)


if __name__ == "__main__":
    test()
