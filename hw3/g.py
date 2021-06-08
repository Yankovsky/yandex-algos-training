def turtles_liars(statements):
    previous_statements = set()
    result = 0
    for statement in statements:
        no_negative_placements = statement[0] >= 0 and statement[1] >= 0
        correct_number_of_turtles = statement[0] + statement[1] + 1 == len(statements)
        if no_negative_placements and correct_number_of_turtles and statement not in previous_statements:
            previous_statements.add(statement)
            result += 1

    return result


assert turtles_liars([(1, 0), (1, 0)]) == 1
assert turtles_liars([(2, 0), (0, 2), (2, 2)]) == 2
assert turtles_liars([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]) == 5
assert turtles_liars([(9, 1), (8, 1), (7, 2), (6, 2), (5, 3), (4, 4), (3, 6), (2, 7), (1, 9), (8, 0)]) == 4


def main():
    n = int(input())
    statements = [tuple(map(int, input().split())) for _ in range(n)]
    print(turtles_liars(statements))


if __name__ == '__main__':
    main()
