# https://contest.yandex.ru/contest/27794/problems/C/

def tourism(points, tracks):
    # Суммарные подъёмы от начала до i слева направо
    prefixes_rises_ltr = [0] + [None] * (len(points) - 1)
    # Суммарные подъёмы от конца до i справа налево
    prefixes_rises_rtl = [None] * (len(points) - 1) + [0]

    for i in range(1, len(points)):
        prefixes_rises_ltr[i] = \
            prefixes_rises_ltr[i - 1] + max(points[i][1] - points[i - 1][1], 0)
        prefixes_rises_rtl[len(points) - i - 1] = \
            prefixes_rises_rtl[len(points) - i] + max(points[len(points) - i - 1][1] - points[len(points) - i][1], 0)

    results = []
    for track in tracks:
        if track[0] < track[1]:
            results.append(prefixes_rises_ltr[track[1] - 1] - prefixes_rises_ltr[track[0] - 1])
        else:
            results.append(prefixes_rises_rtl[track[1] - 1] - prefixes_rises_rtl[track[0] - 1])

    return results


assert tourism([(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)], [(2, 6)]) == [4]
assert tourism(
    [(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)],
    [(1, 4), (1, 5), (2, 6), (2, 7), (1, 7)]
) == [4, 8, 4, 4, 8]
assert tourism(
    [(2, 1), (4, 5), (7, 4), (8, 2), (9, 6), (11, 3), (15, 3)],
    [(4, 1), (5, 1), (6, 2), (7, 2), (7, 1), (6, 3), (5, 3)]
) == [3, 3, 6, 6, 6, 5, 2]
assert tourism([(1, 1), (3, 2), (5, 6), (7, 2), (10, 4), (11, 1)], [(5, 6), (1, 4), (4, 2)]) == [0, 5, 4]


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    tracks = [tuple(map(int, input().split())) for _ in range(m)]
    results = tourism(points, tracks)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
