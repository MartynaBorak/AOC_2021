import os
from collections import Counter

def load_input(file):
    with open(file, 'r') as lines:
        temp = [str(line).strip() for line in lines]
        start = [x for x in temp[0]]
        rules = {}
        for i in range(2, len(temp)):
            line = temp[i].split(" -> ")
            rules[line[0]] = line[1]
        return start, rules

def get_starting_pairs(polymer):
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append("".join((polymer[i], polymer[i+1])))
    return pairs

def get_numbers(pairs, rules):
    pairs_numbers = dict(Counter(pairs))
    for key in rules.keys():
        if not key in pairs_numbers.keys():
            pairs_numbers.update({key : 0})
    return pairs_numbers

def make_insertion(pair, rules):
    x = rules[pair]
    return "".join((pair[0], x)), "".join((x, pair[1]))

def count_letters(pairs):
    count = Counter()
    for key in pairs.keys():
        if not key[0] == key[1]: 
            count.update({key[0]:pairs[key], key[1]:pairs[key]})
        else:
            count.update({key[0]:pairs[key]*2})
    return count

def main():
    #load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    polymer, rules = load_input(file_name)
    temp = get_starting_pairs(polymer)
    pairs = get_numbers(temp, rules)
    
    #part 1
    for _ in range(10):
        step_count = Counter()
        for pair in pairs.keys():
            if not pairs[pair]==0:
                a, b = make_insertion(pair, rules)
                step_count.update({a:pairs[pair], b:pairs[pair]})
                pairs[pair] = 0
        for key, value in step_count.items():
            pairs[key] += value
    count = count_letters(pairs)
    for key, value in count.items():
        count[key] //= 2
    count.update({polymer[0]:1, polymer[-1]:1})
    answer = count.most_common()[0][1]-count.most_common()[-1][1]
    print("Part 1: " + str(answer))

    #part 2
    pairs = get_numbers(temp, rules)
    for _ in range(40):
        step_count = Counter()
        for pair in pairs.keys():
            if not pairs[pair]==0:
                a, b = make_insertion(pair, rules)
                step_count.update({a:pairs[pair], b:pairs[pair]})
                pairs[pair] = 0
        for key, value in step_count.items():
            pairs[key] += value
    count = count_letters(pairs)
    for key, value in count.items():
        count[key] //= 2
    count.update({polymer[0]:1, polymer[-1]:1})
    answer = count.most_common()[0][1]-count.most_common()[-1][1]
    print("Part 2: " + str(answer))
    

if __name__ == '__main__':
    main()