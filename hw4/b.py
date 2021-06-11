import sys
from collections import Counter


def word_number(text):
    result = []
    words_counter = Counter()
    for word in text.split():
        result.append(words_counter[word])
        words_counter.update([word])
    return result


assert word_number('one two one tho three') == [0, 0, 1, 0, 0]
assert word_number('''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.''') == \
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 2, 2, 0, 0, 0, 0, 1, 2, 3, 3, 1, 1, 4, 0, 1, 0, 1, 2, 4, 1, 5, 0, 0]
assert word_number('aba aba; aba @?"') == [0, 0, 1, 0]


def main():
    text = sys.stdin.read()
    print(*word_number(text))


if __name__ == '__main__':
    main()
