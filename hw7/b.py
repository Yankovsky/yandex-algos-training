# https://contest.yandex.ru/contest/27883/problems/B/
#
# Создадим массив событий, в который войдут начала отрезков, концы отрезков и точки.
# Отсортируем этот массив.
# Пройдём по всем событиям, поддерживая количество отрезков в текущей точке.
# Учтём, что надо вывести результаты в исходном порядке точек.
#
# Сложность сортировки O((N+M)*log(N+M)), цикл O(N+M).
# Итоговая асимптотика O((N+M)*log(N+M)).

def point_inclusions_count(segments, points):
    events = []
    SEGMENT_START = -1
    SEGMENT_END = 1
    POINT = 0
    for segment in segments:
        sorted_segment = sorted(segment)
        events.append((sorted_segment[0], SEGMENT_START))
        events.append((sorted_segment[1], SEGMENT_END))
    for i, point in enumerate(points):
        events.append((point, POINT, i))
    sorted_events = sorted(events)

    results = [None] * len(points)
    current_segments_count = 0
    for event in sorted_events:
        event_type = event[1]
        if event_type == SEGMENT_START:
            current_segments_count += 1
        elif event_type == SEGMENT_END:
            current_segments_count -= 1
        elif event_type == POINT:
            idx = event[2]
            results[idx] = current_segments_count

    return results


assert point_inclusions_count([[0, 5], [-3, 2], [7, 10]], [1, 6]) == [2, 0]
assert point_inclusions_count([[5, 0], [2, -3], [10, 7]], [6, 1]) == [0, 2]


def main():
    n, m = map(int, input().split())
    segments = [list(map(int, input().split())) for _ in range(n)]
    points = list(map(int, input().split()))
    print(*point_inclusions_count(segments, points))


if __name__ == '__main__':
    main()
