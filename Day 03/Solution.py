import os

def load_input(file):
    with open(file, 'r') as lines:
        return [str(line[:-1]) for line in lines]

def get_gamma(numbers):
    gamma = ""

    for i in range(len(numbers[0])):
        gamma += most_common(numbers, i)

    return gamma

def get_epsilon(gamma):
    epsilon = ""
    
    for i in gamma:
        if i == '0':
            epsilon += '1'
        else:
            epsilon += '0'
    
    return epsilon

def find_oxygen(numbers):
    mc = ""
    
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            return numbers[0]
        
        mc = most_common(numbers, i)
        if mc == "-1":
            mc = "1"
        numbers = keep(numbers, i, mc)

    return numbers[0]

def find_co2(numbers):
    lc = ""
    
    for i in range(len(numbers[0])):
        if len(numbers) == 1:
            return numbers[0]
        
        lc = most_common(numbers, i)
        if lc == "0":
            lc = "1"
        else:
            lc = "0"
        numbers = keep(numbers, i, lc)

    return numbers[0]

def most_common(numbers, x):
    zeros = 0
    ones = 0
        
    for number in numbers:
        if number[x] == "0":
                zeros += 1
        else:
            ones += 1 
        
    if zeros > ones:
        return "0"
    if zeros < ones:
        return "1"
    if zeros == ones:
        return "-1"

def keep(numbers, bit, value):
    filtered = []

    for number in numbers:
        if number[bit] == value:
            filtered.append(number)

    return filtered

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    numbers = load_input(file_name)

    #part 1
    gamma = get_gamma(numbers)
    epsilon = get_epsilon(gamma)
    power_consumption = int(gamma, 2)*int(epsilon, 2)
    print("Part 1: " + str(power_consumption))
        
    #part 2
    oxygen = find_oxygen(numbers)
    co2 = find_co2(numbers)
    life_support = int(oxygen, 2)*int(co2, 2)
    print("Part 2: " + str(life_support))

if __name__ == '__main__':
    main()