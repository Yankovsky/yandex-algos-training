def triangle(items):
    freq_min = 30
    freq_max = 4000
    previous = items[0][0]
    for i in range(1, len(items)):
        freq, nearness = items[i]
        closer = nearness == 'closer'
        less_than_previous = freq < previous
        if freq != previous:
            if (closer and less_than_previous) or (not closer and not less_than_previous):
                freq_max = max(freq_min, min((previous + freq) / 2, freq_max))
            else:
                freq_min = min(freq_max, max((previous + freq) / 2, freq_min))

        previous = freq

    return [freq_min, freq_max]


assert triangle([(440, None), (220, 'closer'), (300, 'further')]) == [30.0, 260.0]
assert triangle([(554, None), (880, 'further'), (440, 'closer'), (622, 'closer')]) == [531.0, 660.0]
assert triangle([(2705, None), (117, 'closer'), (3697, 'further'), (1565, 'closer')]) == [30.0, 1411.0]


def main():
    n = int(input())
    input_items = []
    for _ in range(n):
        input_item = input().split()
        input_items.append((float(input_item[0]), input_item[1] if len(input_item) > 1 else None))
    result = triangle(input_items)
    print(f'{result[0]:.6f} {result[1]:.6f}')


if __name__ == '__main__':
    main()
