import os

def load_input(file):
    with open(file, 'r') as lines:
        return [str(line).split() for line in lines]

def count_direction(commands):
    horizontal = 0
    depth = 0
    direction = ""
    number = 0

    for command in commands:
        direction = command[0]
        number = int(command[1])

        if direction == "forward":
            horizontal += number
        if direction == "up":
            depth -= number
        if direction == "down":
            depth += number

    return horizontal*depth

#I made this function so that Ill have both parts solved here
#I could just modify the one above
def count_corrected(commands):
    horizontal = 0
    depth = 0
    aim = 0
    direction = ""
    number = 0

    for command in commands:
        direction = command[0]
        number = int(command[1])

        if direction == "forward":
            horizontal += number
            depth += number*aim
        if direction == "up":
            aim -= number
        if direction == "down":
            aim += number

    return horizontal*depth


def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    
    splited = load_input(file_name)

    answer = count_direction(splited)
    print("Part 1: " + str(answer))

    answer = count_corrected(splited)
    print("Part 2: " + str(answer))
    

if __name__ == '__main__':
    main()