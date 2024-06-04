# https://contest.yandex.ru/contest/27844/problems/E/

# С помощью бинарного поиска находим предположительное количество оценок "5",
# считаем средний балл и сравниваем с тем, какой он должен быть по условию

def find_quantity_mark(a, b, c):
    left, right = 0, a + b + c
    while left < right:
        middle = (left + right) // 2
        if (2 * a + 3 * b + 4 * c + 5 * middle) * 10 < 35 * (a + b + c + middle):
            left = middle + 1
        else:
            right = middle
    return left


assert find_quantity_mark(2, 0, 0) == 2


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    print(find_quantity_mark(a, b, c))


if __name__ == '__main__':
    main()
