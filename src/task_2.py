from tqdm import tqdm

ANIMALS = [ ("horse", 31), ("cow", 21) ]

TOTAL = 1770

def matches_condition(n: int) -> bool:
    return n == TOTAL


def main():
    combinations = []
    for i in tqdm(range(100)):
        for j in range(100):
            if(matches_condition(ANIMALS[0][1] * i + ANIMALS[1][1] * j)):
                combinations.append((ANIMALS[0][0], i,ANIMALS[1][0], j))

    print(combinations)


if __name__ == "__main__":
    main()