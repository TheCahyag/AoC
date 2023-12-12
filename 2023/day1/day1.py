def part1():
    with open("day1/input.txt") as input:
        total: int = 0
        for line in input.readlines():
            nums = [x for x in line if x.isdigit()]
            str_total = ""
            str_total += nums[0]
            str_total += nums[-1]
            total += int(str_total)

        print(f"total: {total}")


def part2():
    with open("day1/sampleinput.txt") as input:
        total: int = 0
        for line in input.readlines():
            newline = replace_nums(line)
            nums = [x for x in newline if x.isdigit()]
            str_total = ""
            str_total += nums[0]
            str_total += nums[-1]
            total += int(str_total)
        print(f"total: {total}")


def replace_nums(line: str):
    replace_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    substring = ""
    newline = line
    for char in line:
        substring += char
        for key in replace_dict.keys():
            if key in substring:
                newline = newline.replace(key, replace_dict[key])
                substring = ""
    return newline
