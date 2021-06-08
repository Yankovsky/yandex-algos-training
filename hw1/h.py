def subway(a, b, m, n):
    min_a_time = m + (m - 1) * a
    max_a_time = m + (m + 1) * a
    min_b_time = n + (n - 1) * b
    max_b_time = n + (n + 1) * b
    left = max(min_a_time, min_b_time)
    right = min(max_a_time, max_b_time)
    if left > right:
        return -1
    return ' '.join(map(str, [left, right]))


assert subway(1, 3, 3, 2) == '5 7'
assert subway(1, 5, 1, 2) == -1


def main():
    a, b, m, n = [int(input()) for _ in range(4)]
    print(subway(a, b, m, n))


if __name__ == '__main__':
    main()
