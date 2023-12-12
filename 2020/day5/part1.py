def base2tobase10(input: str) -> int:
    i = len(input) - 1
    total = 0
    for char in input:
        if char == '1':
            total += 2**i
        i -= 1
    return total


def main():
    with open("day5/part1input.txt", "r") as file:
        lines = file.read().splitlines()
        highest = -1
        for line in lines:
            row = line[0:7]
            column = line[7:10]
            rowInt = base2tobase10(row.replace("B", "1").replace("F", "0"))
            columnInt = base2tobase10(
                column.replace("R", "1").replace("L", "0"))
            seatId = rowInt * 8 + columnInt
            if seatId > highest:
                highest = seatId
        print(f"Highest: {highest}")
