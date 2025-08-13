def min_projects_needed(scores: list, p, q) -> int:
    result = 0
    while not is_all_zero(scores):
        scores.sort(reverse=True)
        num_of_projects = scores[0] // p
        if num_of_projects == 0:
            num_of_projects = 1
        result += num_of_projects
        scores[0] -= num_of_projects * p
        for i in range(1, len(scores)):
            scores[i] -= num_of_projects * q
            if scores[i] < 0:
                scores[i] = 0
            continue
    return result


def is_all_zero(src: list) -> bool:
    return len(list(filter(lambda x: x != 0, src))) == 0


def test():
    test_input = [5, 6, 9]
    p = 2
    q = 1
    result = min_projects_needed(test_input, p, q)
    print(result)


if __name__ == '__main__':
    test()
