# При рассмотрении каждой новой локации от навигатора ищем пересечение множества позиций,
# на которых может быть Михаил с множеством позиций, на которые может указывать навигатор.
# Медленно, но субъективно красиво.
def manhattan(t, d, positions):
    # Перебор всех возможных позиций для стартовой позиции и отклонения
    def get_possible_positions(start_positions, deviation):
        possible_positions = set()
        for start_x, start_y in start_positions:
            for x in range(-deviation, deviation + 1):
                abs_x = abs(x)
                for y in range(-deviation + abs_x, deviation - abs_x + 1):
                    possible_positions.add((start_x + x, start_y + y))
        return possible_positions

    previous_positions = {(0, 0)}
    for position in positions:
        possible_navigator_positions = get_possible_positions([position], d)
        possible_michael_positions = get_possible_positions(previous_positions, t)
        previous_positions = possible_navigator_positions.intersection(possible_michael_positions)

    return previous_positions


assert manhattan(2, 1, [(0, 1), (-2, 1), (-2, 3), (0, 3), (2, 5)]) == {(1, 5), (2, 4)}
assert manhattan(1, 1, [(0, 0)]) == {(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)}
assert manhattan(1, 10, [(0, 0)]) == {(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)}
assert manhattan(3, 2, [(5, 0)]) == {(3, 0)}


def main():
    t, d, n = map(int, input().split())
    positions = [tuple(map(int, input().split())) for _ in range(n)]
    results = manhattan(t, d, positions)
    print(len(results))
    for result in results:
        print(*result)


if __name__ == '__main__':
    main()
