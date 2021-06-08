def conditioner(t_room, t_cond, mode):
    if mode == 'auto' or (t_room < t_cond and mode == 'heat') or (t_room > t_cond and mode == 'freeze'):
        return t_cond
    return t_room


assert conditioner(10, 20, 'heat') == 20
assert conditioner(10, 20, 'freeze') == 10


def main():
    t_room, t_cond = map(int, input().split())
    mode = input()
    print(conditioner(t_room, t_cond, mode))


if __name__ == '__main__':
    main()
