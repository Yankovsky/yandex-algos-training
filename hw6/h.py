# https://contest.yandex.ru/contest/27844/problems/H/

# С помощью бинарного поиска находим длину отрезков,
# вычисляем суммарное количество отрезков данной длины из всех проводов,
# сравниваем по условию задачи

def length_of_segments(k, segments):
    left, right = 1, 10 ** 9
    while left < right:
        middle = (left + right) // 2
        count = 0
        for s in segments:
            count += s // middle
        if count >= k:
            left = middle + 1
        else:
            right = middle

    return left - 1


assert length_of_segments(11, [802, 743, 457, 539]) == 200
assert length_of_segments(10, [3, 5]) == 0


def main():
    n, k = map(int, input().split())
    segments = [int(input()) for i in range(n)]
    print(length_of_segments(k, segments))


if __name__ == '__main__':
    main()
