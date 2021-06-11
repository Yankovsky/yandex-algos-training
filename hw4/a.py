def get_synonym(synonyms, word):
    synonyms_dict = {}
    for synonym_word1, synonym_word2 in synonyms:
        synonyms_dict[synonym_word1] = synonym_word2
        synonyms_dict[synonym_word2] = synonym_word1
    return synonyms_dict[word]


assert get_synonym([('Hello', 'Hi'), ('Bye', 'Goodbye'), ('List', 'Array')], 'Goodbye') == 'Bye'
assert get_synonym([('beep', 'Car')], 'Car') == 'beep'
assert get_synonym([('Ololo', 'Ololo'), ('Numbers', '1234567890')], 'Numbers') == '1234567890'


def main():
    n = int(input())
    synonyms = [tuple(input().split()) for _ in range(n)]
    word = input()
    print(get_synonym(synonyms, word))


if __name__ == '__main__':
    main()
