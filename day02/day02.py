file = open('input', 'r')
lines = file.readlines()


def part_1():
    depth = 0
    distance = 0
    for line in lines:
        input = line.split(" ")
        action = input[0]
        value = int(input[1])

        if action == "forward":
            distance += value
        elif action == "up":
            depth -= value
        elif action == "down":
            depth += value
    print(depth * distance)


def part_2():
    depth = 0
    distance = 0
    aim = 0
    for line in lines:
        input = line.split(" ")
        action = input[0]
        value = int(input[1])

        if action == "forward":
            distance += value
            depth = depth + (aim * value)
        elif action == "up":
            aim -= value
        elif action == "down":
            aim += value
    print(depth * distance)


part_1()
part_2()
