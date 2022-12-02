def day_1(data):
    elves = ''.join(data).split('\n\n')
    elves = [elf.split('\n') for elf in elves]
    elves[-1][-1] = '0'
    elves = [[int(val) for val in elf] for elf in elves]
    food = list(map(sum, elves))
    food.sort()
    return max(food), sum(food[-3:])


def day(day_number: int):
    path = "input" + str(day_number) + ".txt"
    with open(path) as file:
        data = file.readlines()
        part_1_result, part_2_result = eval("day_" + str(day_number))(data)
        print("Results for day ", day_number)
        print("Part 1: ", part_1_result)
        print("Part 2: ", part_2_result)


if __name__ == '__main__':
    day(1)
