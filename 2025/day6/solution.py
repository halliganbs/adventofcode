def calc(a,b,c,d,oper):
    if oper == '*':
        return a*b*c*d
    elif oper == '+':
        return a+b+c+d
    else:
        print(a,b,c,oper)
def part1(file):
    with open(file) as f:
        lines = f.read().splitlines()
    lines = [l.split() for l in lines]
    indices = len(lines[0])
    count = 0
    for i in range(indices):
        a = int(lines[0][i])
        b = int(lines[1][i])
        c = int(lines[2][i])
        d = int(lines[3][i])
        oper = lines[4][i]
        # print(a,b,c,oper)
        count += calc(a,b,c,d,oper)
    return count

def part2(file):
    with open(file) as f:
        lines = f.read().splitlines()
    lines = [l.split() for l in lines]
    print(lines)

if __name__ == "__main__":
    path = 'input.txt'
    test = 'test.txt'
    print("Part 1:", part1(path))
    print('Part 2:', part2(test))
