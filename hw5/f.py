import math


# Медленное решение, по которому легко сверяться, можно писать рандомизированные тесты.
# O(n*m)
# Для каждого класса ищем по всему списку моделей кондиционеров самый дешёвый.
def naive(required_powers, conditioners):
    result = 0
    for required_power in required_powers:
        conditioners_with_required_power = filter(lambda conditioner: conditioner[0] >= required_power, conditioners)
        result += min(conditioners_with_required_power, key=lambda conditioner: conditioner[1])[1]

    return result


# O(max(1000 * m, n))
# Для примера 2:
# conditioners = [(1, 10), (1, 5), (10, 7), (2, 3)] ->
# prices = [-inf, 3, 3, 7, 7, 7, 7, 7, 7, 7, 7, inf, ..., inf]
def linear(required_powers, conditioners):
    max_power = 1000
    prices = [-math.inf] + [math.inf] * max_power
    for conditioner in conditioners:
        price = conditioner[1]
        i = conditioner[0]
        # Здесь никогда не будет i < 0, потому что prices[0] = -math.inf
        while price < prices[i]:
            prices[i] = price
            i -= 1

    return sum(prices[required_power] for required_power in required_powers)


def optimal_conditioners(required_powers, conditioners):
    return linear(required_powers, conditioners)


assert optimal_conditioners([800], [(800, 1000)]) == 1000
assert optimal_conditioners([1, 2, 3], [(1, 10), (1, 5), (10, 7), (2, 3)]) == 13


def main():
    n = int(input())
    required_powers = map(int, input().split())
    m = int(input())
    conditioners = [tuple(map(int, input().split())) for _ in range(m)]
    print(optimal_conditioners(required_powers, conditioners))


if __name__ == '__main__':
    main()
