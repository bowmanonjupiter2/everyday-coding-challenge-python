def maxDaysToWork(countTown: list) -> int:
    result = 0
    while len(countTown) > 1:
        countTown.sort(reverse=True)
        days_to_work = countTown[1]
        result += 2 * days_to_work
        countTown.pop(1)
        countTown[0] -= days_to_work
    return result


def test_maxDaysToWork():
    # Test case 1: Basic functionality
    countTown = [3, 2, 4]
    result = maxDaysToWork(countTown)
    expected = 8  # Work 3 days, then 2 days
    print(
        f"Test 1: countTown={countTown}, result={result}, expected={expected}: {'PASS' if result == expected else 'FAIL'}")



# Run the test cases
test_maxDaysToWork()
