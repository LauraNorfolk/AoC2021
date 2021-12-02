data = open("data.txt")

data_lines = data.read()
list_of_depths = data_lines.split("\n")

def number_of_increases(data):
    comparator = 0
    counter = 0
    is_first = True

    for depth in data:
        depth = int(depth.strip())
        if is_first:
            is_first = False
            continue

        if depth > comparator:
            counter += 1
        comparator = depth

    return counter


def sliding_window_increases(list_of_depths):
    previous_window = 0
    current_window = 0
    counter = 0

    for i in range(len(list_of_depths)):
        if i < 2:
            continue

        elif i == 2:
            previous_window = int(list_of_depths[i]) + int(list_of_depths[i-1]) + int(list_of_depths[i-2])

        else:
            current_window = int(list_of_depths[i]) + int(list_of_depths[i-1]) + int(list_of_depths[i-2])

            if current_window > previous_window:
                counter += 1
            previous_window = current_window


    return counter

print(sliding_window_increases(list_of_depths))