import os

def load_input(file):
    with open(file, 'r') as lines:
        return [[int(x) for x in line.strip()] for line in lines]

def add_frame(map):
    for line in map:
        line.insert(0, 9)
        line.append(9)
    map.insert(0, [9]*len(map[0]))
    map.append([9]*len(map[0]))
    return map

def find_lowpoints(heightmap):
    lowpoints = []
    for y in range(1, len(heightmap)-1):
        for x in range(1, len(heightmap[0])-1):
            if is_lowpoint(heightmap, y, x):
                lowpoints.append([y, x])
    return lowpoints

def is_lowpoint(heightmap, y, x):
    point = heightmap[y][x]
    if point == 9:
        return False
    if not point < heightmap[y-1][x]:
        return False
    if not point < heightmap[y][x-1]:
        return False
    if not point < heightmap[y][x+1]:
        return False
    if not point < heightmap[y+1][x]:
        return False
    return True

def sum_lowpoints(heightmap, lowpoints):
    sum = 0
    for y, x in lowpoints:
        sum += 1+heightmap[y][x]
    return sum

def mark_basins(heightmap, lowpoints):
    for i in range(len(lowpoints)):
        heightmap = color_point(lowpoints[i][0], lowpoints[i][1], i+10, heightmap)
    return heightmap

def color_point(y, x, color, heightmap):
    #color bc it's "coloring" every basin with another number (flood fill)
    if heightmap[y][x] < 9:
        heightmap[y][x] = color
        heightmap = color_point(y+1, x, color, heightmap)
        heightmap = color_point(y-1, x, color, heightmap)
        heightmap = color_point(y, x-1, color, heightmap)
        heightmap = color_point(y, x+1, color, heightmap)
    return heightmap

def basins_sizes(basins_map, sizes):
    for y in range(1, len(basins_map)-1):
        for x in range(1, len(basins_map[0])-1):
            if basins_map[y][x] > 9:
                sizes[basins_map[y][x]-10] += 1
    return sizes

def biggest3_product(sizes):
    biggest = [sizes[0]]*3 #[biggest, 2nd, 3rd]
    for size in sizes:
        if size > biggest[2]:
            if size > biggest[1]:
                if size > biggest[0]: #the biggest
                    biggest.insert(0, size)
                    del biggest[3]
                else: #bigger than 3rd & 2nd, but not 1st
                    biggest.insert(1, size)
                    del biggest[3]
            else: #bigger than 3rd, but not 2nd
                biggest[2] = size
    return biggest[0]*biggest[1]*biggest[2]

def main():
    #load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    heightmap = add_frame(load_input(file_name))

    #part 1
    lowpoints = find_lowpoints(heightmap)
    sum = sum_lowpoints(heightmap, lowpoints)
    print("Part 1: " + str(sum))

    #part 2
    basins_map = mark_basins(heightmap, lowpoints)
    sizes = [0]*len(lowpoints)
    sizes = basins_sizes(basins_map, sizes)
    print("Part 2: " + str(biggest3_product(sizes)))
    

if __name__ == '__main__':
    main()