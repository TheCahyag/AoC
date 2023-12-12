import re
from typing import List, Optional


class Passport:

    def __init__(self, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def _byr_valid(self) -> bool:
        if self.byr is None:
            return False
        return 1920 <= int(self.byr) <= 2002

    def _iyr_valid(self) -> bool:
        if self.iyr is None:
            return False
        return 2010 <= int(self.iyr) <= 2020

    def _eyr_valid(self) -> bool:
        if self.eyr is None:
            return False
        return 2020 <= int(self.eyr) <= 2030

    def _hgt_valid(self) -> bool:
        if self.hgt is None:
            return False
        measure = self.hgt[-2:]
        if measure == "in":
            return 59 <= int(self.hgt[0:len(self.hgt) - 2]) <= 76
        elif measure == "cm":
            return 150 <= int(self.hgt[0:len(self.hgt) - 2]) <= 193
        return False

    def _hcl_valid(self) -> bool:
        if self.hcl is None:
            return False
        if self.hcl[0] == "#" and len(self.hcl) == 7:
            if re.search("([0-9a-fA-F]{6})", self.hcl[1:7]):
                return True
        return False

    def _ecl_valid(self) -> bool:
        if self.ecl is None:
            return False
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def _pid_valid(self) -> bool:
        if self.pid is None:
            return False
        return len(self.pid) == 9

    def hasRequiredFields(self) -> bool:
        return self._byr_valid() and self._iyr_valid() and self._eyr_valid() and self._hgt_valid() and self._hcl_valid() and self._ecl_valid() and self._pid_valid()

    def __str__(self) -> str:
        return f"Passport: byr={self.byr}, iyr={self.iyr}, eyr={self.eyr}, hgt={self.hgt}, hcl={self.hcl}, ecl={self.ecl}, pid={self.pid}, cid={self.cid}"


def main():
    with open("day4/part1input.txt", "r") as file:
        lines: List[str] = file.read().splitlines()
        passports: List[Passport] = []
        params: dict = {}
        for line in lines:
            if line.strip() == "":
                passport = Passport(**params)
                passports.append(passport)
                params = {}
                continue

            parseThese: List[str] = line.split(" ")
            for this in parseThese:
                key, value = this.split(":")
                params[key] = value
        count = 0
        for passport in passports:
            if passport.hasRequiredFields():
                count += 1
        print(f"Total valid passports: {count}")


if __name__ == "__main__":
    passport = Passport('1994', '2010', '2021', '70in',
                        '#b6652a', 'blu', '093154719')
    print(f"byr: {passport._byr_valid()}")
    print(f"iyr: {passport._iyr_valid()}")
    print(f"eyr: {passport._eyr_valid()}")
    print(f"hgt: {passport._hgt_valid()}")
    print(f"hcl: {passport._hcl_valid()}")
    print(f"ecl: {passport._ecl_valid()}")
    print(f"pid: {passport._pid_valid()}")
