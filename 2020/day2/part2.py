
from typing import List


def main():
    with open('day2/part1input.txt', 'r') as file:
        passwords: List[str] = file.read().splitlines()
        validPasswords = 0
        for rulePassword in passwords:
            rule, password = rulePassword.split(":")
            rule, password = rule.strip(), password.strip()
            indices, targetChar = rule.split(" ")
            firstIndex, secondIndex = indices.split("-")
            firstIndex, secondIndex = int(firstIndex) - 1, int(secondIndex) - 1
            hasFirstChar = password[firstIndex] == targetChar
            hasSecondChar = password[secondIndex] == targetChar
            if hasFirstChar and hasSecondChar:
                continue
            elif hasFirstChar or hasSecondChar:
                validPasswords += 1

        print(f'validPasswords: {validPasswords}')
