if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_02.txt') as f:
        file_data = f.read()
    input_list = [x.split(" ") for x in file_data.split('\n')]

    horizontal_position = 0
    depth = 0

    for command, value in input_list:
        value = int(value)
        if command == "forward":
            horizontal_position += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value
    print(f"Answer to part 1: {horizontal_position * depth}")

    horizontal_position = 0
    depth = 0
    aim = 0

    for command, value in input_list:
        value = int(value)
        if command == "forward":
            horizontal_position += value
            depth += aim * value
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value
    print(f"Answer to part 2: {horizontal_position * depth}")
