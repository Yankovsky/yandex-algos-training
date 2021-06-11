from collections import Counter


def keyboard(keys_durability, keys_pressed_sequence):
    keys_pressed_counter = Counter(keys_pressed_sequence)
    keyboard_durability_counter = Counter({i + 1: durability for i, durability in enumerate(keys_durability)})
    return [
        'YES' if (keyboard_durability_counter[i + 1] - keys_pressed_counter[i + 1]) < 0
        else 'NO'
        for i in range(len(keys_durability))
    ]


assert keyboard([1, 50, 3, 4, 3], [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]) == ['YES', 'NO', 'NO', 'NO', 'YES']


def main():
    n = int(input())
    keys_durability = list(map(int, input().split()))
    k = int(input())
    keys_pressed_sequence = map(int, input().split())
    results = keyboard(keys_durability, keys_pressed_sequence)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
