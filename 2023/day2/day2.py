def part1():
    with open("day2/input.txt") as input:
        total = 0
        rules = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        for line in input.readlines():
            game_num, hands_str = line.split(":")
            _, game_number = game_num.split(" ")
            hands = hands_str.split(";")
            red, green, blue = [0], [0], [0]
            for hand in hands:
                grabs = hand.split(",")
                for grab in grabs:
                    num, color = grab.strip().split(" ")
                    match color:
                        case "red":
                            red.append(int(num))
                        case "green":
                            green.append(int(num))
                        case "blue":
                            blue.append(int(num))
            red.sort()
            blue.sort()
            green.sort()
            if red[-1] > rules["red"]:
                continue
            if green[-1] > rules["green"]:
                continue
            if blue[-1] > rules["blue"]:
                continue
            total += int(game_number)


def part2():
    with open("day2/input.txt") as input:
        total = 0
        for line in input.readlines():
            game_num, hands_str = line.split(":")
            _, game_number = game_num.split(" ")
            hands = hands_str.split(";")
            red, green, blue = [0], [0], [0]
            for hand in hands:
                grabs = hand.split(",")
                for grab in grabs:
                    num, color = grab.strip().split(" ")
                    match color:
                        case "red":
                            red.append(int(num))
                        case "green":
                            green.append(int(num))
                        case "blue":
                            blue.append(int(num))
            red.sort()
            blue.sort()
            green.sort()
            total += (red[-1] * blue[-1] * green[-1])
        print("d2p2 total: ", total)
