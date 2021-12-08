import os

def load_input(file):
    with open(file, 'r') as lines:
        return [str(line).split() for line in lines]

def count_easy(outputs):
    count = 0
    for line in outputs:
        for digit in line:
            if len(digit) == 7 or (len(digit)>1 and len(digit)<5):
                count += 1
    return count

def decode_easy(digits, decoded):
    for digit in digits:
        if len(digit) == 2:
            decoded[1] = digit
        elif len(digit) == 3:
            decoded[7] = digit
        elif len(digit) == 4:
            decoded[4] = digit
        elif len(digit) == 7:
            decoded[8] = digit
    return decoded

def decode_remaining(digits, decoded):
    decoded[3] = find_3(digits, decoded)
    decoded[5] = find_5(digits, decoded)
    decoded[2] = find_2(digits, decoded)
    decoded[0] = find_0(digits, decoded)
    decoded[9] = find_9(digits, decoded)
    decoded[6] = find_6(digits, decoded)
    return decoded

def find_0(digits, decoded):
    for digit in digits:
        if len(digit) == 6:
            for x in decoded[5]:
                if not x in digit:
                    return digit

def find_2(digits, decoded):
    for digit in digits:
        if len(digit) == 5:
            if not (digit==decoded[3] or digit==decoded[5]):
                return digit

def find_3(digits, decoded):
    for digit in digits:
        if len(digit) == 5:
            is3 = True
            for x in decoded[1]:
                if not x in digit:
                    is3 = False
                    break
            if is3 == True:
                return digit

def find_5(digits, decoded):
    for digit in digits:
        if len(digit) == 5 and not digit==decoded[3]:
            common = 0
            for x in decoded[4]:
                if x in digit:
                        common += 1   
            if common == 3:
                return digit

def find_6(digits, decoded):
    for digit in digits:
        if len(digit) == 6:
            if not (digit==decoded[0] or digit==decoded[9]):
                return digit

def find_9(digits, decoded):
    for digit in digits:
        if len(digit) == 6 and not digit==decoded[0]:
            is9 = True
            for x in decoded[1]:
                if not x in digit:
                    is9 = False
                    break
            if is9 == True:
                return digit

def read_output(decoded, output):
    output_digits = [0]*4
    for i in range(4):
        for j in range(10):
            if len(decoded[j]) == len(output[i]):
                same = True
                for x in decoded[j]:
                    if not x in output[i]:
                        same = False
                        break
                if same == True:
                    output_digits[i] = j
    return output_digits[0]*1000 + output_digits[1]*100 + output_digits[2]*10 + output_digits[3]

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    lines = load_input(file_name) 

    #part 1
    outputs = [line[11:] for line in lines]
    print("Part 1: " + str(count_easy(outputs)))

    #part 2
    patterns = [line[:10] for line in lines]
    sum = 0
    for i in range(len(patterns)):
        decoded = [""]*10
        decoded = decode_easy(patterns[i], decoded)
        decoded = decode_remaining(patterns[i], decoded)
        sum += read_output(decoded, outputs[i])
    print("Part 2: " + str(sum))


if __name__ == '__main__':
    main()