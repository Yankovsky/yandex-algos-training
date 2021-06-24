# https://contest.yandex.ru/contest/27844/problems/A/

from bisect import bisect_left


# Для сравнения используем встроенный бинарный поиск
def binary_search_using_builtin(sorted_nums, num):
    i = bisect_left(sorted_nums, num)
    if i != len(sorted_nums) and sorted_nums[i] == num:
        return ('YES')
    else:
        return ('NO')


# Самописный бинарный поиск
def binary_search(sorted_nums, num):
    left = 0
    right = len(sorted_nums)
    while left < right:
        mid = (left + right) // 2
        if sorted_nums[mid] == num:
            return 'YES'
        elif num < sorted_nums[mid]:
            right = mid
        else:
            left = mid + 1
    return 'NO'


def binary_search_for_list(sorted_nums, nums_to_find):
    results = []
    for num in nums_to_find:
        results.append(binary_search(sorted_nums, num))
    return results


assert binary_search_for_list(
    [1, 61, 126, 217, 2876, 6127, 39162, 98126, 712687, 1000000000],
    [100, 6127, 1, 61, 200, -10000, 1, 217, 10000, 1000000000]
) == ['NO', 'YES', 'YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'NO', 'YES']
assert binary_search_for_list(
    [-8, -6, -4, -4, -2, -1, 0, 2, 3, 3],
    [8, 3, -3, -2, 2, -1, 2, 9, -8, 0]
) == ['NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'YES', 'NO', 'YES', 'YES']
assert binary_search_for_list(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [-2, 0, 4, 9, 12]
) == ['NO', 'NO', 'YES', 'YES', 'NO']


def main():
    n, k = map(int, input().split())
    sorted_nums = list(map(int, input().split()))
    nums_to_find = map(int, input().split())
    results = binary_search_for_list(sorted_nums, nums_to_find)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
