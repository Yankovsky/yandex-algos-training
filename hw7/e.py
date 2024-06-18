# https://contest.yandex.ru/contest/27883/problems/E/

# Создаём массив размером 1440 (количество минут в день), каждые входные данные со временем
# переводим в минуты и отмечаем в созданном массиве время, когда касса была открыта.


def open_cash_registers(n):
    a = [0] * 1440
    res = 0

    for _ in range(n):
        h1, m1, h2, m2 = map(int, input().split())
        t1 = h1 * 60 + m1
        t2 = h2 * 60 + m2
        if t1 >= t2:
            for j in range(t1, 1440):
                a[j] += 1
            for j in range(t2):
                a[j] += 1
        else:
            for j in range(t1, t2):
                a[j] += 1

    for i in a:
        if i == n:
            res += 1

    return res


def main():
    n = int(input())
    print(open_cash_registers(n))


if __name__ == '__main__':
    main()
