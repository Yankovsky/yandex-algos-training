import math

def nearest_num(nums, x):
    nearest = math.inf
    for num in nums:
        if abs(x - num) < abs(x - nearest):
            nearest = num

    return nearest


assert nearest_num([1, 2, 3, 4, 5], 6) == 5
assert nearest_num([5, 4, 3, 2, 1], 3) == 3


def main():
    n = int(input())
    nums = map(int, input().split())
    x = int(input())
    print(nearest_num(nums, x))


if __name__ == '__main__':
    main()
