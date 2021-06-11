import sys
from collections import Counter


def most_frequent_word(text):
    words_counter = Counter()
    words = text.split()
    max_count = 1
    max_words = [words[0]]
    for word in words[1:]:
        words_counter.update([word])
        word_count = words_counter[word]
        if word_count > max_count:
            max_count = word_count
            max_words = [word]
        elif word_count == max_count:
            max_words.append(word)

    return sorted(max_words)[0]


assert most_frequent_word('apple orange banana banana orange') == 'banana'
assert most_frequent_word('oh you touch my tralala mmm my ding ding dong') == 'ding'
assert most_frequent_word('''q w e r t y u i o p
a s d f g h j k l
z x c v b n m''') == 'a'


def main():
    text = sys.stdin.read()
    print(most_frequent_word(text))


if __name__ == '__main__':
    main()
