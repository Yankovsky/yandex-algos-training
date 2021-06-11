def apps_per_floor(m, k, p, n):
    # Теперь научимся считать q при условии наличия нескольких подъездов.
    # m * (p - 1) – количество этажей во всех предыдущих подъездах кроме подъезда квартиры.
    # Тогда этаж квартиры можно выразить как (m * (p - 1) + n - 1),
    # Можно мысленно преобразовать многоподъездный дом в небоскрёб с одним подъездом.
    # Например, если дом 4-этажный, а квартира находится на 3 этаже 7 подъезда, то можно представить,
    # что квартира находится на 27 (4 * 6 + 3) этаже одноподъездного небоскрёба.
    # Обновим формулу:
    # k - 1 = (m * (p - 1) + n - 1) * q + (k - 1) % q
    # Обновим подсчёт границ:
    # При (k - 1) % q == 0;
    #     k - 1 = (m * (p - 1) + n - 1) * q =>
    #     => q = (k - 1) // (m * (p - 1) + n - 1)
    # При (k - 1) % q == q - 1; k - 1 = (n - 1) * q + q - 1 => q = k // n
    #     k - 1 = (m * (p - 1) + n - 1) * q + q - 1 =>
    #     => q = k // (m * (p - 1) + n)
    #
    # Если (m * (p - 1) + n - 1) равно нулю, то мы не можем определить количество квартир на этаже.
    # Такое может быть, если подъезд первый и этаж первый.
    if p == 1 and n == 1:
        return 0

    bound1 = (k - 1) // (m * (p - 1) + n - 1)
    bound2 = k // (m * (p - 1) + n)
    min_bound = min(bound1, bound2)
    max_bound = max(bound1, bound2)
    possible_qs = []
    for q in range(min_bound, max_bound + 1):
        if q != 0 and (m * (p - 1) + n - 1) * q + (k - 1) % q == k - 1:
            possible_qs.append(q)

    if len(possible_qs) == 0:
        return -1
    elif len(possible_qs) == 1:
        return q
    else:
        return 0


assert apps_per_floor(1, 1, 1, 1) == 0
assert apps_per_floor(20, 1, 1, 1) == 0
assert apps_per_floor(20, 2, 1, 1) == 0
assert apps_per_floor(20, 3, 1, 1) == 0
assert apps_per_floor(20, 4, 1, 1) == 0
assert apps_per_floor(20, 1, 1, 2) == -1
assert apps_per_floor(20, 9, 1, 4) == -1
assert apps_per_floor(20, 10, 1, 4) == 3
assert apps_per_floor(20, 11, 1, 4) == 3
assert apps_per_floor(20, 12, 1, 4) == 3
assert apps_per_floor(20, 13, 1, 4) == 4
assert apps_per_floor(20, 6, 1, 2) == 0  # варианты 3, 4, 5
assert apps_per_floor(20, 2, 1, 2) == 1
assert apps_per_floor(20, 3, 1, 2) == 2
assert apps_per_floor(20, 4, 1, 2) == 0
assert apps_per_floor(20, 5, 1, 2) == 0
assert apps_per_floor(20, 6, 1, 2) == 0
assert apps_per_floor(20, 4, 1, 3) == -1
assert apps_per_floor(20, 7, 1, 4) == 2
assert apps_per_floor(20, 8, 1, 4) == 2
assert apps_per_floor(20, 10, 1, 4) == 3
assert apps_per_floor(20, 11, 1, 4) == 3
assert apps_per_floor(20, 12, 1, 4) == 3
assert apps_per_floor(20, 24, 2, 4) == 1
assert apps_per_floor(20, 25, 2, 5) == 1
assert apps_per_floor(20, 47, 2, 4) == 2
assert apps_per_floor(20, 48, 2, 4) == 2
assert apps_per_floor(20, 41, 1, 11) == 4
assert apps_per_floor(20, 42, 1, 11) == 4
assert apps_per_floor(20, 43, 1, 11) == 4
assert apps_per_floor(20, 44, 1, 11) == 4
assert apps_per_floor(20, 45, 1, 11) == -1
assert apps_per_floor(2, 2, 2, 1) == -1
