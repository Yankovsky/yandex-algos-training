import sys


def intersection(list_a, list_b):
    return sorted(set(list_a) & set(list_b))


assert intersection([1, 3, 2], [4, 3, 2]) == [2, 3]
assert intersection([1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8]) == [2, 4]


def main():
    reader = (map(int, line.split()) for line in sys.stdin)
    print(*intersection(next(reader), next(reader)))


if __name__ == '__main__':
    main()
