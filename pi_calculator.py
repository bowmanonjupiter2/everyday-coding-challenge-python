def pi_calculator(k: int) -> float:
    intermediate = 0
    for i in range(k):
        if i % 2 == 0:
            intermediate += 1 / (2 * i + 1)
        else:
            intermediate -= 1 / (2 * i + 1)
    return 4 * intermediate


def test():
    result = pi_calculator(100_000_000)
    print(f"result:{result} ")


if __name__ == "__main__":
    test()
