def statues(r, distances):
    result = 0
    right = 1
    for left_distance in distances:
        while right < len(distances) and distances[right] - left_distance <= r:
            right += 1
        result += len(distances) - right

    return result


assert statues(4, [1, 3, 5, 8]) == 2
assert statues(4, [1, 3, 5, 8, 9]) == 4
assert statues(4, [1, 3, 5, 8, 10]) == 5
assert statues(4, [1, 1, 1, 1, 2, 3, 4, 4, 4, 4]) == 0
assert statues(4, [1, 100, 200]) == 3


def main():
    n, r = map(int, input().split())
    distances = list(map(int, input().split()))
    print(statues(r, distances))


if __name__ == '__main__':
    main()
