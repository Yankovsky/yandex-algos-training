# Улучшим перебор возможных положений на каждом шаге итерации.
# Сначала определим возможные значения x для новых положений,
# а затем используя остатки от прохода до этих значений x определим возможные значения y.

def manhattan_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + abs(pos_a[1] - pos_b[1])


def manhattan(t, d, positions):
    previous_positions = {(0, 0)}
    for navigator_position in positions:
        possible_positions = set()
        for previous_position in previous_positions:
            distance = manhattan_distance(navigator_position, previous_position)
            if distance <= d + t:
                min_x_pos = max(navigator_position[0] - d, previous_position[0] - t)
                max_x_pos = min(navigator_position[0] + d, previous_position[0] + t)
                for x in range(min_x_pos, max_x_pos + 1):
                    # оставшееся расстояние после прохождения по прямой до координаты x
                    # это расстояние будет использовано для определения возможных y координат
                    leftover_a = d - abs(navigator_position[0] - x)
                    leftover_b = t - abs(previous_position[0] - x)
                    min_y_pos = max(navigator_position[1] - leftover_a, previous_position[1] - leftover_b)
                    max_y_pos = min(navigator_position[1] + leftover_a, previous_position[1] + leftover_b)
                    for y in range(min_y_pos, max_y_pos + 1):
                        possible_positions.add((x, y))

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
assert manhattan(40, 23, [
    (6, -25), (-15, -54), (13, -19), (2, -39), (-38, -31),
    (-61, -53), (-88, -59), (-46, -67), (-32, -52), (-52, -47),
    (-43, -57), (-57, -48), (-3, -64), (-4, -43), (13, -35),
    (44, -16), (44, -46), (41, -58), (15, -46), (5, -67),
    (17, -64), (23, -87), (59, -71), (30, -85), (93, -87)
]) == \
       {
           (79, -95), (76, -85), (79, -86), (81, -89), (88, -83),
           (82, -90), (90, -86), (81, -80), (82, -81), (73, -84),
           (84, -87), (86, -90), (77, -93), (78, -94), (80, -97),
           (86, -81), (77, -84), (87, -82), (78, -85), (80, -88),
           (83, -89), (84, -78), (89, -85), (92, -86), (80, -79),
           (75, -84), (93, -85), (76, -92), (79, -93), (81, -96),
           (88, -90), (85, -80), (76, -83), (79, -84), (81, -87),
           (88, -81), (71, -88), (82, -88), (90, -84), (82, -79),
           (84, -94), (84, -85), (86, -88), (77, -91), (78, -92),
           (80, -95), (86, -79), (77, -82), (87, -80), (78, -83),
           (80, -86), (84, -76), (70, -87), (89, -83), (75, -91),
           (80, -77), (92, -84), (74, -87), (76, -90), (79, -91),
           (81, -94), (83, -75), (82, -95), (76, -81), (79, -82),
           (85, -78), (88, -88), (71, -86), (73, -89), (82, -86),
           (90, -82), (84, -92), (82, -77), (72, -85), (84, -83),
           (77, -89), (86, -86), (78, -90), (80, -93), (87, -87),
           (77, -80), (78, -81), (80, -84), (89, -81), (74, -85),
           (76, -88), (79, -89), (85, -85), (88, -86), (82, -93),
           (82, -84), (84, -90), (84, -81), (86, -84), (77, -87),
           (87, -85), (78, -88), (80, -91), (89, -88), (78, -79),
           (80, -82), (91, -85), (85, -92), (79, -96), (83, -80),
           (74, -83), (76, -86), (85, -83), (88, -84), (82, -91),
           (84, -88), (86, -91), (77, -94), (78, -95), (81, -78),
           (84, -79), (86, -82), (87, -83), (78, -86), (80, -89),
           (89, -86), (91, -83), (83, -87), (74, -90), (76, -93),
           (85, -90), (83, -78), (85, -81), (76, -84), (75, -82),
           (88, -82), (82, -89), (81, -85), (72, -88), (84, -86),
           (86, -89), (87, -90), (78, -93), (80, -96), (81, -76),
           (84, -77), (86, -80), (78, -84), (80, -87), (87, -81),
           (89, -84), (83, -94), (83, -85), (74, -88), (76, -91),
           (75, -89), (85, -88), (83, -76), (82, -96), (76, -82),
           (85, -79), (88, -89), (81, -92), (84, -93), (79, -80),
           (81, -83), (72, -86), (84, -84), (73, -87), (86, -87),
           (78, -91), (80, -94), (82, -75), (87, -88), (87, -79),
           (78, -82), (89, -82), (83, -92), (83, -83), (74, -86),
           (76, -89), (75, -87), (85, -86), (85, -77), (79, -87),
           (81, -90), (84, -91), (90, -87), (79, -78), (81, -81),
           (84, -82), (82, -82), (73, -85), (87, -86), (78, -89),
           (89, -89), (77, -85), (91, -86), (83, -90), (85, -93),
           (80, -80), (83, -81), (74, -84), (76, -87), (75, -85),
           (85, -84), (79, -94), (81, -97), (79, -85), (81, -88),
           (84, -89), (90, -85), (81, -79), (82, -80), (87, -84),
           (77, -92), (77, -83), (91, -84), (92, -85), (83, -88),
           (74, -91), (85, -91), (75, -92), (80, -78), (83, -79),
           (85, -82), (75, -83), (79, -92), (81, -95), (88, -80),
           (79, -83), (81, -86), (72, -89), (71, -87), (73, -90),
           (82, -87), (81, -77), (87, -91), (82, -78), (90, -83),
           (77, -90), (83, -95), (77, -81), (86, -78), (80, -85),
           (83, -86), (74, -89), (85, -89), (75, -90), (83, -77),
           (88, -87), (79, -90), (81, -93), (82, -94), (79, -81),
           (81, -84), (72, -87), (82, -85), (73, -88), (87, -89),
           (82, -76), (86, -85), (77, -88), (80, -92), (83, -93),
           (78, -80), (80, -83), (83, -84), (85, -87), (75, -88),
           (88, -85), (79, -88), (81, -91), (90, -88), (82, -92),
           (79, -79), (81, -82), (82, -83), (73, -86), (86, -92),
           (84, -80), (86, -83), (77, -86), (91, -87), (78, -87),
           (80, -90), (83, -91), (89, -87), (80, -81), (83, -82),
           (75, -86)
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
