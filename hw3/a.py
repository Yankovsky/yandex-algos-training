def unique_count(nums):
    return len(set(nums))


assert unique_count([1, 2, 3, 2, 1]) == 3
assert unique_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert unique_count([1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]) == 6


def main():
    nums = map(int, input().split())
    print(unique_count(nums))


if __name__ == '__main__':
    main()
