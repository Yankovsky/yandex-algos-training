def phone(vasya_phone, phone_book):
    default_code = '495'

    def parse_phone(phone):
        digits = ''.join([c for c in phone if c.isdigit()])
        if len(digits) == 7:
            return (default_code, digits)
        else:
            return (digits[1:4], digits[4:])

    vasya_parsed_phone = parse_phone(vasya_phone)
    return ['YES' if parse_phone(phone_book_item) == vasya_parsed_phone else 'NO' for phone_book_item in phone_book]


assert phone('8(495)430-23-97', ['+7-4-9-5-43-023-97', '4-3-0-2-3-9-7', '8-495-430']) == ['YES', 'YES', 'NO']
assert phone('86406361642', ['83341994118', '86406361642', '83341994118']) == ['NO', 'YES', 'NO']
assert phone('+78047952807', ['+78047952807', '+76147514928', '88047952807']) == ['YES', 'NO', 'YES']


def main():
    vasya_phone = input()
    phone_book = [input(), input(), input()]
    result = phone(vasya_phone, phone_book)
    print(result[0])
    print(result[1])
    print(result[2])


if __name__ == '__main__':
    main()
