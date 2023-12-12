from typing import Dict


def main():
    with open("day6/part1input.txt", "r") as file:
        lines = file.read().splitlines()
        answers = {}
        total = 0
        group_size = 0
        for line in lines:
            strippedLine = line.strip()
            if strippedLine == "":
                everyone_answered = [
                    x for x in answers.values() if int(x) == group_size]
                total += len(everyone_answered)
                answers: Dict[str, int] = {}
                group_size = 0
            else:
                group_size += 1
                for char in strippedLine:
                    if char in answers.keys():
                        value = int(answers.get(char)) + 1
                        answers[char] = value
                    else:
                        answers[char] = 1

        everyone_answered = [
            x for x in answers.values() if int(x) == group_size]
        total += len(everyone_answered)
        print(f"Day 6 total: {total}")
