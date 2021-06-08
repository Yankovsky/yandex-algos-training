def cubes(colors_a, colors_b):
    set_a = set(colors_a)
    set_b = set(colors_b)
    return list(map(sorted, [set_a & set_b, set_a - set_b, set_b - set_a]))


assert cubes([0, 1, 10, 9], [1, 3, 0]) == [[0, 1], [9, 10], [3]]
assert cubes([1, 2], [2, 3]) == [[2], [1], [3]]
assert cubes([], []) == [[], [], []]


def main():
    n, m = map(int, input().split())
    colors_a = [int(input()) for _ in range(n)]
    colors_b = [int(input()) for _ in range(m)]
    results = cubes(colors_a, colors_b)
    for result in results:
        print(len(result))
        print(*result)


if __name__ == '__main__':
    main()
