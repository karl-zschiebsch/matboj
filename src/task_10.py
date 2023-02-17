from tqdm import tqdm

def product(data: list):
    product = 1
    for i in data:
        product *= i
    return product


def matches_condition(data: list, split: int = 5) -> bool:
    data.sort(reverse=True)
    return product(data[:split]) > product(data[split:])


def generate_array(seed: int, max: int, size: int = 11) -> list:
    generated = []
    for _ in range(size):
        generated.append(seed % max)
        seed //= max
    return generated


def main():
    matched = []
    for i in tqdm(range(10**8)):
        numbers = generate_array(i, 4)
        if matches_condition(numbers):
            matched.append(numbers)
    print(matched[:10], ' ... ', matched[len(matched)-1])


if __name__ == "__main__":
    main()