import re

def check_valid_p2(data):
    invalids = 0
    a, b = data.split('-')
    print(a,b)
    for i in range(int(a), int(b)+1):
        i = str(i)
        if not i.startswith('0'):
            indx =  (i+i).find(i, 1, -1)
            if indx != -1 :
                invalids+=int(i)
                print('added', i)
    print()
    return invalids

def check_valid_p1(data):
    invalids = 0
    a,b, = data.split('-')
    print(a,b)
    for i in range(int(a), int(b)+1):
        i = str(i)
        if re.match(r"\b(\d+)\1+\b", i):
            if len(i) % 2 == 0:
                mid = int(len(i)/2)
                start = i[:mid]
                end = i[mid:]
                if start == end:
                    invalids+=int(i)
                    print('added', i)
    return invalids

if __name__ == "__main__":
    with open('input.txt') as f:
        ids = f.readline().split(',')
    invalids = 0
    for i in ids:
        invalids += check_valid_p2(i)
        print()
        # break
    

    print(invalids)