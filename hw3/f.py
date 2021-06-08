def genome_similarity(genome_a, genome_b):
    set_b = set()
    for i in range(len(genome_b) - 1):
        set_b.add(genome_b[i:i + 2])

    result = 0
    for i in range(len(genome_a) - 1):
        if genome_a[i:i + 2] in set_b:
            result += 1

    return result


assert genome_similarity('ABBACAB', 'BCABB') == 4
assert genome_similarity('ABBACAB', 'BCABABB') == 5


def main():
    print(genome_similarity(input(), input()))


if __name__ == '__main__':
    main()
