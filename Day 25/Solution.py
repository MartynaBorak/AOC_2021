def load_input(file):
    with open(file, 'r') as lines:
        return [[x for x in str(line).strip()] for line in lines]

def step_east(map):
    moved = False
    new_map = [["."]*len(map[0]) for i in range(len(map))]
    for y in range(len(map)):
        for x in range(len(map[0])-1):
            if map[y][x] == ">":
                if map[y][x+1] == ".":
                    new_map[y][x+1] = ">"
                    moved = True
                else:
                    new_map[y][x] = ">"
            elif map[y][x] == "v":
                new_map[y][x] = "v"
        if map[y][-1] == ">":
            if map[y][0] == ".":
                new_map[y][0] = ">"
                moved = True
            else:
                new_map[y][-1] = ">"
        elif map[y][-1] == "v":
            new_map[y][-1] = "v"
    return new_map, moved

def step_south(map):
    moved = False
    new_map = [["."]*len(map[0]) for i in range(len(map))]
    for y in range(len(map)-1):
        for x in range(len(map[0])):
            if map[y][x] == "v":
                if map[y+1][x] == ".":
                    new_map[y+1][x] = "v"
                    moved = True
                else:
                    new_map[y][x] = "v"
            elif map[y][x] == ">":
                new_map[y][x] = ">"
    for x in range(len(map[0])):
        if map[-1][x] == "v":
            if map[0][x] == ".":
                new_map[0][x] = "v"
                moved = True
            else:
                new_map[-1][x] = "v"
        elif map[-1][x] == ">":
            new_map[-1][x] = ">"
    return new_map, moved

def main():
    #load file
    cucumbers_map = load_input("input.txt")

    #part 1
    i = 0
    while True:
        i += 1
        cucumbers_map, changed = step_east(cucumbers_map)
        cucumbers_map, changed2 = step_south(cucumbers_map)
        if not (changed or changed2):
            break
    print("Part 1: " + str(i))
    

if __name__ == '__main__':
    main()