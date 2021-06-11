import sys
from collections import defaultdict


def bank_accounts(operations):
    result = []
    clients = defaultdict(int)
    for operation in operations:
        operation_name = operation[0]
        if operation_name == 'INCOME':
            percent = int(operation[1])
            for client_name in clients:
                balance = clients[client_name]
                if balance > 0:
                    clients[client_name] += balance * percent // 100
        else:
            client = operation[1]
            if operation_name == 'BALANCE':
                result.append(clients[client] if client in clients else 'ERROR')
            elif operation_name == 'DEPOSIT':
                clients[client] += int(operation[2])
            elif operation_name == 'WITHDRAW':
                clients[client] -= int(operation[2])
            else:
                second_client = operation[2]
                amount = int(operation[3])
                clients[client] -= amount
                clients[second_client] += amount

    return result


assert bank_accounts([
    ('DEPOSIT', 'Ivanov', '100'),
    ('INCOME', '5'),
    ('BALANCE', 'Ivanov'),
    ('TRANSFER', 'Ivanov', 'Petrov', '50'),
    ('WITHDRAW', 'Petrov', '100'),
    ('BALANCE', 'Petrov'),
    ('BALANCE', 'Sidorov')
]) == [105, -50, 'ERROR']
assert bank_accounts([
    ('BALANCE', 'Ivanov'),
    ('BALANCE', 'Petrov'),
    ('DEPOSIT', 'Ivanov', '100'),
    ('BALANCE', 'Ivanov'),
    ('BALANCE', 'Petrov'),
    ('DEPOSIT', 'Petrov', '150'),
    ('BALANCE', 'Petrov'),
    ('DEPOSIT', 'Ivanov', '10'),
    ('DEPOSIT', 'Petrov', '15'),
    ('BALANCE', 'Ivanov'),
    ('BALANCE', 'Petrov'),
    ('DEPOSIT', 'Ivanov', '46'),
    ('BALANCE', 'Ivanov'),
    ('BALANCE', 'Petrov'),
    ('DEPOSIT', 'Petrov', '14'),
    ('BALANCE', 'Ivanov'),
    ('BALANCE', 'Petrov')
]) == ['ERROR', 'ERROR', 100, 'ERROR', 150, 110, 165, 156, 165, 156, 179]
assert bank_accounts([
    ('BALANCE', 'a'),
    ('BALANCE', 'b'),
    ('DEPOSIT', 'a', '100'),
    ('BALANCE', 'a'),
    ('BALANCE', 'b'),
    ('WITHDRAW', 'a', '20'),
    ('BALANCE', 'a'),
    ('BALANCE', 'b'),
    ('WITHDRAW', 'b', '78'),
    ('BALANCE', 'a'),
    ('BALANCE', 'b'),
    ('WITHDRAW', 'a', '784'),
    ('BALANCE', 'a'),
    ('BALANCE', 'b'),
    ('DEPOSIT', 'b', '849'),
    ('BALANCE', 'a'),
    ('BALANCE', 'b')
]) == ['ERROR', 'ERROR', 100, 'ERROR', 80, 'ERROR', 80, -78, -704, -78, -704, 771]


def main():
    operations = [line.split() for line in sys.stdin]
    results = bank_accounts(operations)
    for result in results:
        print(result)


if __name__ == '__main__':
    main()
