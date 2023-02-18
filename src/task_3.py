from tqdm import tqdm
 
PRIMES = []

NEUTRAL_ELEMENTS = (0, 1)

def is_prime(i: int) -> bool:
    for j in PRIMES:
        if i % j == 0:
            return False
    return True


def calculate_primes(end: int) -> None:
    for i in tqdm(range(2, end)):
        if is_prime(i):
            PRIMES.append(i)

calculate_primes(10 ** 3)
print(PRIMES)


def matches_condition(n: int) -> bool:
    return (6 * n - 1) not in PRIMES and (6 * n + 1) not in PRIMES


def main():
    """
    The French mathematician De Bouvelle proved incorrectly in 1509 that
    for all n ∈ N one of the numbers 6n - 1 or 6n + 1 is a prime number.
    1. Give an example that shows that he was wrong.
    2. Show that there are infinitely many n ∈ N that disprove this statement.
    """
    matched = []
    for i in tqdm(range(2, 10 ** 2)):
        if matches_condition(i):
            matched.append(i)
    print(matched)


if __name__ == "__main__":
    main()