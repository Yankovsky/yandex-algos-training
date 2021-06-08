def system_of_equations(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        if a == 0 and c == 0:
            if b == 0 and d == 0:
                if e == 0 and f == 0:
                    return [5]
                return [0]

            if e * d != f * b:
                return [0]
            else:
                if b != 0:
                    return [4, f'{e / b:.5f}']
                else:
                    return [4, f'{f / d:.5f}']

        if b == 0 and d == 0:
            if e * c != f * a:
                return [0]
            else:
                if a != 0:
                    return [3, f'{e / a:.5f}']
                else:
                    return [3, f'{f / c:.5f}']

        if a != 0:
            coefficient = c / a
            c = 0
            d -= coefficient * b
            f -= coefficient * e
            if c == 0 and d == 0 and f == 0:
                return [1, f'{-a / b:.5f}', f'{e / b:.5f}']
        else:
            coefficient = a / c
            a = 0
            b -= coefficient * d
            e -= coefficient * f
            if a == 0 and b == 0 and e == 0:
                return [1, f'{-c / d:.5f}', f'{f / d:.5f}']

        return [0]
    else:
        if d != 0:
            x = (e - b * f / d) / (a - b * c / d)
            y = (f - c * x) / d
            return [2, f'{x:.5f}', f'{y:.5f}']
        else:
            x = (f - d * e / b) / (c - d * a / b)
            y = (e - a * x) / b
            return [2, f'{x:.5f}', f'{y:.5f}']

assert system_of_equations(1, 0, 0, 1, 3, 3) == [2, '3.00000', '3.00000']
assert system_of_equations(2, 2, 3, -3, 6, -3) == [2, '1.00000', '2.00000']
assert system_of_equations(1, 1, 1, -1, 3, -1) == [2, '1.00000', '2.00000']
assert system_of_equations(1, 1, 2, 2, 1, 2) == [1, '-1.00000', '1.00000']
assert system_of_equations(1, 1, 1, 1, 1, 2) == [0]
assert system_of_equations(0, 1, 0, 1, 2, 3) == [0]
assert system_of_equations(0, 1, 0, 2, 2, 4) == [4, '2.00000']
assert system_of_equations(1, 0, 2, 0, 2, 4) == [3, '2.00000']
assert system_of_equations(0, 0, 0, 0, 0, 0) == [5]
assert system_of_equations(0, 0, 0, 0, 1, 0) == [0]
assert system_of_equations(0, 2, 0, 4, 1, 2) == [4, '0.50000']
assert system_of_equations(0, 2, 0, 4, 1, 2) == [4, '0.50000']
assert system_of_equations(0, 0, 2, 4, 0, 2) == [1, '-0.50000', '0.50000']
assert system_of_equations(2, 4, 0, 0, 2, 0) == [1, '-0.50000', '0.50000']
assert system_of_equations(2, 0, 3, 0, 2, 3) == [3, '1.00000']
assert system_of_equations(2, 2, 3, 0, 6, 3) == [2, '1.00000', '2.00000']
assert system_of_equations(1, 1, 1.5, 0, 3, 1.5) == [2, '1.00000', '2.00000']


def main():
    a, b, c, d, e, f = [float(input()) for _ in range(6)]
    result = system_of_equations(a, b, c, d, e, f)
    print(' '.join(map(str, result)))


if __name__ == '__main__':
    main()
