

from typing import Dict, List


class BagWithQuantity:
    color: str
    quantity: int

    def __init__(self, color: str, quantity):
        self.color = color.replace("bags", "").replace("bag", "").strip()
        self.quantity = quantity

    def __str__(self):
        return f"color: {self.color}, quantity: {self.quantity}"

    def __repr__(self):
        return f"color: {self.color}, quantity: {self.quantity}"


def hasTarget(target, bags: List[BagWithQuantity], map: Dict[str, BagWithQuantity]) -> bool:
    if len(bags) == 0:
        return False
    else:
        if len([x for x in bags if x.color == target]):
            return True
        else:
            for bag in bags:
                if bag.color in map.keys():
                    return hasTarget(target, map.get(bag.color), map)
            print("shouldn't be here")
            return False


def main():
    with open("day7/part1input.txt", "r") as file:
        lines = file.read().splitlines()
        rules: Dict[str, List[BagWithQuantity]] = {}
        for line in lines:
            bag, others = line.split("contain")
            bags: List[BagWithQuantity] = []
            mapping = others.split(",")
            for map in mapping:
                quantity, color = map.strip().split(" ", maxsplit=1)
                if quantity != "no":
                    bags.append(BagWithQuantity(color.strip("."), quantity))

            rules[bag.replace("bags", "").replace("bag", "").strip()] = bags
        target = "shiny gold"
        targetCount = 0
        for v in rules.values():
            if hasTarget(target, v, rules):
                targetCount += 1
        print(
            f"Count: {targetCount}, rules len: {len(rules.keys())}, rules: {rules}")
