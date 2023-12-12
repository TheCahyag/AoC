from typing import Dict


def main():
    with open("day6/part1input.txt", "r") as file:
        lines = file.read().splitlines()
        answers = {}
        total = 0
        for line in lines:
            strippedLine = line.strip()
            if strippedLine == "":
                total += len(answers.keys())
                answers: Dict[str, int] = {}
            else:
                for char in strippedLine:
                    if char in answers.keys():
                        value = int(answers.get(char)) + 1
                        answers[char] = value
                    else:
                        answers[char] = 1
        total += len(answers.keys())
        print(f"Day 6 total: {total}")
