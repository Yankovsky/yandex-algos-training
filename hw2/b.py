class Sequence:
    previous = None
    type = None

    def __init__(self, arr):
        if arr:
            for item in arr:
                self.add(item)

    def add(self, new_num):
        if self.previous:
            if new_num == self.previous:
                if self.type is None:
                    self.type = 'CONSTANT'
                elif self.type == 'ASCENDING':
                    self.type = 'WEAKLY ASCENDING'
                elif self.type == 'DESCENDING':
                    self.type = 'WEAKLY DESCENDING'
            elif new_num > self.previous:
                if self.type is None:
                    self.type = 'ASCENDING'
                elif self.type == 'WEAKLY DESCENDING' or self.type == 'DESCENDING':
                    self.type = 'RANDOM'
                elif self.type == 'CONSTANT':
                    self.type = 'WEAKLY ASCENDING'
            else:
                if self.type is None:
                    self.type = 'DESCENDING'
                elif self.type == 'WEAKLY ASCENDING' or self.type == 'ASCENDING':
                    self.type = 'RANDOM'
                elif self.type == 'CONSTANT':
                    self.type = 'WEAKLY DESCENDING'

        self.previous = new_num


assert Sequence([-530, -530, -530]).type == 'CONSTANT'
assert Sequence([1, 7, 9]).type == 'ASCENDING'
assert Sequence([1, 9, 7]).type == 'RANDOM'
assert Sequence([2, 2, 2]).type == 'CONSTANT'
assert Sequence([2, 2]).type == 'CONSTANT'
assert Sequence([2, 2, 3]).type == 'WEAKLY ASCENDING'
assert Sequence([3, 3, 2]).type == 'WEAKLY DESCENDING'
assert Sequence([4, 3, 2]).type == 'DESCENDING'


def main():
    sequence = Sequence([])
    while True:
        new_num = int(input())
        if new_num == -2000000000:
            print(sequence.type)
            break
        sequence.add(new_num)


if __name__ == '__main__':
    main()
