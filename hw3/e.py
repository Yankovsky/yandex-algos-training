def open_calculator(buttons, num):
    buttons_set = set(map(str, buttons))
    missing_counter = 0
    for digit in str(num):
        if digit not in buttons_set:
            missing_counter += 1
            buttons_set.add(digit)
    return missing_counter


assert open_calculator([1, 2, 3], 1123) == 0
assert open_calculator([1, 2, 3], 1001) == 1
assert open_calculator([5, 7, 3], 123) == 2


def main():
    buttons = map(int, input().split())
    num = int(input())
    print(open_calculator(buttons, num))


if __name__ == '__main__':
    main()
