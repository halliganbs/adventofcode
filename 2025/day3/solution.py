import re

def read_input(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        return lines

def solution(line):
    first = 0
    first_idx = -1
    second = 0
    # find first number from all values before last
    for i, s in enumerate(line[:-1]):
        if int(s) > int(first):
            first = s
            first_idx = i 
    for i, s in enumerate(line[first_idx+1:]):
        if int(s) > int(second):
            second = s 
    return int(first+second)

if __name__ == '__main__':
    file = "input.txt"
    lines = read_input(file)
    total = 0
    for line in lines:
        print(line)
        result = solution(line)
        print(result)
        total+=result
    print(total)
