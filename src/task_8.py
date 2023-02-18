from tqdm import tqdm

def digit_sum(i: int) -> int:
    q = 0
    n = i
    while (n > 0):
        q += n % 10
        n //= 10
    return q


def evaluated(i: int) -> float:
    return i / digit_sum(i)


def main():
    """
    Let q(n) be the digit sum of a natural number n. Find the three-digit 
    natural number m for which the quotient m/q(m) is minimal.
    """
    minimum = 10 ** 3
    score = evaluated(minimum)
    for i in tqdm(range(10 ** 2, 10 ** 3)):
        if (score > evaluated(i)):
            score = evaluated(i)
            minimum = i
    print(minimum, score)


if __name__ == "__main__":
    main()