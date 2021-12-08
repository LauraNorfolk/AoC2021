
def parse_data():
    commands = open("commands.txt")

    command_lines = commands.read()
    list_of_commands = command_lines.split("\n")

    return list_of_commands

def calculate_sub_position_1(list_of_commands):
    depth = 0
    forward_position = 0

    for command in list_of_commands:
        split_command = command.split(" ")
        if split_command[0] == "forward":
            forward_position += int(split_command[1])

        elif split_command[0] == "down":
            depth += int(split_command[1])

        elif split_command[0] == "up":
            depth -= int(split_command[1])

    print(depth)
    print(forward_position)
    print(depth * forward_position)


def calculate_sub_position_2(list_of_commands):
    depth = 0
    forward_position = 0
    aim = 0

    for command in list_of_commands:
        split_command = command.split(" ")
        if split_command[0] == "down":
            aim += int(split_command[1])

        elif split_command[0] == "up":
            aim -= int(split_command[1])

        elif split_command[0] == "forward":
            forward_position += int(split_command[1])
            depth += (aim * int(split_command[1]))

    print(depth)
    print(forward_position)
    print(depth * forward_position)

calculate_sub_position_2(parse_data())



