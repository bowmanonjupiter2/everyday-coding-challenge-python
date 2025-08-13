def binary_search(src: list, target):
    low_end = 0
    high_end = len(src) - 1

    while low_end < high_end:
        mid = low_end + (high_end - low_end) // 2
        if mid == low_end or mid == high_end:
            if target == src[low_end]:
                return low_end
            elif target == src[high_end]:
                return high_end
            else:
                print('oops')
                break
        else:
            if target < src[mid]:
                high_end = mid
            elif target == src[mid]:
                return mid
            else:
                low_end = mid
    return -1


def test_comprehensive():
    test_input = [1, 3, 5, 7, 9, 12]

    # Test cases for each target
    test_cases = [
        (-1, -1),  # Target not in array (less than min)
        (1, 0),  # First element
        (2, -1),  # Between first and second elements
        (4, -1),  # Between second and third elements
        (5, 2),  # Third element
        (6, -1),  # Between third and fourth elements
        (8, -1),  # Between fourth and fifth elements
        (11, -1),  # Between fifth and sixth elements
        (12, 5),  # Last element
        (13, -1)  # Target not in array (greater than max)
    ]

    for target, expected in test_cases:
        result = binary_search(test_input, target)
        status = "PASS" if result == expected else "FAIL"
        print(f'Target: {target:2d}, Expected: {expected:2d}, Got: {result:2d} - {status}')


if __name__ == '__main__':
    test_comprehensive()
