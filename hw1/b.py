def triangle(a, b, c):
    return 'YES' if (a < b + c) and (b < a + c) and (c < a + b) else 'NO'


assert triangle(3, 4, 5) == 'YES'
assert triangle(3, 5, 4) == 'YES'
assert triangle(4, 5, 3) == 'YES'
assert triangle(4, 7, 3) == 'NO'


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(triangle(a, b, c))


if __name__ == '__main__':
    main()
