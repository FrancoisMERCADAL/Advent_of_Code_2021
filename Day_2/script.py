FILE_NAME = 'commands.txt'
TRAJECTORY_DICT = {
    'up': -1,
    'down': 1
}

## PART 1
def calculate_product(file):
    depth = 0
    horizontal_position = 0
    for line in file:
        command = line.split()
        if command[0] == 'forward':
            horizontal_position += int(command[1])
        elif command[0] in ['down', 'up']:
            depth += TRAJECTORY_DICT[command[0]] * int(command[1])
        else:
            pass
    return depth * horizontal_position

def dive_part1():
    file = open(FILE_NAME, "r")
    product = calculate_product(file)
    file.close()
    return product

## PART 2
def recalculate_product(file):
    depth = 0
    horizontal_position = 0
    aim = 0
    for line in file:
        command = line.split()
        if command[0] in ['down', 'up']:
            aim += TRAJECTORY_DICT[command[0]] * int(command[1])
        elif command[0] == 'forward':
            horizontal_position += int(command[1])
            depth += aim * int(command[1])
    return horizontal_position * depth

def dive_part2():
    file = open(FILE_NAME, "r")
    product = recalculate_product(file)
    file.close()
    return product

## TESTS
### PART 1
#print(dive_part1()) # 1882980

### PART 2
#print(dive_part2()) # 1971232560
