def is_symmetric(nums):
    for i in range(len(nums) // 2):
        if nums[i] != nums[-1 - i]:
            return False
    return True


def symmetric_sequence(nums):
    for i in range(len(nums)):
        if is_symmetric(nums[i:]):
            return list(reversed(nums[:i]))


assert symmetric_sequence([1, 2, 3, 4, 5, 4, 3, 2, 1]) == []
assert symmetric_sequence([1, 2, 1, 2, 2]) == [1, 2, 1]
assert symmetric_sequence([1, 2, 3, 4, 5]) == [4, 3, 2, 1]


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    result = symmetric_sequence(nums)
    print(len(result))
    if len(result):
        print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
