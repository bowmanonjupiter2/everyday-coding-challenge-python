def find_balanced_sub_array(input_array:list)->bool:
    sum_array = sum(input_array)
    if sum_array % 2 != 0:
        return False
    else:
        half = sum_array / 2
        input_array.sort()