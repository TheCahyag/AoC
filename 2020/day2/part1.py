
from typing import List


def main():
    with open('day2/part1input.txt', 'r') as file:
        passwords: List[str] = file.read().splitlines()
        validPasswords = 0
        for rulePassword in passwords:
            rule, password = rulePassword.split(":")
            rule, password = rule.strip(), password.strip()
            minMax, targetChar = rule.split(" ")
            minChar, maxChar = minMax.split("-")
            min, max = int(minChar), int(maxChar)
            count = password.count(targetChar)
            if min <= count <= max:
                validPasswords += 1
        print(f'validPasswords: {validPasswords}')
