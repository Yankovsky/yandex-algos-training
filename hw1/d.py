def equation(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if c ** 2 == b:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    x = (c ** 2 - b) / a
    if x.is_integer():
        return int(x)
    else:
        return 'NO SOLUTION'

assert equation(0, 0, 0) == 'MANY SOLUTIONS'
assert equation(1, 0, 0) == 0
assert equation(1, 2, 3) == 7
assert equation(3, 13, 7) == 12
assert equation(0, 0, 5) == 'NO SOLUTION'
assert equation(0, 4, 2) == 'MANY SOLUTIONS'
assert equation(0, 2, 2) == 'NO SOLUTION'
assert equation(1, 2, -3) == 'NO SOLUTION'
assert equation(2, 2, 3) == 'NO SOLUTION'


def main():
    a, b, c = [int(input()) for _ in range(3)]
    print(equation(a, b, c))


if __name__ == '__main__':
    main()
