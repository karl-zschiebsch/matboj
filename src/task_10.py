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
    """
    11 (not necessarily different) integers are written on a board. Is it 
    possible that the product of any five numbers on the board is greater 
    than the product of the remaining numbers?
    """
    matched = []
    for i in tqdm(range(10**8)):
        numbers = generate_array(i, 4)
        if matches_condition(numbers):
            matched.append(numbers)
    print(matched[:10], ' ... ', matched[len(matched)-1])


if __name__ == "__main__":
    main()