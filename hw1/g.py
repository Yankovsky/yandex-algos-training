def details(n, k, m):
    details_per_bar = k // m
    if details_per_bar == 0:
        return 0
    details_weight_for_one_bar = details_per_bar * m

    details_count = 0
    while n >= k:
        bars_count = n // k
        n -= bars_count * details_weight_for_one_bar
        details_count += bars_count * details_per_bar

    return details_count


assert details(5, 2, 1) == 4
assert details(5, 3, 1) == 3
assert details(164, 5, 3) == 54
assert details(1, 1, 2) == 0
assert details(10, 5, 2) == 4
assert details(13, 5, 3) == 3
assert details(14, 5, 3) == 4


def main():
    n, k, m = map(int, input().split())
    print(details(n, k, m))


if __name__ == '__main__':
    main()
