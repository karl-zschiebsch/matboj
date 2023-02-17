from tqdm import tqdm

def quer_sum(i: int) -> int:
    q = 0
    n = i
    while (n > 0):
        t = n % 10
        q += t
        n //= 10
    return q


def evaluated(i: int) -> float:
    return i / quer_sum(i)


def main():
    minimum = 10 ** 3
    score = evaluated(minimum)
    for i in tqdm(range(10 ** 2, 10 ** 3)):
        if (score > evaluated(i)):
            score = evaluated(i)
            minimum = i
    print(minimum, score)


if __name__ == "__main__":
    main()