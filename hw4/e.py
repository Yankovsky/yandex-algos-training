def pyramid(sizes):
    pyramid_blocks = {}
    for width, height in sizes:
        if width not in pyramid_blocks or pyramid_blocks[width] < height:
            pyramid_blocks[width] = height

    return sum(pyramid_blocks.values())


assert pyramid([(3, 1), (2, 2), (3, 3)]) == 5


def main():
    n = int(input())
    sizes = [tuple(map(int, input().split())) for _ in range(n)]
    print(pyramid(sizes))


if __name__ == '__main__':
    main()
