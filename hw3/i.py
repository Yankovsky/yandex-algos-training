def polyglots(students):
    return [
        students[0].intersection(*students[1:]),
        students[0].union(*students[1:])
    ]


assert polyglots([
    {'Russian', 'English', 'Japanese'},
    {'Russian', 'English'},
    {'English'}]) == [{'English'}, {'Russian', 'English', 'Japanese'}]


def main():
    n = int(input())
    students = []
    for _ in range(n):
        m = int(input())
        students.append({input() for _ in range(m)})
    results = polyglots(students)
    for result in results:
        print(len(result))
        for language in result:
            print(language)


if __name__ == '__main__':
    main()
