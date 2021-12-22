def load_input(file):
    with open(file, 'r') as lines:
        return [str(line).strip() for line in lines]

def execute_line(line, switched_on):
    instruction, coordinates = line.split()
    x_range, y_range, z_range = coordinates.split(",")
    x_min, x_max = [int(x) for x in x_range[2:].split("..")]
    y_min, y_max = [int(y) for y in y_range[2:].split("..")]
    z_min, z_max = [int(z) for z in z_range[2:].split("..")]

    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            for z in range(z_min, z_max+1):
                switched_on.add((x,y,z)) if instruction=="on" else switched_on.discard((x,y,z))

    return switched_on

def main():
    #load file
    input = load_input("input.txt")
    initialization = input[:20]
    switched_on = set(()) #set of cubes represented as tuples (x,y,z)

    #part 1
    for line in initialization:
        execute_line(line, switched_on)
    print("Part 1: " + str(len(switched_on)))

    #part 2
    #print("Part 2: " + str())
    

if __name__ == '__main__':
    main()