def count_neighbors(nums):
    result = 0
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            result += 1
    return result


assert count_neighbors([1, 2, 3, 4, 5]) == 0
assert count_neighbors([5, 4, 3, 2, 1]) == 0
assert count_neighbors([1, 5, 1, 5, 1]) == 2


def main():
    nums = list(map(int, input().split()))
    print(count_neighbors(nums))


if __name__ == '__main__':
    main()
