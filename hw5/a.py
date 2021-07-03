# https://contest.yandex.ru/contest/27794/problems/A/

import math


def stylish_look(a, b):
    i = 0
    j = 0
    best_i = 0
    best_j = 0
    best_result = math.inf

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return a[i], b[j]

        new_result = abs(b[j] - a[i])
        if new_result < best_result:
            best_i = i
            best_j = j
            best_result = new_result

        if a[i] > b[j]:
            j += 1
        else:
            i += 1

    return a[best_i], b[best_j]


assert stylish_look([3, 4], [1, 2, 3]) == (3, 3)
assert stylish_look([4, 5], [1, 2, 3]) == (4, 3)
assert stylish_look([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == (1, 1)
assert stylish_look([1], [10]) == (1, 10)
assert stylish_look([10], [1]) == (10, 1)
assert stylish_look([5], [5]) == (5, 5)
assert stylish_look([1, 3, 5, 7, 10], [2, 4, 6, 8, 12]) == (1, 2)
assert stylish_look([1, 2, 1000], [3, 4]) == (2, 3)
assert stylish_look([1, 2, 1000, 1010], [3, 4, 1000, 1020]) == (1000, 1000)


def main():
    n = int(input())
    shirts = list(map(int, input().split()))
    m = int(input())
    pants = list(map(int, input().split()))
    print(*stylish_look(shirts, pants))


if __name__ == '__main__':
    main()
