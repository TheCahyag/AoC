from typing import List


def main():
    with open('day3/part1input.txt', 'r') as file:
        lines: List[str] = file.read().splitlines()
        columns = len(lines[0].strip())
        rows = len(lines)
        print(f'columns, rows: {columns}, {rows}')
        i, j, count = 0, 0, 0
        while i < rows - 1:
            i += 1
            j += 3
            char = lines[i][j % columns]
            if char == "#":
                count += 1
        print(f'Tree Count: {count}')
