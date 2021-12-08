FILE_NAME = 'crabs.txt'

def open_read_file():
    file = open(FILE_NAME, 'r')
    line = list(map(int, file.readline().split(',')))
    file.close()
    return line

## PART 1
def treachery_of_whales_part1():
    from statistics import median
    fuel_count = 0
    crabs_positions = open_read_file()
    median = int(median(crabs_positions))
    for pos in crabs_positions:
        fuel_count += abs(pos - median)
    return fuel_count

## PART 2
def define_fuel_consumption_per_distance(max_crab_position):
    fuel_consumption_per_distance = {0:0}
    for i in range(1,max_crab_position+1):
        fuel_consumption_per_distance[i] = i + fuel_consumption_per_distance[i-1]
    return fuel_consumption_per_distance

def treachery_of_whales_part2():
    from statistics import mean
    count_fuel = 0
    crabs_positions = open_read_file()
    max_crab_position = max(crabs_positions)
    fuel_consumption_per_distance = define_fuel_consumption_per_distance(max_crab_position)
    mean_position = int(mean(crabs_positions))
    for crab in crabs_positions:
        count_fuel += fuel_consumption_per_distance[abs(crab - mean_position)]
    return count_fuel

## TESTS
### PART 1
print(treachery_of_whales_part1()) # 344605

### PART 2
print(treachery_of_whales_part2()) # 9369985
