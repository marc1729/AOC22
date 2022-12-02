def day_1(data):
    elves = ''.join(data).split('\n\n')
    elves = [elf.split('\n') for elf in elves]
    elves[-1][-1] = '0'
    elves = [[int(val) for val in elf] for elf in elves]
    food = list(map(sum, elves))
    food.sort()
    return max(food), sum(food[-3:])


def score_rock_paper_scissors(game):
    score = game[1]
    if game[1] == game[0]:
        score = score + 3
    elif game[1] == game[0] + 1 or (game[1] == 1 and game[0] == 3):
        score = score + 6
    return score


def score_rock_paper_scissors_part_2(game):
    score = (game[1] - 1) * 3
    if game[1] == 2:
        score = score + game[0]
    elif game[1] == 3:
        score = score + ((game[0] ) % 3) + 1
    elif game[1] == 1:
        score = score + ((game[0] - 2) % 3) + 1
    return score


def day_2(data):
    games = ''.join(data).split('\n')
    games = games[:-1]
    # games = [game.replace('A', 'rock').replace('B', 'paper').replace('C', 'scissors') for game in games]
    # games = [game.replace('X', 'rock').replace('Y', 'paper').replace('Z', 'scissors') for game in games]
    games = [game.replace('A', '1').replace('B', '2').replace('C', '3') for game in games]
    games = [game.replace('X', '1').replace('Y', '2').replace('Z', '3') for game in games]
    games = [game.split(' ') for game in games]
    games = [[int(shape) for shape in game] for game in games]
    # games_part_2 = [game.replace('X', '0').replace('Y', '3').replace('Z', '6') for game in games_part_2]
    # games_part_2 = [game.replace('A', '0').replace('B', '1').replace('C', '2') for game in games_part_2]
    # games_part_2 = [game.split(' ') for game in games_part_2]
    # games_part_2 = [[int(shape) for shape in game] for game in games_part_2]
    games_part_2 = games.copy()
    result_1 = sum(map(score_rock_paper_scissors, games))
    result_2 = sum(map(score_rock_paper_scissors_part_2, games_part_2))
    return result_1, result_2

def day(day_number: int):
    path = "input" + str(day_number) + ".txt"
    with open(path) as file:
        data = file.readlines()
        part_1_result, part_2_result = eval("day_" + str(day_number))(data)
        print("Results for day ", day_number)
        print("Part 1: ", part_1_result)
        print("Part 2: ", part_2_result)


if __name__ == '__main__':
    day(2)
