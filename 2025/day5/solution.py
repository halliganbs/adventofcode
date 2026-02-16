def part1(file):
    with open(file) as f:
        lines = f.read().splitlines()
    idx = lines.index('')
    ranges = lines[:idx]
    count = 0
    for l in lines[1+idx:]:
        for r in ranges:
            a,b = r.split('-')
            if int(l)>=int(a)and int(l)<=int(b):
                count+=1
                break
    return count

"""
read in only the ranges
sort
make new stack of ranges add first range
for r in ranges
if r-first >= to efirst do something
if rsecond is > esecond, esecond = rfrist
    pop off stack
    append new range
"""

def part2(file):
    with open(file) as f:
        lines = f.read().splitlines()
    idx = lines.index('')
    ranges = lines[:idx]
    ranges = [(int(r.split('-')[0]),int(r.split('-')[1])) for r in ranges]
    ranges = sorted(ranges, key=lambda x: x[0])
    stack = []
    stack.append(ranges[0])
    for a1,b1 in ranges[1:]:
        a0, b0 = stack[-1]
        if a1 >= a0 and a1 <= b0 and b1> b0: # start 
            stack.pop()
            stack.append((a0, b1))
        elif b1 >= a0 and b1<=b0:
            pass
        elif a1 >= b0:
            stack.append((a1,b1))
    # print(stack)
    count = 0
    for s, e in stack:
        count+=(e-s)+1
    return count



if __name__ == "__main__":
    path = 'input.txt'
    path2 = 'test.txt'
    print("Part 1:", part1(path))
    print("Part 2:", part2(path))