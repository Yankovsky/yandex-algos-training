# https://contest.yandex.ru/contest/27844/problems/C/

# с помощью бинарного поиска находим диаметр,
# вычисля максимальное кол-во модулей, которые можем разместить с таким диаметром


def additional_protection(n, a, b, w, h):
    left, right = 0, min(w, h)
    while left + 1 < right:
        d = (left + right) // 2
        x = max((w // (a + 2 * d)) * (h // (b + 2 * d)), (h // (a + 2 * d)) * (w // (b + 2 * d)))
        if x >= n:
            left = d
        else:
            right = d
    return left


assert additional_protection(1, 1, 1, 1, 1) == 0
assert additional_protection(1, 1, 1, 3, 3) == 1
assert additional_protection(11, 3, 2, 21, 25) == 2


def main():
    n, a, b, w, h = map(int, input().split())
    print(additional_protection(n, a, b, w, h))


if __name__ == '__main__':
    main()
