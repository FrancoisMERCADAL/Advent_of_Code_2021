FILE_NAME = 'diagnostic_report.txt'
LINE_LENGTH = 12

def binary_to_decimal(array):
    decimal = 0
    for i in range(len(array)):
        decimal += array[i] * 2**(len(array) - i - 1)
    return decimal

## PART 1
def calculate_power_consumption(file):
    diagnostic_report_length = 0
    count_ones = [0] * LINE_LENGTH
    for line in file:
        diagnostic_report_length += 1
        for i in range(len(line)):
            if line[i] == '1':
                count_ones[i] += 1
    gamma_rate = [1 if nb/diagnostic_report_length > 0.5 else 0 for nb in count_ones]
    epsilon_rate = [0 if nb/diagnostic_report_length > 0.5 else 1 for nb in count_ones]
    gamma_rate = binary_to_decimal(gamma_rate)
    epsilon_rate = binary_to_decimal(epsilon_rate)
    return gamma_rate * epsilon_rate

def binary_diagnotic_part1():
    file = open(FILE_NAME, "r")
    power_consumption = calculate_power_consumption(file)
    file.close()
    return power_consumption

## PART 2
def calculate_oxygen_generator_rating(oxygen_generator_rating_array):
    index = 0
    char_selected = None
    while len(oxygen_generator_rating_array) > 1:
        count_ones = 0
        for i in range(len(oxygen_generator_rating_array)):
            if oxygen_generator_rating_array[i][index] == '1':
                count_ones += 1
        if count_ones/len(oxygen_generator_rating_array) >= 0.5:
            char_selected = '1'
        else:
            char_selected = '0'
        oxygen_generator_rating_array = [line for line in oxygen_generator_rating_array if line[index] == char_selected]
        index += 1
    return binary_to_decimal(list(map(int, oxygen_generator_rating_array[0][:-1])))

def calculate_co2_scrubber_rating(co2_scrubber_rating_array):
    index = 0
    char_selected = None
    while len(co2_scrubber_rating_array) > 1:
        count_ones = 0
        for i in range(len(co2_scrubber_rating_array)):
            if co2_scrubber_rating_array[i][index] == '1':
                count_ones += 1
        if count_ones/len(co2_scrubber_rating_array) >= 0.5:
            char_selected = '0'
        else:
            char_selected = '1'
        co2_scrubber_rating_array = [line for line in co2_scrubber_rating_array if line[index] == char_selected]
        index += 1
    return binary_to_decimal(list(map(int, co2_scrubber_rating_array[0][:-1])))

def calculate_life_support_rating(file):
    binary_array = []
    for line in file:
        binary_array.append(line)
    oxygen_generator_rating_array = binary_array
    co2_scrubber_rating_array = binary_array

    oxygen_generator_rating = calculate_oxygen_generator_rating(oxygen_generator_rating_array)
    co2_scrubber_rating = calculate_co2_scrubber_rating(co2_scrubber_rating_array)
    return oxygen_generator_rating * co2_scrubber_rating

def binary_diagnostic_part2():
    file = open(FILE_NAME, "r")
    life_support_rating = calculate_life_support_rating(file)
    file.close()
    return life_support_rating

## TESTS
### PART 1
#print(binary_diagnotic_part1()) # 3958484

### PART 2
#print(binary_diagnostic_part2()) # 1613181
