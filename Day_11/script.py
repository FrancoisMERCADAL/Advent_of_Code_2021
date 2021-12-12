FILE_NAME = 'dumbo_octopuses.txt'
NB_STEPS = 100

def open_file():
    lines_array = []
    file = open(FILE_NAME, 'r')
    for line in file:
        line = line.strip("\n")
        lines_array.append([int(char) for char in line])
    file.close()
    return lines_array

def is_on_upper_edge(i):
    if i == 0:
        return True
    return False

def is_on_left_edge(k):
    if k == 0:
        return True
    return False

def is_on_down_edge(lines_array, i):
    if i == len(lines_array) - 1:
        return True
    return False

def is_on_right_edge(line, k):
    if k == len(line) - 1:
        return True
    return False

def get_neighbours_coordinates(lines_array, i, k):
    # is on upper edge
    if is_on_upper_edge(i):
        # top left corner
        if is_on_left_edge(k):
            neighbours = [(i, k+1), (i+1, k), (i+1, k+1)]
        # top right corner
        elif is_on_right_edge(lines_array[i], k):
            neighbours = [(i, k-1), (i+1, k), (i+1, k-1)]
        # top edge normal case
        else:
            neighbours = [(i, k-1), (i+1, k), (i, k+1), (i+1, k-1), (i+1, k+1)]
    # is on left edge (normal case)
    elif is_on_left_edge(k) and not is_on_upper_edge(i) and not is_on_down_edge(lines_array, i):
        neighbours = [(i-1, k), (i-1, k+1), (i, k+1), (i+1, k+1), (i+1, k)]
    # is on down edge
    elif is_on_down_edge(lines_array, i):
        # down left corner
        if is_on_left_edge(k):
            neighbours = [(i-1, k), (i-1, k+1), (i, k+1)]
            pass
        # down right corner
        elif is_on_right_edge(lines_array[i], k):
            neighbours = [(i, k-1), (i-1, k-1), (i-1, k)]
        # normal down edge case
        else:
            neighbours = [(i, k-1), (i-1, k-1), (i-1, k), (i-1, k+1), (i, k+1)]
    # is on right edge
    elif is_on_right_edge(lines_array[i], k) and not is_on_upper_edge(i) and not is_on_down_edge(lines_array, i):
        neighbours = [(i+1, k), (i+1, k-1), (i, k-1), (i-1, k-1), (i-1, k)]
    # normal case
    else:
        neighbours = [(i-1, k-1), (i-1, k), (i-1, k+1), (i, k-1), (i, k+1), (i+1, k-1), (i+1, k), (i+1, k+1)]
    return neighbours

def shine_energy(lines_array, i, k, shining_points):
    neighbours = get_neighbours_coordinates(lines_array, i, k)
    for neighbour in neighbours:
        lines_array[neighbour[0]][neighbour[1]] += 1
        if lines_array[neighbour[0]][neighbour[1]] > 9 and (neighbour[0], neighbour[1]) not in shining_points:
            shining_points.append((neighbour[0], neighbour[1]))
            shine_energy(lines_array, neighbour[0], neighbour[1], shining_points)
    return lines_array

def count_shining_points(lines_array):
    count = 0
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            if lines_array[i][k] > 9:
                count += 1
    return count

def first_substep(lines_array):
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            lines_array[i][k] += 1
    return lines_array

def second_substep(lines_array):
    shining_points = []
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            if lines_array[i][k] > 9 and (i, k) not in shining_points:
                shining_points.append((i,k))
                lines_array = shine_energy(lines_array, i, k, shining_points)
                #print(shining_points)
    return lines_array

def third_step(lines_array):
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            if lines_array[i][k] > 9:
                lines_array[i][k] = 0
    return lines_array

def print_octopuses(lines_array):
    for line in lines_array:
        print(''.join(str(i) for i in line))

## PART 1
def dumbo_octopus_part1():
    lines_array = open_file()
    count = 0
    for i in range(NB_STEPS):
        lines_array = first_substep(lines_array)
        lines_array = second_substep(lines_array)
        count += count_shining_points(lines_array)
        lines_array = third_step(lines_array)
    return count

## PART 2
def dumbo_octopus_part2():
    lines_array = open_file()
    steps_count = 0
    flash_count = None
    while flash_count != len(lines_array) * len(lines_array[0]):
        steps_count += 1
        lines_array = first_substep(lines_array)
        lines_array = second_substep(lines_array)
        flash_count = count_shining_points(lines_array)
        lines_array = third_step(lines_array)
    return steps_count

## TESTS 
### PART 1
print(dumbo_octopus_part1()) # 1661

### PART 2
print(dumbo_octopus_part2()) # 334
