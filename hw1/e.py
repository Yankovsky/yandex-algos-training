# Далее в задаче q – количество квартир на этаже.
# Подробное описание откуда получена формула и границы для q в соседних файлах e_help
# Формула для референса:
# k - 1 = (n - 1) * q + (k - 1) % q


def apps_per_floor(m, k, p, n):
    bound1 = (k - 1) // (m * (p - 1) + n - 1)
    bound2 = k // (m * (p - 1) + n)
    min_bound = min(bound1, bound2)
    max_bound = max(bound1, bound2)
    possible_qs = []
    for q in range(min_bound, max_bound + 1):
        if q != 0 and (m * (p - 1) + n - 1) * q + (k - 1) % q == k - 1:
            possible_qs.append(q)

    return possible_qs


def emergency(k1, m, k2, p2, n2):
    # Если этаж второй квартиры больше, чем всего этажей в здании, вернуть [-1, -1]
    if not (0 <= n2 <= m):
        return [-1, -1]

    # Отдельно рассматриваем случай, когда для второй квартиры подъезд первый и этаж первый
    if p2 == 1 and n2 == 1:
        # Если k1 <= k2, то можно точно сказать, что k1 в первом подъезде на первом этаже
        if k1 <= k2:
            return [1, 1]
        else:
            # Если k1 > k2, то необходимо рассмотреть возможные значения q.
            # q может быть в промежутке от k2 включительно и до +∞.
            # Заметим, что на самом деле перебирать все значения до +∞ необязательно,
            # достаточно дойти до k1 включительно.
            # Если брать q большие или равные k1,
            # то для них всегда будет получаться, что подъезд и этаж первой квартиры равны 1.
            # Это следует из формулы подсчёта floor_index ниже,
            # конкретно (k1 - 1 - (k1 - 1) % q) == 0 при q >= k1.
            # Нам достаточно проверить только одно такое решение, конкретно q = k1,
            # чтобы понять точно ли определены p1 и n1.
            possible_qs = range(k2, k1 + 1)
    else:
        possible_qs = apps_per_floor(m, k2, p2, n2)

    result = [-1, -1]
    for q in possible_qs:
        # Преобразуем формулу: m * (p - 1) + n = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        # floor_index – это левая часть m * (p - 1) + n
        floor_index = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        n1 = floor_index % m
        p1 = ((floor_index - n1) / m) + 1
        # Если оказалось, что квартира на нулевом этаже,
        # то берём последний этаж предыдущего подъезда
        if n1 == 0:
            n1 = m
            p1 -= 1
        if result == [-1, -1]:
            result = [p1, n1]
        else:
            # Если для разных q, существует более одного значения подъезда или этажа, то значит,
            # что определить подъезд или этаж нельзя, ответ 0.
            if p1 != result[0]:
                result[0] = 0
            if n1 != result[1]:
                result[1] = 0

    return list(map(int, result))


assert emergency(89, 20, 41, 1, 11) == [2, 3]
assert emergency(11, 1, 1, 1, 1) == [0, 1]
assert emergency(3, 2, 2, 2, 1) == [-1, -1]
assert emergency(16, 2, 15, 2, 1) == [2, 0]
assert emergency(17, 2, 15, 2, 1) == [2, 0]
assert emergency(18, 2, 15, 2, 1) == [2, 0]
assert emergency(19, 2, 15, 2, 1) == [2, 0]
assert emergency(20, 2, 15, 2, 1) == [2, 0]
assert emergency(21, 2, 15, 2, 1) == [0, 0]
assert emergency(22, 2, 15, 2, 1) == [0, 0]
assert emergency(23, 2, 15, 2, 1) == [0, 0]
assert emergency(24, 2, 15, 2, 1) == [0, 0]
assert emergency(25, 2, 15, 2, 1) == [0, 0]
assert emergency(26, 2, 15, 2, 1) == [0, 0]
assert emergency(27, 2, 15, 2, 1) == [0, 0]
assert emergency(28, 2, 15, 2, 1) == [0, 0]
assert emergency(29, 2, 15, 2, 1) == [3, 0]
assert emergency(5, 20, 2, 1, 1) == [1, 0]
assert emergency(20, 20, 2, 1, 1) == [1, 0]
assert emergency(21, 20, 2, 1, 1) == [1, 0]
assert emergency(753, 10, 1000, 1, 1) == [1, 1]
assert emergency(10, 3, 50, 1, 50) == [-1, -1]
assert emergency(25, 3, 1, 1, 1) == [0, 0]
assert emergency(25, 3, 1, 1, 1) == [0, 0]
assert emergency(24, 3, 1, 1, 1) == [0, 0]
assert emergency(23, 3, 1, 1, 1) == [0, 0]
assert emergency(22, 3, 1, 1, 1) == [0, 0]
assert emergency(21, 3, 1, 1, 1) == [0, 0]
assert emergency(20, 3, 1, 1, 1) == [0, 0]
assert emergency(19, 3, 1, 1, 1) == [0, 0]
assert emergency(18, 3, 1, 1, 1) == [0, 0]
assert emergency(17, 3, 1, 1, 1) == [0, 0]
assert emergency(16, 3, 1, 1, 1) == [0, 0]
assert emergency(15, 3, 1, 1, 1) == [0, 0]
assert emergency(19, 3, 8, 1, 1) == [1, 0]
assert emergency(19, 3, 7, 1, 1) == [1, 0]
assert emergency(19, 3, 6, 1, 1) == [0, 0]
assert emergency(18, 3, 6, 1, 1) == [1, 0]
assert emergency(6, 3, 18, 1, 1) == [1, 1]
assert emergency(3, 1, 9, 7, 3) == [-1, -1]
assert emergency(3, 1, 2, 1, 1) == [0, 1]
assert emergency(2, 1, 1, 1, 1) == [0, 1]
assert emergency(3, 2, 2, 1, 1) == [1, 0]
assert emergency(2, 3, 1, 1, 1) == [1, 0]


# from random import randint
#
#
# def randomized_testing():
#     N = 1000000
#     for tests_count in range(N):
#         k1, m, k2, p2, n2 = [randint(1, 3) for _ in range(5)]
#         if emergency(k1, m, k2, p2, n2) != etalon(k1, m, k2, p2, n2):
#             print('fail', k1, m, k2, p2, n2)
#     for tests_count in range(N):
#         k1, m, k2, p2, n2 = [randint(1, 1_000_000) for _ in range(5)]
#         if emergency(k1, m, k2, p2, n2) != etalon(k1, m, k2, p2, n2):
#             print('fail', k1, m, k2, p2, n2)
#
#     print('ok')
#
# randomized_testing()

def main():
    k1, m, k2, p2, n2 = map(int, input().split())
    print(*emergency(k1, m, k2, p2, n2))


if __name__ == '__main__':
    main()
