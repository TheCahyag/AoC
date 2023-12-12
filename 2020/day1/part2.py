def main():
    with open('day1/part1input.txt', 'r') as file:
        array = file.read().splitlines()
        i, j, k = 0, 0, 0
        for iLine in array:
            for jLine in array:
                for kLine in array:
                    if int(iLine.strip()) + int(jLine.strip()) + int(kLine.strip()) == 2020 and i != j and j != k:
                        print(
                            f'Found it! {iLine} * {jLine} * {kLine} = {int(iLine.strip()) * int(jLine.strip()) * int(kLine.strip())}')
                    k += 1
                j += 1
                k = 0
            i += 1
            j = 0
            k = 0

