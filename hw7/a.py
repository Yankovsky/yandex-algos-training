# https://contest.yandex.ru/contest/27883/problems/A/
#
# Воспользуемся методом сканирующей прямой (или по-другому сортировкой событий).
# Заметим, что нам необязательно проверять находится ли каждый студент под наблюдением.
# Можно взять общее количество студентов за исходное количество студентов без наблюдения,
# и затем проходя по всем событиям уменьшать это количество на количество наблюдаемых студентов
# на отрезке. При это надо учесть, что если несколько преподавателей следят за одним студентом,
# то вычесть его из общего числа надо только один раз.
#
# Асимптотика – O(M*log(M))

def students_observation(n, observed_desks):
    events = []
    SEGMENT_START = -1
    SEGMENT_END = 1
    for start, end in observed_desks:
        events.append((start, SEGMENT_START))
        events.append((end, SEGMENT_END))
    sorted_events = sorted(events)

    result = n
    left = None
    current_segments_count = 0
    for coordinate, event_type in sorted_events:
        if event_type == SEGMENT_START:
            if current_segments_count == 0:
                left = coordinate
            current_segments_count += 1
        elif event_type == SEGMENT_END:
            current_segments_count -= 1
            if current_segments_count == 0:
                result -= (coordinate - left + 1)

    return result


assert students_observation(10, [[1, 3], [2, 4], [9, 9]]) == 5
assert students_observation(10, [[1, 1], [1, 2]]) == 8


def main():
    n, m = map(int, input().split())
    observed_desks = [map(int, input().split()) for _ in range(m)]
    print(students_observation(n, observed_desks))


if __name__ == '__main__':
    main()
