FILE_NAME = 'coordinates.txt'

def open_file():
    coordinates = []
    folds = []
    file = open(FILE_NAME, 'r')
    for line in file:
        if line == '\n':
            break
        else:
            line_array = line.split(',')
            coordinates.append([int(line_array[0]), int(line_array[1].strip('\n'))])
    for line in file:
        line_array = line.split('=')
        folds.append((line_array[0][-1], int(line_array[1].strip('\n'))))
    file.close()
    return coordinates, folds

def fold_on_x(coordinates, x):
    for i in range(len(coordinates)):
        if coordinates[i][0] > x:
            coordinates[i][0] = (2*x) - coordinates[i][0]
    return coordinates

def fold_on_y(coordinates, y):
    for i in range(len(coordinates)):
        if coordinates[i][1] > y:
            coordinates[i][1] = (2*y) - coordinates[i][1]
            pass
    return coordinates

def count_nb_dots(coordinates):
    check_dict = {}
    for coordinate in coordinates:
        key = f'{coordinate[0]},{coordinate[1]}'
        if key not in check_dict:
            check_dict[key] = 1
    return len(check_dict.keys())

def return_tranparent_paper(coordinates):
    screen_lines = ["." * 50] * 7
    for coordinate in coordinates:
        pass
        screen_lines[coordinate[1]] = screen_lines[coordinate[1]][:coordinate[0]] + '#' + screen_lines[coordinate[1]][coordinate[0]+1:]
    return screen_lines

def display_screen(screen_lines):
    for line in screen_lines:
        print(line)
    return None

## PART 1
def transparent_origami_part1():
    coordinates, folds = open_file()
    first_fold = folds[0]
    if first_fold[0] == 'x':
        coordinates = fold_on_x(coordinates, first_fold[1])
    else:
        coordinates = fold_on_y(coordinates, first_fold[1])
    return count_nb_dots(coordinates)

## PART 2
def transparent_origami_part2():
    coordinates, folds = open_file()
    for fold in folds:
        if fold[0] == 'x':
            coordinates = fold_on_x(coordinates, fold[1])
        else:
            coordinates = fold_on_y(coordinates, fold[1])
    screen_lines = return_tranparent_paper(coordinates)
    display_screen(screen_lines)

## TESTS
### PART 1
print(transparent_origami_part1()) # 731

### PART 2
transparent_origami_part2() # ZKAUCFUC
