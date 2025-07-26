def find_longest_consecutive_n_sub_string(s: str, n: int = 2) -> int:
    result = 0
    current_longest = 0
    current_set = set()

    if len(s) == 0 or n < 2:
        return result

    s_list = list(s)

    for i in range(0, len(s_list)):
        current_set.add(s_list[i])
        if len(current_set) <= n:
            current_longest += 1
            continue
        else:
            current_set = set()
            current_set.add(s_list[i - 1])
            current_set.add(s_list[i])
            if current_longest > result:
                result = current_longest
            current_longest = n

    if current_longest > result:
        result = current_longest

    return result


def main():
    test_str = "abcabcc"
    result = find_longest_consecutive_n_sub_string(test_str, 2)
    print(f"result:{result}")


if __name__ == "__main__":
    main()
