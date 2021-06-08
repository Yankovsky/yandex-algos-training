# TODO

# def apps_per_floor(m, k, p, n):
#     floor = (p - 1) * m + n
#     q = k // floor
#
#     results = []
#     while True:
#         q * floor
#
#     # 9, 1, 4 -> 2.25 -> -1
#     # 10, 1, 4 -> 2.5 -> 3
#     # 11, 1, 4 -> 2.75 -> 3
#     # 12, 1, 4 -> 3 -> 3
#     # 13, 1, 4 -> 3.25 -> 4
#     # 6, 1, 2 -> 3 -> 0 (варианты 3, 4, 5)
#
#
#     n_kvartir / n_etagei = q
#
# def emergency(k1, m, k2, p2, n2):
#     # k2 //
#     pass
#
#
# assert apps_per_floor(20, 2, 1, 2) == 1
# assert apps_per_floor(20, 3, 1, 2) == 2
# assert apps_per_floor(20, 4, 1, 2) == 0
# assert apps_per_floor(20, 5, 1, 2) == 0
# assert apps_per_floor(20, 6, 1, 2) == 0
# assert apps_per_floor(20, 4, 1, 3) == -1
# assert apps_per_floor(20, 7, 1, 4) == 2
# assert apps_per_floor(20, 8, 1, 4) == 2
# assert apps_per_floor(20, 10, 1, 4) == 3
# assert apps_per_floor(20, 11, 1, 4) == 3
# assert apps_per_floor(20, 12, 1, 4) == 3
# assert apps_per_floor(20, 24, 2, 4) == 1
# assert apps_per_floor(20, 25, 2, 5) == 1
# assert apps_per_floor(20, 47, 2, 4) == 2
# assert apps_per_floor(20, 48, 2, 4) == 2
# assert apps_per_floor(20, 41, 1, 11) == 4
# assert apps_per_floor(20, 42, 1, 11) == 4
# assert apps_per_floor(20, 43, 1, 11) == 4
# assert apps_per_floor(20, 44, 1, 11) == 4
# assert apps_per_floor(20, 45, 1, 11) == -1
# assert apps_per_floor(2, 2, 2, 1) == -1
#
# assert emergency([89, 20, 41, 1, 11]) == [2, 3]
# assert emergency([11, 1, 1, 1, 1]) == [0, 1]
# assert emergency([3, 2, 2, 2, 1]) == [-1, -1]
# assert emergency([5, 20, 2, 1, 1]) == [0, 0]
#
#
# def main():
#     k1, m, k2, p2, n2 = [int(input()) for _ in range(5)]
#     print(emergency(k1, m, k2, p2, n2))
#
#
# if __name__ == '__main__':
#     main()
