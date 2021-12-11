import os

def load_input(file):
    with open(file, 'r') as lines:
        return [[int(x) for x in line.strip()] for line in lines]

def perform_step(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            map = point_step(map, y, x)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] > 9:
                map[y][x] = 0
    return map

def point_step(map, y, x):
    map[y][x] += 1
    if map[y][x] == 10:
        if y>0:
            if x>0:
                map = point_step(map, y-1, x-1) 
            map = point_step(map, y-1, x)
            if x<len(map[0])-1:
                map = point_step(map, y-1, x+1)
        if x>0:         
            map = point_step(map, y, x-1) 
        if x<len(map[0])-1:
            map = point_step(map, y, x+1) 
        if y<len(map)-1:
            if x>0:
                map = point_step(map, y+1, x-1) 
            map = point_step(map, y+1, x)
            if x<len(map[0])-1:
                map = point_step(map, y+1, x+1) 
    return map

def count_flashes(map):
    flashes = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 0:
                flashes += 1
    return flashes

def main():
    #load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    map_init = load_input(file_name)

    #part 1
    map = [x[:] for x in map_init]
    total_flashes = 0  
    for i in range(100):
        map = perform_step(map)
        total_flashes += count_flashes(map)
    print("Part 1: " + str(total_flashes))

    #part 2
    map = [x[:] for x in map_init]
    first_sync = -1
    i=0
    while(first_sync < 0):
        i+=1
        map = perform_step(map)
        if count_flashes(map) == len(map)*len(map[0]):
            first_sync = i
    print("Part 2: " + str(first_sync))
    

if __name__ == '__main__':
    main()