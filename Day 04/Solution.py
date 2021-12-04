import os

def load_input(file):
    with open(file, 'r') as lines:
        return [str(line) for line in lines]

def get_boards(contents):
    del contents[:2]
    boards = []
    board = []

    while len(contents)>0:
        for i in range(5):
            line = contents[i].strip()
            line_int = [int(num) for num in line.split()]
            board.append(line_int)
        boards.append(board)
        board = []
        del contents[:6]

    return boards

def generate_score_sheets(boards):
    score_sheets = [[[-1 for x in range(5)] for y in range(5)] for i in range(len(boards))]
    
    return score_sheets

def next_round(number, boards, score_sheets):
    for i in range(len(boards)): #every board
        for y in range(len(boards[0])): #every line
            for x in range(len(boards[0][0])): #num in line
                if boards[i][y][x] == number:
                    score_sheets[i][y][x] = number
                    break
            
    return score_sheets

def check_scores(score_sheets):
    for i in range(len(score_sheets)): #every board
        #horizontal
        for y in range(len(score_sheets[0])): #every line
            horizontal = 0
            for x in score_sheets[i][y]:
                if x > -1:
                    horizontal += 1
            
            if horizontal == 5:
                return i

        #vertical
        for x in range(len(score_sheets[0][0])): #every column
            vertical = 0
            for y in range(len(score_sheets[0])): #line
                if score_sheets[i][y][x] > -1:
                    vertical += 1

            if vertical == 5:
                return i

    return -1

def count_points(board, scores):
    points = 0
    for line in board:
        for num in line:
            points += num

    for line in scores:
        for num in line:
            if num > -1:
                points -= num

    return points

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    contents = load_input(file_name)
    
    #part 1
    numbers = [int(num) for num in contents[0].split(',')]
    boards = get_boards(contents)
    score_sheets = generate_score_sheets(boards)
    answer = 0
    index = 0 #needed for 2nd part
    winner = -1

    for number in numbers:
        index += 1
        score_sheets = next_round(number, boards, score_sheets)
        winner = check_scores(score_sheets)
        if winner >= 0:
            answer = number*count_points(boards[winner], score_sheets[winner])
            break

    print("Part 1: " + str(answer))
        
    #part 2
    numbers = numbers[index:]
    answer = 0
    while len(boards) > 1:
        del boards[winner]
        del score_sheets[winner]

        for number in numbers:
            score_sheets = next_round(number, boards, score_sheets)
            winner = check_scores(score_sheets)
            if winner >= 0:
                answer = number*count_points(boards[winner], score_sheets[winner])
                break

    print("Part 2: " + str(answer))

if __name__ == '__main__':
    main()