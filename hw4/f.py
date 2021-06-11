import sys
from collections import defaultdict


def sales(sales_data):
    customers = defaultdict(lambda: defaultdict(int))
    for customer, item, quantity in sales_data:
        customers[customer][item] += quantity
    return customers


assert sales([
    ('Ivanov', 'paper', 10),
    ('Petrov', 'pens', 5),
    ('Ivanov', 'marker', 3),
    ('Ivanov', 'paper', 7),
    ('Petrov', 'envelope', 20),
    ('Ivanov', 'envelope', 5)
]) == {
   'Ivanov': {
       'paper': 17,
       'marker': 3,
       'envelope': 5
   },
   'Petrov': {
       'pens': 5,
       'envelope': 20
   }
}
assert sales([
    ("Ivanov", "aaa", 1),
    ("Petrov", "aaa", 2),
    ("Sidorov", "aaa", 3),
    ("Ivanov", "aaa", 6),
    ("Petrov", "aaa", 7),
    ("Sidorov", "aaa", 8),
    ("Ivanov", "bbb", 3),
    ("Petrov", "bbb", 7),
    ("Sidorov", "aaa", 345),
    ("Ivanov", "ccc", 45),
    ("Petrov", "ddd", 34),
    ("Ziborov", "eee", 234),
    ("Ivanov", "aaa", 45)
]) == {
   'Ivanov': {
       'aaa': 52,
       'bbb': 3,
       'ccc': 45
   },
   'Petrov': {
       'aaa': 9,
       'bbb': 7,
       'ddd': 34
   },
   'Sidorov': {
       'aaa': 356
   },
   'Ziborov': {
       'eee': 234
   }
}


def main():
    sales_data = []
    for line in sys.stdin:
        sales_item = line.split()
        sales_data.append((sales_item[0], sales_item[1], int(sales_item[2])))
    results = sales(sales_data)
    for customer in sorted(results.keys()):
        print(f'{customer}:')
        customer_data = results[customer]
        for item in sorted(customer_data.keys()):
            print(f'{item} {customer_data[item]}')


if __name__ == '__main__':
    main()
