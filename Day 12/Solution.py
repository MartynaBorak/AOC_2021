import os
from copy import deepcopy

def load_input(file):
    with open(file, 'r') as lines:
        return [[x for x in str(line).strip().split('-')] for line in lines]

def describe_caves(connections):
    #caves is a dict of caves : [list of caves it's connected to]
    caves = {}
    for cave1, cave2 in connections:
        if not cave1 in caves.keys():
            caves[cave1] = [cave2]
        elif not cave2 in caves[cave1]:
            caves[cave1].append(cave2)

        if not cave2 in caves.keys():
            caves[cave2] = [cave1]
        elif not cave1 in caves[cave2]:
            caves[cave2].append(cave1)        
    return caves

def find_paths(node, caves):
    if node == 'end':
        return ['0']
    current_caves = deepcopy(caves)
    branches = []
    branch = []
    if not current_caves[node] == []:
        if node.islower():
            for cave in current_caves.keys():
                if node in current_caves[cave]:
                    current_caves[cave].remove(node)
        for cave in current_caves[node]:
            paths = find_paths(cave, current_caves)
            for path in paths:
                branch = [node]
                branch.extend(path)
                branches.append(branch)
        return branches
    else:
        return [node]

def remove_deadends(all_paths):
    correct_paths = []
    for path in all_paths:
        if path[-1]=='0':
            correct_paths.append(path[:])
    return correct_paths

def duplicate_connection(node, caves):
    current_caves = deepcopy(caves)
    for cave in current_caves.keys():
        if node in current_caves[cave]:
            current_caves[cave].append(node)
    return current_caves

def main():
    #load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    connections = load_input(file_name)
    caves = describe_caves(connections)
    
    #part 1
    all_paths = find_paths('start', caves)
    correct_paths = remove_deadends(all_paths)
    print("Part 1: " + str(len(correct_paths)))

    #part 2
    small_caves = []
    correct_paths = []
    for cave in caves.keys():
        if cave.islower() and cave != 'start' and cave != 'end':
            small_caves.append(cave)
    for cave in small_caves:
        new_caves = duplicate_connection(cave, caves)
        all_paths = find_paths('start', new_caves)
        for path in remove_deadends(all_paths):
            if not path in correct_paths:
                correct_paths.append(path)
    print("Part 2: " + str(len(correct_paths)))
    

if __name__ == '__main__':
    main()