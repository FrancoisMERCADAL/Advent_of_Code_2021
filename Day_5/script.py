FILE_NAME = 'vents.txt'

def extract_data_from_line(line):
    line = line.split(' -> ')
    line[1] = line[1].replace('\n', '')
    x1_y1 = line[0].split(',')
    x2_y2 = line[1].split(',')
    return int(x1_y1[0]), int(x1_y1[1]), int(x2_y2[0]), int(x2_y2[1])

def count_interest_keys_from_dictionary(dictionary):
    count = 0
    for key in dictionary:
        if dictionary[key] >= 2:
            count += 1
    return count

def same_x_update_dict(x1, y1, x2, y2, points_dictionary):
    y1_y2 = [y1, y2]
    y1_y2.sort()
    columns = list(range(y1_y2[0], y1_y2[1]+1))
    for column in columns:
        key = f'{x1},{column}'
        if key in points_dictionary:
            points_dictionary[key] += 1
        else:
            points_dictionary[key] = 1
    return points_dictionary

def same_y_update_dict(x1, y1, x2, y2, points_dictionary):
    x1_x2 = [x1, x2]
    x1_x2.sort()
    lines = list(range(x1_x2[0], x1_x2[1]+1))
    for line in lines:
        key = key = f'{line},{y1}'
        if key in points_dictionary:
            points_dictionary[key] += 1
        else:
            points_dictionary[key] = 1
    return points_dictionary

def diagonal_case_update_dict(x1, y1, x2, y2, coefficient, points_dictionary):
    x1_x2, y1_y2 = [x1, x2], [y1, y2]
    x1_x2.sort()
    y1_y2.sort()
    lines = list(range(x1_x2[0], x1_x2[1]+1))
    columns = list(range(y1_y2[0], y1_y2[1]+1))
    if coefficient == -1:
        columns.reverse()
    for line, column in zip(lines, columns):
        key = f'{line},{column}'
        if key in points_dictionary:
            points_dictionary[key] += 1
        else:
            points_dictionary[key] = 1
    return points_dictionary

## PART 1
def count_overlap_lines_1(file):
    points_dictionary = {}
    for line in file:
        x1, y1, x2, y2 = extract_data_from_line(line)
        if x1 == x2:
            points_dictionary = same_x_update_dict(x1, y1, x2, y2, points_dictionary)
        elif y1 == y2:
            points_dictionary = same_y_update_dict(x1, y1, x2, y2, points_dictionary)
        else:
            continue
    count = count_interest_keys_from_dictionary(points_dictionary)
    return count

def hydrothermal_venture_part1():
    file = open(FILE_NAME, 'r')
    count = count_overlap_lines_1(file)
    file.close()
    return count

## PART 2
def count_overlap_lines_2(file):
    points_dictionary = {}
    for line in file:
        x1, y1, x2, y2 = extract_data_from_line(line)
        if x1 == x2:
            points_dictionary = same_x_update_dict(x1, y1, x2, y2, points_dictionary)
        elif y1 == y2:
            points_dictionary = same_y_update_dict(x1, y1, x2, y2, points_dictionary)
        else:
            coefficient = (y2 - y1)/(x2 - x1)
            if coefficient in [-1, 1]:
                points_dictionary = diagonal_case_update_dict(x1, y1, x2, y2, coefficient, points_dictionary)
    return count_interest_keys_from_dictionary(points_dictionary)

def hydrothermal_venture_part2():
    file = open(FILE_NAME, 'r')
    count = count_overlap_lines_2(file)
    file.close()
    return count

## TESTS
### PART 1
print(hydrothermal_venture_part1()) # 7269

### PART 2
print(hydrothermal_venture_part2()) # 21140
