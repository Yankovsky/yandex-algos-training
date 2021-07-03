# Здесь реализована идея проверки на вырожденность через set обратных векторов,
# где ключ вектора считается как произведение его координат со сдвигом.
from collections import defaultdict

# Сдвиг для вычисления уникального значения произведения координат вектора.
# Сдвиг именно такой, потому что если его сделать хотя бы на 1 меньше,
# то начнутся коллизии, можно рассмотреть краевой случай (0, 10**9) и (1, -10**9))
SHIFT = 2 * 10 ** 9 + 1


def triangles(points):
    triangles_count = 0
    for (x1, y1) in points:
        opposite_vectors_xy_product = set()
        points_by_distances = defaultdict(int)
        for x2, y2 in points:
            x = x2 - x1
            y = y2 - y1
            squared_distance = x ** 2 + y ** 2

            triangles_count += points_by_distances[squared_distance]

            previous_vectors_xy_product_values = abs(x * SHIFT + y)
            if previous_vectors_xy_product_values in opposite_vectors_xy_product:
                triangles_count -= 1
            else:
                opposite_vectors_xy_product.add(previous_vectors_xy_product_values)

            points_by_distances[squared_distance] += 1

    return triangles_count


assert triangles([(0, 0), (-1, 0), (0, -1), (0, 1), (1, 0)]) == 8
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
