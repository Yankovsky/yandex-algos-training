# https://contest.yandex.ru/contest/27844/problems/F/

# С помощью бинарного поиска находим время,
# высчитываем количество копий, которые можно сделать за это время и сравниваем с условием

def time_to_copy(n, x, y):
    left, right = 0, max(x, y) * n
    while left < right:
        t = (left + right) // 2
        q_copies = t // min(x, y) + ((t - min(x, y)) // max(x, y))
        if q_copies < n:
            left = t + 1
        else:
            right = t
    return left


assert time_to_copy(4, 1, 1) == 3
assert time_to_copy(5, 1, 2) == 4


def main():
    n, x, y = map(int, input().split())
    print(time_to_copy(n, x, y))


if __name__ == '__main__':
    main()
