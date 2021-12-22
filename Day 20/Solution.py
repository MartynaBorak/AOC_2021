def load_input(file):
    with open(file, 'r') as lines:
        return [str(line).strip() for line in lines]

def get_image(input):
    image = []
    for line in input[2:]:
        image.append([0 if x=="." else 1 for x in line])
    return image

def add_frame(image, background):
    framed = []
    width = len(image)+4
    framed.extend([[background]*width for i in range(2)])
    for line in image:
        temp = [background]*2
        temp.extend(line)
        temp.extend([background]*2)
        framed.append(temp)
    framed.extend([[background]*width for i in range(2)])
    return framed

def enhance(enhancement, image, background):
    filtered = [[0]*(len(image[0])-2) for i in range(len(image)-2)]
    for y in range(1, len(image)-1):
        for x in range(1, len(image[0])-1):
            square = []
            for a in range(-1,2):
                for b in range(-1,2):
                    square.append(image[y+a][x+b])
            i = int("".join(str(a) for a in square), 2)
            filtered[y-1][x-1] = 0 if enhancement[i] == "." else 1

    i = int("".join(str(background)*9), 2)
    background = 0 if enhancement[i]=="." else 1
    return filtered, background

def main():
    #load file
    input = load_input("input.txt")
    enhancement = input[0]
    image = get_image(input)
    background = 0

    #part 1
    filtered = image
    for _ in range(2):
        filtered = add_frame(filtered, background)
        filtered, background = enhance(enhancement, filtered, background)
    total = 0
    for y in range(len(filtered)):
        for x in range(len(filtered[0])):
            if filtered[y][x]==1:
                total+=1
    print("Part 1: " + str(total))

    #part 2
    filtered = image
    for _ in range(50):
        filtered = add_frame(filtered, background)
        filtered, background = enhance(enhancement, filtered, background)
    total = 0
    for y in range(len(filtered)):
        for x in range(len(filtered[0])):
            if filtered[y][x]==1:
                total+=1
    print("Part 2: " + str(total))
    

if __name__ == '__main__':
    main()