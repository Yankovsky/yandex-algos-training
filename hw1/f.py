def laptops(a1, b1, a2, b2):
    combinations = [
        (a1 + a2, max(b1, b2)),
        (a1 + b2, max(b1, a2)),
        (max(a1, a2), b1 + b2),
        (max(a1, b2), b1 + a2)
    ]

    return min(combinations, key=lambda y: y[0] * y[1])


assert laptops(10, 2, 2, 10) == (20, 2)
assert laptops(5, 7, 3, 2) == (5, 9)


def main():
    a1, b1, a2, b2 = map(int, input().split())
    result = laptops(a1, b1, a2, b2)
    print(f"{result[0]} {result[1]}")


if __name__ == '__main__':
    main()
