# Несколько оптимизаций по сравнению с наивным решением:
# 1. Если манхэттенское расстояние между возможной предыдущей позицией Михаила и локацией навигатора
#    больше, чем сумма отклонений (d + t), то можем эту возможную предыдущую позицию исключить из рассчётов.
# 2. Для получения новых возможных позиций итерируемся сначала по показателю
#    с наименьшим отклонением (сравниваем d и t), затем от него считаем манхэттенское расстояние
#    и сравниваем со вторым отклонением.
# Работает быстрее, чем наивное решение, но всё равно очень медленно.

def manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def get_possible_positions(pos_a, pos_b, deviation_a, deviation_b):
    positions = set()
    for x in range(-deviation_a, deviation_a + 1):
        abs_x = abs(x)
        for y in range(-deviation_a + abs_x, deviation_a - abs_x + 1):
            new_position = (pos_a[0] + x, pos_a[1] + y)
            if manhattan_distance(new_position, pos_b) <= deviation_b:
                positions.add(new_position)

    return positions


def manhattan(t, d, positions):
    previous_positions = {(0, 0)}
    for navigator_position in positions:
        possible_positions = set()
        for previous_position in previous_positions:
            distance = manhattan_distance(navigator_position, previous_position)
            if distance <= d + t:
                if d < t:
                    new_possible_positions = get_possible_positions(navigator_position, previous_position, d, t)
                else:
                    new_possible_positions = get_possible_positions(previous_position, navigator_position, t, d)
                possible_positions.update(new_possible_positions)

        previous_positions = possible_positions

    return previous_positions


assert manhattan(2, 1, [(0, 1), (-2, 1), (-2, 3), (0, 3), (2, 5)]) == {(1, 5), (2, 4)}
assert manhattan(1, 1, [(0, 0)]) == {(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)}
assert manhattan(1, 10, [(0, 0)]) == {(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)}
assert manhattan(3, 2, [(5, 0)]) == {(3, 0)}
assert manhattan(45, 49, [(-31, -7), (-16, -117)]) == \
       {
           (-14, -76), (-14, -73), (-14, -70), (-8, -78), (-9, -77),
           (-15, -71), (-17, -69), (-7, -77), (-18, -71), (-17, -72),
           (-15, -75), (-15, -69), (-12, -76), (-16, -71), (-15, -72),
           (-12, -73), (-10, -76), (-11, -78), (-16, -68), (-10, -79),
           (-13, -75), (-11, -75), (-13, -72), (-14, -74), (-14, -71),
           (-8, -76), (-9, -78), (-9, -75), (-18, -72), (-17, -73),
           (-16, -72), (-17, -70), (-15, -73), (-16, -69), (-11, -79),
           (-15, -70), (-12, -77), (-13, -73), (-10, -74), (-11, -76),
           (-10, -77), (-13, -76), (-12, -74), (-10, -80), (-11, -73),
           (-19, -71), (-14, -75), (-9, -79), (-14, -72), (-9, -76),
           (-8, -77), (-16, -74), (-17, -71), (-15, -74), (-12, -78),
           (-16, -73), (-18, -70), (-13, -74), (-12, -75), (-10, -78),
           (-13, -71), (-16, -70), (-11, -74), (-10, -75), (-11, -77),
           (-13, -77), (-12, -72)
       }


def main():
    t, d, n = map(int, input().split())
    positions = [tuple(map(int, input().split())) for _ in range(n)]
    results = manhattan(t, d, positions)
    print(len(results))
    for result in results:
        print(*result)


if __name__ == '__main__':
    main()
