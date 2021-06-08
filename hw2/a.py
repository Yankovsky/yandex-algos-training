import math


def monotonically_increasing(nums):
    previous = -math.inf
    for num in nums:
        if num <= previous:
            return 'NO'
        previous = num
    return 'YES'


assert monotonically_increasing([1,7,9]) == 'YES'
assert monotonically_increasing([1,9,7]) == 'NO'
assert monotonically_increasing([2,2,2]) == 'NO'


def main():
    nums = map(int, input().split())
    print(monotonically_increasing(nums))


if __name__ == '__main__':
    main()
