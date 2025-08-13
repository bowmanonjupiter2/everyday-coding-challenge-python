def merge_two_sorted_lists(one: list, the_other: list) -> list:
    i, j = 0, 0
    result = []
    while i < len(one) and j < len(the_other):
        if one[i] <= the_other[j]:
            result.append(one[i])
            i += 1
            continue
        else:
            result.append(the_other[j])
            j += 1
            continue

    if i < len(one):
        result.extend(one[i:])

    if j < len(the_other):
        result.extend(the_other[j:])
    return result


def test():
    test_list_1 = [1, 3, 5, 7]
    test_list_2 = [2, 4, 6, 20]
    result = merge_two_sorted_lists(test_list_1, test_list_2)
    print(result)


if __name__ == '__main__':
    test()
