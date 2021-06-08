import math


def max_product(nums):
    if len(nums) == 3:
        return sorted(nums)

    min_negative_nums = [None, None, None]
    max_negative_nums = [None, None]
    max_positive_nums = [None, None, None]

    for num in nums:
        if num < 0:
            if max_negative_nums[0] is None or num < max_negative_nums[0]:
                max_negative_nums[1] = max_negative_nums[0]
                max_negative_nums[0] = num
            elif max_negative_nums[1] is None or num < max_negative_nums[1]:
                max_negative_nums[1] = num

            if min_negative_nums[2] is None or num > min_negative_nums[2]:
                min_negative_nums[0] = min_negative_nums[1]
                min_negative_nums[1] = min_negative_nums[2]
                min_negative_nums[2] = num
            elif min_negative_nums[1] is None or num > min_negative_nums[1]:
                min_negative_nums[0] = min_negative_nums[1]
                min_negative_nums[1] = num
            elif min_negative_nums[0] is None or num > min_negative_nums[0]:
                min_negative_nums[0] = num
        else:
            if max_positive_nums[2] is None or num > max_positive_nums[2]:
                max_positive_nums[0] = max_positive_nums[1]
                max_positive_nums[1] = max_positive_nums[2]
                max_positive_nums[2] = num
            elif max_positive_nums[1] is None or num > max_positive_nums[1]:
                max_positive_nums[0] = max_positive_nums[1]
                max_positive_nums[1] = num
            elif max_positive_nums[0] is None or num > max_positive_nums[0]:
                max_positive_nums[0] = num

    three_positive = max_positive_nums \
        if len([x for x in max_positive_nums if x is not None]) == 3 \
        else [-math.inf]
    two_negative_one_positive = [*max_negative_nums, max_positive_nums[2]] \
        if max_positive_nums[2] is not None and len([x for x in max_negative_nums if x is not None]) == 2 \
        else [-math.inf]
    three_min_negative = min_negative_nums \
        if len([x for x in min_negative_nums if x is not None]) == 3 \
        else [-math.inf]

    return max([three_positive, two_negative_one_positive, three_min_negative], key=math.prod)


assert max_product([4, 3, 5, 2, 5]) == [4, 5, 5]
assert max_product([-4, 3, -5, 2, 5]) == [-5, -4, 5]
assert max_product([4, 3, -5, 2, 5]) == [3, 4, 5]
assert max_product([-100, 1, 1]) == [-100, 1, 1]
assert max_product([-100, 100, 1, 2]) == [1, 2, 100]
assert max_product([-100, 100, -1, 2]) == [-100, -1, 100]
assert max_product([-100, 100, 0]) == [-100, 0, 100]
assert max_product([3, 5, 1, 7, 9, 0, 9, -3, 10]) == [9, 9, 10]
assert max_product([-5, -30000, -12]) == [-30000, -12, -5]
assert max_product([1, 2, 3]) == [1, 2, 3]
assert max_product([-1, -2, -3, -4]) == [-3, -2, -1]
assert max_product(
    [12288, -10075, 29710, 15686, -18900, -17715, 15992, 24431, 6220, 28403, -23148, 18480, -22905, 5411, -7602, 15560,
     -26674, 11109, -4323, 6146, -1523, 4312, 10666, -15343, -17679, 7284, 20709, -7103, 24305, 14334, -12281, 17314,
     26061, 25616, 17453, 16618, -24230, -19788, 21172, 11339, 2202, -22442, -20997, 1879, -8773, -8736, 5310, -23372,
     12621, -25596, -28609, -13309, -13, 10336, 15812, -21193, 21576, -1897, -12311, -6988, -25143, -3501, 23231, 26610,
     12618, 25834, -29140, 21011, 23427, 1494, 15215, 23013, -15739, 8325, 5359, -12932, 18111, -72, -12509, 20116,
     24390, 1920, 17487, 25536, 24934, -6784, -16417, -2222, -16569, -25594, 4491, 14249, -28927, 27281, 3297, 5998,
     6259, 4577, 12415, 3779, -8856, 3994, 19941, 11047, 2866, -24443, -17299, -9556, 12244, 6376, -13694, -14647,
     -22225, 21872, 7543, -6935, 17736, -2464, 9390, 1133, 18202, -9733, -26011, 13474, 29793, -26628, -26124, 27776,
     970, 14277, -23213, 775, -9318, 29014, -5645, -27027, -21822, -17450, -5, -655, 22807, -20981, 16310, 27605,
     -18393, 914, 7323, 599, -12503, -28684, 5835, -5627, 25891, -11801, 21243, -21506, 22542, -5097, 8115, 178, 10427,
     25808, 10836, -11213, 18488, 21293, 14652, 12260, 42, 21034, 8396, -27956, 13670, -296, -757, 18076, -15597, 4135,
     -25222, -19603, 8007, 6012, 2704, 28935, 16188, -20848, 13502, -11950, -24466, 5440, 26348, 27378, 7990, -11523,
     -26393
     ]) == [29014, 29710, 29793]


def main():
    nums = list(map(int, input().split()))
    print(' '.join(map(str, max_product(nums))))


if __name__ == '__main__':
    main()