import math

def find_possible_vx(v_min, v_max, x_min, x_max):
    good = []
    for v in range(v_min, v_max):
        i = 0
        x = 0
        temp_v = v
        steps = [v, 0, 0]
        while x < x_max and i < 50:
            i += 1
            x += temp_v
            temp_v -= 1
            if x >= x_min and x <= x_max:
                if temp_v == 0:
                    if steps[1] == 0:
                        steps[1] = i
                    steps[2] = 1000
                    break
                elif steps[1] == 0:
                    steps[1] = i
                    steps[2] = i
                else:
                    steps[2] += 1
        if not steps[1] == 0:  
            good.append(steps)
    return good

def find_possible_vy(v_min, v_max, y_min, y_max):
    good = []
    for v in range(v_min, v_max):
        i = 0
        y = 0
        temp_v = v
        steps = [v, 0, 0]
        while y > y_min and i < 1000:
            i += 1
            y += temp_v
            temp_v -= 1
            if y >= y_min and y <= y_max:
                if steps[1] == 0:
                    steps[1] = i
                    steps[2] = i
                else:
                    steps[2] += 1
        if not steps[1] == 0:  
            good.append(steps)
    return good

def find_max(vy):
    value = 0
    y = vy
    while value<y:
        value = y
        vy -= 1
        y += vy
    return value

def possibilities_vy(vy):
    possibilities = []
    for v in vy:
        if v[1] == v[2]:
            possibilities.append((v[0], v[1]))
        else:
            possibilities.extend([(v[0], i) for i in range(v[1], v[2]+1)])
    return possibilities

def possibilities_vx(vx):
    vx.reverse()
    possibilities = []
    for v in vx:
        if v[1] == v[2]:
            possibilities.append((v[0], v[1]))
        elif v[2]==1000:
            for i in range(v[1], v[2]+1):
                exists = False
                for pos in possibilities:
                    if i == pos[1]:
                        exists = True
                if exists:
                    possibilities.append((v[0], i))
                else:
                    possibilities.append((v[0], 1000))
                    break
        else:
            possibilities.extend([(v[0], i) for i in range(v[1], v[2]+1)])
    return possibilities

def find_pairs(vx, vy):
    pairs = {}
    for y, steps_y in vy:
        for x, steps_x in vx:
            if steps_x==steps_y or (steps_x == 1000 and steps_y>18):
                if (x, y) not in pairs.keys():
                    pairs[(x, y)] = steps_y
    return pairs

def main():
    #today's code works only for my input, bc the input was very simple
    #it was easier to copy the numbers and set ranges after looking at outputs at different stages

    # input
    x_min = 175
    x_max = 227
    y_min = -134
    y_max = -79
    
    # part 1
    vx = find_possible_vx(int(math.sqrt(2*x_min)), x_max+1, x_min, x_max)
    possible_vx = []
    for v in vx:
        if v[2] == 1000:
            possible_vx.append(v[0])
    vy = find_possible_vy(y_min, 1000, y_min, y_max)
    vy_max = vy[-1][0]
    answer = find_max(vy_max)
    print("Part 1: " + str(answer))
        
    # part 2
    vx_pos = possibilities_vx(vx)  #list of tuples (vx, steps)
    vy_pos = possibilities_vy(vy)  #list of tuples (vy, steps)
    pairs = find_pairs(vx_pos, vy_pos)     #dict of (vx, vy) : steps
    print("Part 2: " + str(len(pairs)))

if __name__ == '__main__':
    main()

