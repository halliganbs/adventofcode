import re
import heapq

def read_input(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
        return lines

def solution(line): 
    out = []
    current_idx = 0
    remaining = 12
    for _ in range(12):
        final_pos = remaining-1
        search_area = line[current_idx : (-final_pos if final_pos > 0 else None)]
        current_max = max(search_area)
        out.append(current_max)
        current_idx = current_idx + search_area.index(current_max) + 1
        remaining -= 1
    return "".join([str(b) for b in out])
   
if __name__ == '__main__':
    file = "input.txt"
    lines = read_input(file)
    total = 0
    for line in lines:
        part = solution(line)
        total += int(part)
        print(part, len(part))
    print()
    print(total)
