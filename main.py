def day_1(path: str):
    with open(path) as file:
        data = file.readlines()
        elves = ''.join(data).split('\n\n')
        elves = [elf.split('\n') for elf in elves]
        elves[-1][-1] = '0'
        elves = [[int(val) for val in elf] for elf in elves]
        food = list(map(sum, elves))
        print(max(food))
        food.sort()
        print(sum(food[-3:]))


if __name__ == '__main__':
    day_1("input1.txt")
