import sys
from collections import Counter


def cheating_test(keywords_array, case_sensitive, can_start_with_digit, text):
    keywords_array_filtered = filter(lambda keyword: len(keyword) <= 50, keywords_array)
    keywords = set(keywords_array_filtered if case_sensitive else map(str.lower, keywords_array_filtered))
    id_counter = Counter()

    id_start_index = None
    at_least_one_non_digit_char = False
    id_starts_with_digit = False

    def id_increment(id_end_index):
        current_word = text[id_start_index:id_end_index]
        normalized_current_word = current_word if case_sensitive else current_word.lower()
        not_a_keyword = normalized_current_word not in keywords
        valid_id = (id_starts_with_digit and can_start_with_digit) or (not id_starts_with_digit)
        if at_least_one_non_digit_char and not_a_keyword and valid_id:
            id_counter[normalized_current_word] += 1

    for i, c in enumerate(text):
        if c.isalnum() or c == '_':
            if not c.isdigit():
                at_least_one_non_digit_char = True

            if id_start_index is None:
                id_start_index = i
                if c.isdigit():
                    id_starts_with_digit = True
        else:
            if id_start_index is not None:
                id_increment(i)
                id_start_index = None
                at_least_one_non_digit_char = False
                id_starts_with_digit = False

    if id_start_index is not None:
        id_increment(len(text))

    return id_counter.most_common(1)[0][0]


assert cheating_test([], True, False, '''int main() {
  int a;
  int b;
  scanf("%d%d", &a, &b);
  printf("%d", a + b);
}''') == 'int'
assert cheating_test([], True, False, '''#define INT int
int main() {
  INT a, b;
  scanf("%d%d", &a, &b);
  printf("%d %d", a + b, 0);
}''') == 'd'
assert cheating_test([], False, False, '''#define INT int
int main() {
  INT a, b;
  scanf("%d%d", &a, &b);
  printf("%d %d", a + b, 0);
}''') == 'int'
assert cheating_test(['program', 'var', 'begin', 'end', 'while', 'for'], False, False, '''program sum;
var
  A, B: integer;
begin
  read(A, b);
  writeln(a + b);
end.''') == 'a'
assert cheating_test(['_'], True, True, '''a = 0h
b = 0h
c = 0h''') == '0h'
assert cheating_test(['a'], False, False, '''A b a a a
b b b B a''') == 'b'
assert cheating_test(['b'], False, False, '''A b a a a
b b b B a''') == 'a'
assert cheating_test(['a', 'b'], True, False, '''A b a a a
b b b B a''') == 'A'
assert cheating_test([], False, False, '''a b c c''') == 'c'
assert cheating_test([], True, False, '''3abc 3abc 3abc
AbC  AbC  AbC
abc  abc  abc''') == 'AbC'


def main():
    n, c, d = input().split()
    keywords = [input().rstrip() for _ in range(int(n))]
    text = sys.stdin.read()
    print(cheating_test(keywords, c == 'yes', d == 'yes', text))


if __name__ == '__main__':
    main()
