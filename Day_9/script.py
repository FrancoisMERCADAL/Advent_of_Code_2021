FILE_NAME = 'heightmap.txt'

def open_file():
    file = open(FILE_NAME, 'r')
    lines_array = []
    for line in file:
        lines_array.append(line.strip('\n'))
    file.close()
    return lines_array

def is_on_top_edge(i):
    if i == 0:
        return True
    return False

def is_on_left_edge(k):
    if k == 0:
        return True
    return False

def is_on_right_edge(line, k):
    if k == len(line) - 1:
        return True
    return False

def is_on_down_edge(lines_array, i):
    if i == len(lines_array) - 1:
        return True
    return False

def get_comparison_values(lines_array, i, k):
    if is_on_top_edge(i):
        # up-left corner case
        if is_on_left_edge(k):
            comparison_values = [int(lines_array[i+1][k]), int(lines_array[i][k+1])]
            indexes = [(i+1,k), (i, k+1)]
        # up-right edge case
        elif is_on_right_edge(lines_array[i], k):
            comparison_values = [int(lines_array[i+1][k]), int(lines_array[i][k-1])]
            indexes = [(i+1, k), (i, k-1)]
        # normal edge on top case
        else:
            comparison_values = [int(lines_array[i][k-1]), int(lines_array[i][k+1]), int(lines_array[i+1][k])]
            indexes = [(i, k-1), (i, k+1), (i+1, k)]
    # normal left-edge case
    elif is_on_left_edge(k) and not is_on_top_edge(i) and not is_on_down_edge(lines_array, i):
        comparison_values = [int(lines_array[i-1][k]), int(lines_array[i+1][k]), int(lines_array[i][k+1])]
        indexes = [(i-1, k), (i+1, k), (i, k+1)]
    elif is_on_down_edge(lines_array, i):
        # down-left corner case
        if is_on_left_edge(k):
            comparison_values = [int(lines_array[i-1][k]), int(lines_array[i][k+1])]
            indexes = [(i-1, k), (i, k+1)]
        # up-right corner case
        elif is_on_right_edge(lines_array[i], k):
            comparison_values = [int(lines_array[i-1][k]), int(lines_array[i][k-1])]
            indexes = [(i-1, k), (i, k-1)]
        # normal down edge case
        else:
            comparison_values = [int(lines_array[i-1][k]), int(lines_array[i][k+1]), int(lines_array[i][k-1])]
            indexes = [(i-1, k), (i, k+1), (i, k-1)]
    # normal right-edge case
    elif is_on_right_edge(lines_array[i], k) and not is_on_top_edge(i) and not is_on_down_edge(lines_array, i):
        comparison_values = [int(lines_array[i-1][k]), int(lines_array[i][k-1]), int(lines_array[i+1][k])]
        indexes = [(i-1, k), (i, k-1), (i+1, k)]
    # normal case with 4 neighbours
    else:
        comparison_values = [int(lines_array[i-1][k]), int(lines_array[i+1][k]), int(lines_array[i][k-1]), int(lines_array[i][k+1])]
        indexes = [(i-1, k), (i+1, k), (i, k-1), (i, k+1)]
    return comparison_values, indexes

def is_low_point(pointed_value, comparison_values):
    if pointed_value < min(comparison_values) and comparison_values.count(pointed_value) == 0:
        return True
    return False

## PART 1
def get_risk_level():
    lines_array = open_file()
    risk_levels = 0
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            pointed_value = int(lines_array[i][k])
            comparison_values, indexes = get_comparison_values(lines_array, i, k)
            if is_low_point(pointed_value, comparison_values):
                risk_levels += 1 + pointed_value
    return risk_levels

def smoke_bassin_part1():
    risk_level = get_risk_level()
    return risk_level

## PART 2
def get_lake(comparison_values, indexes, pointed_value, lines_array, i, k, size):
    for j in range(len(comparison_values)):
        if comparison_values[j] == pointed_value+1:
            new_comparison_values, new_indexes = get_comparison_values(lines_array, indexes[j][0], indexes[j][1])
            size += 1
            print(comparison_values[j], new_comparison_values, new_indexes)
            get_lake(new_comparison_values, new_indexes, comparison_values[j], lines_array, indexes[j][0], indexes[j][1], size)
        return size

lines_array = open_file()
bassins_sizes = []
for i in range(len(lines_array)):
    for k in range(len(lines_array[i])):
        pointed_value = int(lines_array[i][k])
        comparison_values, indexes = get_comparison_values(lines_array, i, k)
        if is_low_point(pointed_value, comparison_values):
            bassins_sizes.append(get_lake(comparison_values, indexes, pointed_value, lines_array, i, k, 1))
print(bassins_sizes)
## TESTS
### PART 1
#print(smoke_bassin_part1()) # 486

### PART 2
