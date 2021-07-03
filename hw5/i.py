# https://contest.yandex.ru/contest/27794/problems/I/

# Специальный символ для окончания итерации.
# Так как у робота команды заданы латинскими строчными буквами,
# то можно использовать любой другой символ и быть уверенным,
# что он не встретится в списке операций.
# Мы увеличиваем последовательность на один символ, зато избавляемся
# от проверки не вышли ли мы за пределы массива на каждом шаге итерации.
STOP_SYMBOL = '!'


def robot(k, ops):
    result = 0
    ops += STOP_SYMBOL
    successful_ops_count = 0
    for right in range(k, len(ops)):
        if ops[right] == ops[right - k]:
            successful_ops_count += 1
        else:
            result += ((successful_ops_count + 1) / 2) * successful_ops_count
            successful_ops_count = 0

    return int(result)


assert robot(2, 'zabacabab') == 5
assert robot(3, 'abcabcabc') == 21
assert robot(3, 'abcabcabcbb') == 22
assert robot(2, 'abc') == 0


def main():
    k = int(input())
    ops = input()
    print(robot(k, ops))


if __name__ == '__main__':
    main()
