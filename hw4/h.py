from collections import Counter


def maya(word, text):
    word_len = len(word)
    result = 0
    word_letters_counter = Counter(word)
    current_sliding_window_len = 0
    matching_letters_count = 0
    for i, c in enumerate(text):
        if current_sliding_window_len >= word_len:
            leftmost_char_out_of_current_sliding_window = text[i - word_len]
            if word_letters_counter[leftmost_char_out_of_current_sliding_window] >= 0:
                matching_letters_count -= 1
            else:
                matching_letters_count += 1
            word_letters_counter[leftmost_char_out_of_current_sliding_window] += 1
        else:
            current_sliding_window_len += 1

        if word_letters_counter[c] > 0:
            matching_letters_count += 1
        else:
            matching_letters_count -= 1

        word_letters_counter[c] -= 1
        if matching_letters_count == word_len:
            result += 1

    return result


assert maya('cAda', 'AbrAcadAbRa') == 2
assert maya(
    'OOO',
    'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
) == 98


def main():
    g, s_len = map(int, input().split())
    w = input()
    s = input()
    print(maya(w, s))


if __name__ == '__main__':
    main()
