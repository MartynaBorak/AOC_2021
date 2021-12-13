import os

def load_input(file):
    with open(file, 'r') as lines:
        raw = [str(line).strip() for line in lines]
        sep = raw.index("")
        points = []
        for i in range(sep):
            points.append([int(x) for x in raw[i].split(',')])        
        folds = []
        for i in range(sep+1, len(raw)):
            temp = raw[i].split()[2].split('=')
            folds.append([temp[0], int(temp[1])])

        return points, folds

def get_page(points, folds):
    #find first x-fold and first y-fold
    x_fold = -1
    y_fold = -1
    for axis, val in folds:
        if axis == "x" and x_fold<0:
            x_fold = val
        elif axis == "y" and y_fold<0:
            y_fold = val

        if x_fold>0 and y_fold>0:
            break

    page = [["." for x in range(2*x_fold + 1)] for y in range(2*y_fold + 1)]
    for x,y in points:
        page[y][x] = "#"
    return page

def fold_page(page, fold):
    axis, val = fold
    if axis == 'y':
        folded = [["." for x in range(len(page[0]))] for y in range(val)]
        for y in range(len(folded)):
            for x in range(len(folded[0])):
                if page[y][x]=="#" or page[-y-1][x]=="#":
                    folded[y][x] = "#"
    else: #axis == x
        folded = [["." for x in range(val)] for y in range(len(page))]
        for y in range(len(folded)):
            for x in range(len(folded[0])):
                if page[y][x]=="#" or page[y][-x-1]=="#":
                    folded[y][x] = "#"
    return folded

def count_dots(page):
    count = 0
    for y in range(len(page)):
        for x in range(len(page[0])):
            if page[y][x] == "#":
                count += 1
    return count

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    points, folds = load_input(file_name)
    page = get_page(points, folds)

    #part 1
    folded = fold_page(page, folds[0])
    print("Part 1: " + str(count_dots(folded)))
    
    #part 2
    for fold in folds:
        page = fold_page(page, fold)
    print("Part 2:")
    for line in page:
        print("".join(line))
    

if __name__ == '__main__':
    main()