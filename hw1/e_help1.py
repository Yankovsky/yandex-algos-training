def apps_per_floor(k, n):
    # q – количество квартир на этаже.

    # Отметим особый случай: если этаж первый, то невозможно определить количество квартир на этаже.
    if n == 1:
        return 0

    # Для наглядности, рассмотрим случай без подъездов:
    # (n - 1) * q – количество квартир на всех предыдущих этажах кроме этажа квартиры.
    # (k - 1) % q – порядковый номер квартиры на её этаже, номер начинается с нуля.
    # Например, если квартир на этаже 3, то квартира с номером 1 будет нулевой на этаже,
    # а квартира с номером 2 будет первой на этаже.
    # теперь можно выразить порядковый номер квартиры как:
    # k - 1 = (n - 1) * q + (k - 1) % q
    # q – неизвестно, но мы попробуем определить границы его возможных значений.
    # Заметим, что k % q изменяется от 0 до q - 1, используем эти граничные значения для определения границ q.
    # Также, отметим, что q – целое число, большее нуля.
    # При (k - 1) % q == 0:
    #     k - 1 = (n - 1) * q =>
    #     => q = (k - 1) // (n - 1)
    # При (k - 1) % q == q - 1:
    #     k - 1 = (n - 1) * q + q - 1 =>
    #     => q = k // n
    max_bound = (k - 1) // (n - 1)
    min_bound = k // n

    # Проверим все возможные значения q на найденном промежутке, подставив q в формулу,
    # посчитаем количество подходящих q.
    # Если (количество подходящих q) == 0, то значит, что данные противоречивы, вернём -1.
    # Если (количество подходящих q) == 1, то значит, что есть точное количество квартир на этаже, вернём q.
    # Если (количество подходящих q) > 1, то значит, что невозможно однозначно его определить.
    possible_qs = []
    for q in range(min_bound, max_bound + 1):
        if q != 0 and (n - 1) * q + (k - 1) % q == k - 1:
            possible_qs.append(q)

    if len(possible_qs) == 0:
        return -1
    elif len(possible_qs) == 1:
        return q
    else:
        return 0

assert apps_per_floor(1, 1) == 0
assert apps_per_floor(2, 1) == 0
assert apps_per_floor(3, 1) == 0
assert apps_per_floor(4, 1) == 0
assert apps_per_floor(1, 2) == -1
assert apps_per_floor(9, 4) == -1
assert apps_per_floor(10, 4) == 3
assert apps_per_floor(11, 4) == 3
assert apps_per_floor(12, 4) == 3
assert apps_per_floor(13, 4) == 4
assert apps_per_floor(6, 2) == 0  # варианты 3, 4, 5
assert apps_per_floor(2, 2) == 1
assert apps_per_floor(3, 2) == 2
assert apps_per_floor(4, 2) == 0
assert apps_per_floor(5, 2) == 0
assert apps_per_floor(6, 2) == 0
assert apps_per_floor(4, 3) == -1
assert apps_per_floor(7, 4) == 2
assert apps_per_floor(8, 4) == 2
assert apps_per_floor(10, 4) == 3
assert apps_per_floor(11, 4) == 3
assert apps_per_floor(12, 4) == 3
assert apps_per_floor(41, 11) == 4
assert apps_per_floor(42, 11) == 4
assert apps_per_floor(43, 11) == 4
assert apps_per_floor(44, 11) == 4
assert apps_per_floor(45, 11) == -1

