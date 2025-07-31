import unittest


def find_the_target_element(source_list: list, target: int) -> list:
    if target in source_list:
        return [target]
    else:
        for i in source_list:
            new_source_list = source_list.copy()
            new_source_list.remove(i)
            new_target = target - i
            result = [i]
            result.extend(find_the_target_element(new_source_list, new_target))
            return result
        return []


def find_balanced_sub_array(input_array: list) -> bool:
    if not input_array:
        return True
    
    sum_array = sum(input_array)
    if sum_array % 2 != 0:
        return False
    else:
        half = int(sum_array / 2)
        result = find_the_target_element(input_array, half)
        if not result:
            return False
        else:
            return True


class TestFindBalancedSubArray(unittest.TestCase):
    def test_balanced_sub_array(self):
        # Test cases
        self.assertTrue(find_balanced_sub_array([1, 5, 11, 5]))  # Balanced
        self.assertFalse(find_balanced_sub_array([1, 2, 3, 5]))  # Not balanced
        self.assertTrue(find_balanced_sub_array([2, 2, 2, 2]))  # Balanced
        self.assertFalse(find_balanced_sub_array([1, 1, 1]))  # Not balanced
        self.assertTrue(find_balanced_sub_array([10, 10, 10, 10, 20, 20]))  # Balanced
        self.assertFalse(find_balanced_sub_array([1]))  # Single element, not balanced
        self.assertTrue(find_balanced_sub_array([]))  # Empty array, considered balanced


if __name__ == "__main__":
    unittest.main()
