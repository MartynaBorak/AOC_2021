import os
from collections import Counter

def load_input(file):
    with open(file, 'r') as lines:
        temp = [str(line).split(',') for line in lines]
        return [int(x) for x in temp[0]]

def get_numbers(fish_list):
    fish_numbers = dict(Counter(fish_list))

    for i in range(9):
        if not i in fish_numbers:
            fish_numbers.update({i : 0})

    return fish_numbers

def next_day(fish_numbers):
    buff = fish_numbers.get(0)

    for i in range(8):
        fish_numbers.update({i : fish_numbers.get(i+1)})

    fish_numbers.update({6 : fish_numbers.get(6) + buff})
    fish_numbers.update({8 : buff})

    return fish_numbers

def sum_fish(fish_numbers):
    sum = 0
    for value in fish_numbers.values():
        sum += value

    return sum

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    fish_list = load_input(file_name)
    fish_numbers = get_numbers(fish_list)
    initial_numbers = fish_numbers.copy() #for part 2

    #part 1
    for i in range(80):
        fish_numbers = next_day(fish_numbers)
    print("Part 1: " + str(sum_fish(fish_numbers)))

    #part 2  
    fish_numbers = initial_numbers
    for i in range(256):
        fish_numbers = next_day(fish_numbers)
    print("Part 2: " + str(sum_fish(fish_numbers)))
    
    
if __name__ == '__main__':
    main()