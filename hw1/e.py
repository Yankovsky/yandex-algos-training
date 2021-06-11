def apps_per_floor(m, k, p, n):
    if p == 1 and n == 1:
        return range(k, k + m + 1)
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
    # Если этаж больше, чем всего этажей в здании, вернуть [-1, -1]
    if not (0 <= n2 <= m):
        return [-1, -1]

    possible_qs = apps_per_floor(m, k2, p2, n2)

    if len(possible_qs) == 0:
        return [-1, -1]
    elif len(possible_qs) == 1:
        q = possible_qs[0]
        # Преобразуем формулу: m * (p - 1) + n = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        # floor_index = m * (p - 1) + n
        floor_index = ((k1 - 1 - (k1 - 1) % q) / q) + 1
        n1 = floor_index % m
        p1 = ((floor_index - n1) / m) + 1
        if n1 == 0:
            n1 = m
            p1 -= 1
        return [int(p1), int(n1)]
    else:
        result_n = None
        result_p = None
        for q in possible_qs:
            floor_index = ((k1 - 1 - (k1 - 1) % q) / q) + 1
            n1 = floor_index % m
            p1 = ((floor_index - n1) / m) + 1
            if n1 == 0:
                n1 = m
                p1 -= 1
            if result_p is None:
                result_p = p1
            elif p1 != result_p:
                result_p = 0
            if result_n is None:
                result_n = n1
            elif n1 != result_n:
                result_n = 0

        return [int(result_p), int(result_n)]


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


def main():
    k1, m, k2, p2, n2 = map(int, input().split())
    print(*emergency(k1, m, k2, p2, n2))


if __name__ == '__main__':
    main()
