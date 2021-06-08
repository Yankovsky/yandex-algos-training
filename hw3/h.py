def angry_pigs(birds):
    return len(set(map(lambda xy: xy[0], birds)))


assert angry_pigs([(1, 1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 1)]) == 3
assert angry_pigs([(1, 1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 4)]) == 3


def main():
    n = int(input())
    birds = [tuple(map(float, input().split())) for _ in range(n)]
    print(angry_pigs(birds))


if __name__ == '__main__':
    main()
