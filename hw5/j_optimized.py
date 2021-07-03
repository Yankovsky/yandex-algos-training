# То же самое решение, что и в j.py, но с меньшим количеством временных структур и циклов,
# более сложное для понимания и чтения.
from collections import defaultdict


def get_squared_distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def triangles(points):
    triangles_count = 0
    for first_idx, first_point in enumerate(points):
        points_by_distances = defaultdict(list)
        for second_idx, second_point in enumerate(points):
            if first_idx == second_idx:
                continue

            squared_distance = get_squared_distance(first_point, second_point)

            for previous_point in points_by_distances[squared_distance]:
                if 4 * squared_distance > get_squared_distance(previous_point, second_point):
                    triangles_count += 1

            points_by_distances[squared_distance].append(second_point)

    return triangles_count


assert triangles([(0, 0), (2, 2), (-2, 2)]) == 1
assert triangles([(0, 0), (2, 2), (-2, -2)]) == 0
assert triangles([(0, 0), (1, 1), (1, 0), (0, 1)]) == 4
assert triangles([(0, 0), (1, 1), (0, 1), (1, 0), (0, -1)]) == 6


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(triangles(points))


if __name__ == '__main__':
    main()
