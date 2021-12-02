FILE_NAME = 'measures.txt'

## PART 1
def count_increases(file):
    reference_val = None
    count = 0
    for line in file:
        if reference_val == None:
            pass
        elif int(line) > reference_val:
            count += 1
        reference_val = int(line)
    return count

def sonar_sweep_part1():
    file = open(FILE_NAME, "r")
    count = count_increases(file)
    file.close()
    return count

## PART 2
def count_increases_2(file):
    sum_array = []
    window_size = 3
    index_array = 0
    index_file = 0
    count = 0
    for line in file:
        sum_array.append([])
        if index_file < window_size - 1:
            if index_file < window_size - 2:
                sum_array[index_file].append(int(line))
            else:
                sum_array[index_file - 1].append(int(line))
                sum_array[index_file].append(int(line))
        else:
            sum_array[index_file - 2].append(int(line))
            sum_array[index_file - 1].append(int(line))
            sum_array[index_file].append(int(line))

            if len(sum_array[index_array]) == window_size and len(sum_array[index_array + 1]) == window_size:
                if sum(sum_array[index_array + 1]) > sum(sum_array[index_array]):
                    count += 1
                index_array += 1
        index_file += 1
    return count

def sonar_sweep_part2():
    file = open(FILE_NAME, "r")
    count = count_increases_2(file)
    file.close()
    return count

## TESTS
### PART 1
#print(sonar_sweep_part1()) # 1529

### PART 2
#print(sonar_sweep_part2()) # 1567
