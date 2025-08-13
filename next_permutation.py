def next_permutation(nums: list) -> None:
    if len(nums) <= 1:
        return

    is_next_permutation_found = False

    k = len(nums) - 1

    while k >= 1 and not is_next_permutation_found:
        j = k - 1
        while j >= 0:
            if nums[j] < nums[k]:
                temp = nums[k]
                nums[k] = nums[j]
                nums[j] = temp
                is_next_permutation_found = True
                break
            j -= 1
        k -= 1

    if not is_next_permutation_found:
        nums.sort()
    else:
        nums[:] = nums[:j + 1] + sorted(nums[j + 1:])


def test():
    test_input = [5,4,7,5,3,2]
    next_permutation(test_input)
    print(test_input)


if __name__ == '__main__':
    test()
