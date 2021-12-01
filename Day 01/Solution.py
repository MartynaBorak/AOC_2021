import os

def load_input(file):
    with open(file, 'r') as lines:
        return [int(line) for line in lines]

def count_increases(numbers):
    count = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            count+=1

    return count

def count_filtered(numbers):
    count = 0

    for i in range(1, len(numbers)-2):

        if numbers[i+2] > numbers[i-1]:
            count+=1

    return count

def main():
    # part 1
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    numbers = load_input(file_name)
    
    count = count_increases(numbers)
    print("Part 1: " + str(count))
        
    count = count_filtered(numbers)
    print("Part 2: " + str(count))

if __name__ == '__main__':
    main()

