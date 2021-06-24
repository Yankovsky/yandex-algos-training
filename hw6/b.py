# https://contest.yandex.ru/contest/27844/problems/B/
#
# Делаем двоичный поиск как обычно,
# в конце сравниваем последний полученный индекс и левый от него.
# Искомое число будет между этими двумя числами.

def nearest_value(sorted_nums, num):
    left = 0
    right = len(sorted_nums)
    while left < right:
        mid = (left + right) // 2
        if sorted_nums[mid] == num:
            return sorted_nums[mid]
        elif num < sorted_nums[mid]:
            right = mid
        else:
            left = mid + 1

    if left != len(sorted_nums) and (left == 0 or abs(sorted_nums[left] - num) < abs(sorted_nums[left - 1] - num)):
        return sorted_nums[left]
    return sorted_nums[left - 1]


def nearest_value_for_list(sorted_nums, nums_to_find):
    results = []
    for num in nums_to_find:
        results.append(nearest_value(sorted_nums, num))
    return results


assert nearest_value_for_list(
    [1, 3, 5, 7, 9],
    [2, 4, 8, 1, 6],
) == [1, 3, 7, 1, 5]
assert nearest_value_for_list(
    [1, 3, 5, 7, 9],
    [0, 1, 2, 4, 6, 8, 9, 10],
) == [1, 1, 1, 3, 5, 7, 9, 9]
assert nearest_value_for_list(
    [1, 1, 4, 4, 8, 120],
    [1, 2, 3, 4, 5, 6, 7, 8, 63, 64, 65],
) == [1, 1, 4, 4, 4, 4, 8, 8, 8, 8, 120]
assert nearest_value_for_list(
    [-5, 1, 1, 3, 5, 5, 8, 12, 13, 16],
    [0, 3, 7, -17, 23, 11, 0, 11, 15, 7],
) == [1, 3, 8, -5, 16, 12, 1, 12, 16, 8]


def main():
    n, k = map(int, input().split())
    sorted_nums = list(map(int, input().split()))
    nums_to_find = map(int, input().split())
    results = nearest_value_for_list(sorted_nums, nums_to_find)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
