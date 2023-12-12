from typing import List


def main():
    with open('day3/part1input.txt', 'r') as file:
        lines: List[str] = file.read().splitlines()
        count = 1
        count *= run(lines, 1, 1)
        count *= run(lines, 1, 3)
        count *= run(lines, 1, 5)
        count *= run(lines, 1, 7)
        count *= run(lines, 2, 1)
        print(f"Total count: {count}")


def run(lines: List[str], iInc: int, jInc: int):
    columns = len(lines[0].strip())
    rows = len(lines)
    print(f'columns, rows: {columns}, {rows}')
    i, j, count = 0, 0, 0
    while i < rows - 1:
        i += iInc
        j += jInc
        char = lines[i][j % columns]
        if char == "#":
            count += 1
    print(f'Tree Count: {count}')
    return count
