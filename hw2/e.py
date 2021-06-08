def championship(throws):
    winner_throw = throws[0]
    winner_was_before = True
    vasya_best_throw = None
    for i in range(1, len(throws) - 1):
        throw = throws[i]
        if throw > winner_throw:
            winner_throw = throw
            winner_was_before = True
            vasya_best_throw = None
        else:
            if winner_was_before:
                if throw % 10 == 5 and throws[i + 1] < throw:
                    if not vasya_best_throw or vasya_best_throw < throw:
                        vasya_best_throw = throw

    if not vasya_best_throw:
        return 0

    vasya_best_placement = 1
    for throw in throws:
        if throw > vasya_best_throw:
            vasya_best_placement += 1

    return vasya_best_placement


assert championship([10, 20, 15, 10, 30, 5, 1]) == 6
assert championship([15, 15, 10]) == 1
assert championship([10, 15, 20]) == 0
assert championship([555, 76, 661, 478, 889, 453, 555, 359, 601, 835]) == 5

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    print(championship(nums))


if __name__ == '__main__':
    main()
