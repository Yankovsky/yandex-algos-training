import sys


def maya(word, text):
    word_len = len(word)
    result = 0
    # Use an array instead of a set for faster random access
    # A-Z and a-z have codes 65-90 and 97-122 respectively
    word_letters_counter = [0] * 123
    for c in word:
        word_letters_counter[ord(c)] += 1
    matching_letters_count = 0

    # Iterate through first word_len characters of text
    for i in range(word_len):
        c_ord = ord(text[i])
        matching_letters_count += (1 if word_letters_counter[c_ord] > 0 else -1)
        word_letters_counter[c_ord] -= 1

    if matching_letters_count == word_len:
        result += 1

    # and now use sliding window technique
    for i in range(word_len, len(text)):
        leftmost_ord = ord(text[i - word_len])
        matching_letters_count += (-1 if word_letters_counter[leftmost_ord] >= 0 else 1)
        word_letters_counter[leftmost_ord] += 1

        c_ord = ord(text[i])
        matching_letters_count += (1 if word_letters_counter[c_ord] > 0 else -1)
        word_letters_counter[c_ord] -= 1

        if matching_letters_count == word_len:
            result += 1

    return result


assert maya('cAda', 'AbrAcadAbRa') == 2
assert maya(
    'OOO',
    'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
) == 2


def main():
    # faster input/output
    next(sys.stdin)
    w = sys.stdin.readline()[:-1]
    s = sys.stdin.readline()[:-1]
    sys.stdout.write(str(maya(w, s)))


if __name__ == '__main__':
    main()
