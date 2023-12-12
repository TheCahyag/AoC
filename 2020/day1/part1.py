def main():
    with open('day1/part1input.txt', 'r') as file:
        array = file.read().splitlines()
        i, j = 0, 0
        for iLine in array:
            for jLine in array:
                if int(iLine.strip()) + int(jLine.strip()) == 2020 and i != j:
                    print(
                        f'Found it! {iLine} * {jLine} = {int(iLine.strip()) * int(jLine.strip())}')
                j += 1
            i += 1
            j = 0
