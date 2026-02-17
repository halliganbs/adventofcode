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

def find_greatest(a,b,c,d):
    return max([a,b,c,d], key=len)
def get_nums(a,b,c,d):
    # flip number order
    print(len(a), len(b), len(c), len(d))
    first = a[3]+b[3]+c[3]+d[3]
    second = a[2]+b[2]+c[2]+d[2]
    thrid = a[1]+b[1]+c[1]+d[1]

    return (int(first), int(second), int(thrid))

def part2(file):
    with open(file) as f:
        lines = f.read().splitlines()
    indices = len(lines[0]) # number of problems
    print(indices)
    numbers = []

    # get number groups
    test = 0
    prev = 0
    for i in range(5, indices+6, 5):
        a = lines[0][prev:i][:3]
        b = lines[1][prev:i][:3]
        c = lines[2][prev:i][:3]
        d = lines[3][prev:i][:3]
        print(a,b,c,d)
        # numbers.append(get_nums(a,b,c,d))
        prev = i
        test+=1
        if test > 3:
            break

    opers = lines[4].split()
    count = 0
    for n, o in zip(numbers,opers):
        if o == '*':
            count+= (n[0]*n[1]*n[2]*n[3])    
        elif o == '+':
            count+= (n[0]+n[1]+n[2]+n[3])
    return count


if __name__ == "__main__":
    path = 'input.txt'
    test = 'test.txt'
    print("Part 1:", part1(path))
    print('Part 2:', part2(path))
