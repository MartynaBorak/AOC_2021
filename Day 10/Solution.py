import os

def load_input(file):
    with open(file, 'r') as lines:
        return [list(str(line).strip()) for line in lines]

def check_line(line, i, pairs):
    while i < len(line):
        if line[i] in pairs.keys():
            if not is_closing_correct(line, i, pairs):
                return line[i]
            else:
                del line[i-1]
                del line[i-1]
                i -= 1
                incorrect = check_line(line, i, pairs)
                if incorrect in pairs.keys():
                    return incorrect
        i += 1
    return ""

def is_closing_correct(line, i, pairs):
    if i==0:
        return False
    elif not line[i-1] == pairs.get(line[i]):
        return False
    return True

def count_completion_score(openings, completion_table):
    score = 0
    openings.reverse()
    for opening in openings:
        score *= 5
        score += completion_table.get(opening)
    return score

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name)
    pairs = {")":"(", "]":"[", "}":"{", ">":"<"}
    points_table = {")":3, "]":57, "}":1197, ">":25137}
    completion_table = {"(":1, "[":2, "{":3, "<": 4}
    score_incorrect = 0
    score_completions = []

    for line in lines:
        incorrect = check_line(line, 0, pairs)
        #part 1
        if incorrect in pairs.keys():
            score_incorrect += points_table.get(incorrect)
        #part 2
        else:
            if len(line) > 0:
                score_completions.append(count_completion_score(line, completion_table))
    print("Part 1: " + str(score_incorrect))
    
    score_completions.sort()
    middle = len(score_completions)//2
    print("Part 2: " + str(score_completions[middle]))
    

if __name__ == '__main__':
    main()