import sys

# faster input/output
next(sys.stdin)
word = sys.stdin.readline()[:-1]
text = sys.stdin.readline()[:-1]

word_len = len(word)
result = 0
# magic starts here
# Мы пользуемся тем, что если код символа возвести в четвёртую степень,
# то он не пересечётся с другими кодами.
# Подход похож на битовые маски.
# Такой подход может не сработать на каких-то определённых тестовых данных.
# Должен быть корректный способ надёжно задать базу непересекающихся чисел.
# Пожалуйста, не используйте этот метод в своём коде, это просто попытка разогнать алгоритм до максимума.
sequence_sum = 0
for c in word:
    c_ord = ord(c)
    # magic
    sequence_sum += c_ord ** 4

# Iterate through first word_len characters of text
for i in range(word_len):
    c_ord = ord(text[i])
    # more magic
    sequence_sum -= c_ord ** 4

if sequence_sum == 0:
    result += 1

# and now use sliding window technique
for i in range(word_len, len(text)):
    leftmost_ord = ord(text[i - word_len])
    # some more
    sequence_sum += leftmost_ord ** 4

    c_ord = ord(text[i])
    # magic again
    sequence_sum -= c_ord ** 4

    if sequence_sum == 0:
        result += 1

sys.stdout.write(str(result))
