def numbers_sum(k, nums):
    result = 0
    left = 0
    current_sum = 0
    for right, num in enumerate(nums):
        current_sum += num
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            result += 1

    return result


assert numbers_sum(17, [17, 7, 10, 7, 10]) == 4
assert numbers_sum(10, [1, 2, 3, 4, 1]) == 2
assert numbers_sum(10, [20, 1, 2, 3, 4, 1]) == 2


def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(numbers_sum(k, nums))


if __name__ == '__main__':
    main()
