import sys

# Считать строку до перевода строки
s = input()

# Считать строку и удалить все пробельные символы в начале и конце строки
s_stripped = input().strip()

# Нарезать строку на слова
words = input().split()

# Считать число из строки, если в ней всего одно число
m = int(input())

# Считать тройки чисел, разделённых пробелами, m раз (m строк)
m_triplets = [tuple(map(int, input().split())) for _ in range(m)]

# Считать несколько чисел, разделённых пробелами, из одной строки
n, k = map(int, input().split())

# Считать n слов из n строк
n_words = [input() for _ in range(n)]
# Считать k списков чисел неопределённой длины (k строк)
k_lists = [list(map(int, input().split())) for _ in range(k)]

# Считать неизвестное количество чисел с плавающей точкой до конца входа,
# каждое число на отдельной строке
unknown_count_of_floats = map(float, sys.stdin.read().split())

# Выведем все считанные данные
print(s)
print(s_stripped)
print(words)
print(*m_triplets)
print(*n_words)
print(*k_lists)
print(*unknown_count_of_floats)
