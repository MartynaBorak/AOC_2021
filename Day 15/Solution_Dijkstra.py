import os
import sys

def load_input(file):
    with open(file, 'r') as lines:
        temp = [[int(x) for x in line.strip()] for line in lines]
        costs = {}
        for y in range(len(temp)):
            for x in range(len(temp[0])):
                costs[(y, x)] = temp[y][x]
        return costs, (len(temp)-1, len(temp[0])-1)

def initialize_path_lengths(costs):
    path_lengths = {}
    for key in costs.keys():
        path_lengths[key] = sys.maxsize
    return path_lengths

def find_next_vertex(possible_next, path_lengths):
    min = possible_next[0]
    for vertex in possible_next:
        if path_lengths[vertex] < path_lengths[min]:
            min = vertex
    return min

def dijkstra(costs, start, end):
    y, x = start
    path_lengths = initialize_path_lengths(costs) #inf everywhere
    path_lengths[start] = 0
    visited = {}
    for key, value in path_lengths.items():
        visited[key] = True if key==start else False
    vertex = start
    possible_next = [vertex]
    while(True):
        update_paths(costs, path_lengths, visited, vertex, possible_next)
        visited[vertex] = True
        possible_next.remove(vertex)
        if vertex == end:
            break
        vertex = find_next_vertex(possible_next, path_lengths)
    return path_lengths[end]

def update_paths(costs, path_lengths, visited, vertex, possible_next):
    y, x = vertex
    path = path_lengths[vertex]
    adjacent = [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]
    for adj in adjacent:
        if adj in visited.keys() and visited[adj] == False:
            path_adj = path_lengths[adj]
            if path + costs[adj] < path_adj:
                path_lengths[adj] = path + costs[adj]
            if not adj in possible_next:
                possible_next.append(adj)

def expand_map(costs, end):
    new_map = {}
    point = (0,0)
    len_y, len_x = end
    for key, value in costs.items():
        for d in range(5): #down
            for r in range(5): #right
                point = key
                point = (point[0]+d*(len_y+1), point[1]+r*(len_x+1))
                new_map[point] = (value + r + d -1)%9 +1
    return new_map, point

def main():
    #load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    costs, end = load_input(file_name)
    
    #part 1
    answer = dijkstra(costs, (0,0), end)
    print("Part 1: " + str(answer))

    #part 2
    costs, end = expand_map(costs, end)
    answer = dijkstra(costs, (0,0), end)
    print("Part 2: " + str(answer))
    

if __name__ == '__main__':
    main()