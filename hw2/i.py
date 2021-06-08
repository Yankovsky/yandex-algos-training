def minesweeper(n, m, mines):
    field = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in mines:
        field[x - 1][y - 1] = '*'
        for i in range(-1, 2):
            for j in range(-1, 2):
                mark_x = x - 1 + i
                mark_y = y - 1 + j
                if 0 <= mark_x < n and 0 <= mark_y < m and field[mark_x][mark_y] != '*':
                    field[mark_x][mark_y] += 1

    return '\n'.join([' '.join(map(str, line)) for line in field])

assert minesweeper(3, 2, [(1,1), (2,2)]) == \
'''* 2
2 *
1 1'''
assert minesweeper(2, 2, []) == \
'''0 0
0 0'''
assert minesweeper(4, 4, [(1, 3), (2, 1), (4, 2), (4, 4)]) == \
'''1 2 * 1
* 2 1 1
2 2 2 1
1 * 2 *'''


def main():
    n, m, mines_count = map(int, input().split())
    mines = [tuple(map(int, input().split())) for _ in range(mines_count)]
    print(minesweeper(n, m, mines))


if __name__ == '__main__':
    main()