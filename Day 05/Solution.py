import os

def load_input(file):
    with open(file, 'r') as lines:
        return [str(line) for line in lines]

def get_points(contents):
    #split lines into [x1, y1, x2, y2]
    points = []
    line_divided = []
    line_ready = []

    for line in contents:
        line = line.strip()
        line_divided = line.split()
        del line_divided[1]
        line_ready.append(int(line_divided[0].split(',')[0])) #x1
        line_ready.append(int(line_divided[0].split(',')[1])) #y1
        line_ready.append(int(line_divided[1].split(',')[0])) #x2
        line_ready.append(int(line_divided[1].split(',')[1])) #y2
        points.append(line_ready)
        line_ready = []
    
    return points

def get_horizontal_vertical(points):
    points_hv = []

    for line in points:
        if line[0] == line[2]:
            points_hv.append(line)
            continue
        if line[1] == line[3]:
            points_hv.append(line)

    return points_hv

def generate_map(points):
    #find max of x,y and create a matrix of 0s
    max_x = points[0][0]
    max_y = points[0][1]

    for line in points:
        if line[0] > max_x:
            max_x = line[0]
        if line[2] > max_x:
            max_x = line[2]

        if line[1] > max_y:
            max_y = line[1]
        if line[3] > max_y:
            max_y = line[3]

    vents_map = [[0 for x in range(max_x+1)] for y in range(max_y+1)]
    return vents_map

def mark_lines(points, vents_map):
    for line in points:
        if line[0] == line[2]:
            #vertical line
            x = line[0]
            for y in range(min(line[1], line[3]), max(line[1], line[3])+1):
                vents_map[x][y] += 1

        if line[1] == line[3]:
            #horizontal line
            y = line[1]
            for x in range(min(line[0], line[2]), max(line[0], line[2])+1):
                vents_map[x][y] += 1

        if line[0] != line[2] and line[1] != line[3]:
            #diagonal line
            x_vector = [x for x in range(min(line[0], line[2]), max(line[0], line[2])+1)]
            if line[0]>line[2]:
                x_vector.reverse() #original order
            y_vector = [y for y in range(min(line[1], line[3]), max(line[1], line[3])+1)]
            if line[1]>line[3]:
                y_vector.reverse() #original order
            for i in range(len(x_vector)):
                vents_map[x_vector[i]][y_vector[i]] += 1

    return vents_map

def count_overlaps(vents_map):
    count = 0

    for line in vents_map:
        for point in line:
            if point > 1:
                count += 1

    return count

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    contents = load_input(file_name)
    
    #part 1
    points = get_points(contents)
    vents_map = generate_map(points)
    points_hv = get_horizontal_vertical(points)
    vents_map = mark_lines(points_hv, vents_map)
    answer = count_overlaps(vents_map)
    print("Part 1: " + str(answer))
        
    #part 2
    vents_map = generate_map(points) #clear the map as mark_lines() draws every kind of line
    vents_map = mark_lines(points, vents_map)
    answer = count_overlaps(vents_map)
    print("Part 2: " + str(answer))

if __name__ == '__main__':
    main()