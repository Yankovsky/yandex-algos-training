def prisoner(a, b, c, d, e):
    brick_dimensions = sorted([a, b, c])
    hole_dimensions = sorted([d, e])
    return 'YES' if brick_dimensions[0] <= hole_dimensions[0] and brick_dimensions[1] <= hole_dimensions[1] else 'NO'


assert prisoner(1, 1, 1, 1, 1) == 'YES'
assert prisoner(2, 2, 2, 1, 1) == 'NO'
assert prisoner(2, 2, 1, 1, 1) == 'NO'
assert prisoner(2, 1, 2, 1, 1) == 'NO'
assert prisoner(2, 1, 1, 1, 1) == 'YES'
assert prisoner(2, 8, 5, 5, 2) == 'YES'
assert prisoner(3, 8, 5, 5, 2) == 'NO'
assert prisoner(100, 1, 1, 5, 2) == 'YES'
assert prisoner(1, 1, 1, 5, 2) == 'YES'


def main():
    a, b, c, d, e = [int(input()) for _ in range(5)]
    print(prisoner(a, b, c, d, e))


if __name__ == '__main__':
    main()
