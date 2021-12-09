FILE_NAME = 'digits.txt'

_0_SEGMENTS = 'abcefg' # 6
_1_SEGMENTS = 'cf' # 2
_2_SEGMENTS = 'acdeg' # 5
_3_SEGMENTS = 'acdeg' # 5
_4_SEGMENTS = 'bcdf' # 4
_5_SEGMENTS = 'abdfg' # 5
_6_SEGMENTS = 'abdefg' # 6
_7_SEGMENTS = 'acf' # 3
_8_SEGMENTS = 'abcdefg' # 7
_9_SEGMENTS = 'abcdfg' # 6

## PART 1
def count_1_4_7_8_outputs(file):
    count = 0
    for line in file:
        line = line.split(' | ')
        outputs = line[1].split()
        for output in outputs:
            if len(output) in [len(_1_SEGMENTS), len(_4_SEGMENTS), len(_7_SEGMENTS), len(_8_SEGMENTS)]:
                count += 1
    return count

def seven_segment_search_part1():
    file = open(FILE_NAME, 'r')
    count = count_1_4_7_8_outputs(file)
    file.close()
    return count

## PART 2
def get_easy_numbers_encryptions(inputs, encryption_dict):
    inputs_to_remove = []
    for input in inputs:
        if len(input) in [len(_1_SEGMENTS), len(_4_SEGMENTS), len(_7_SEGMENTS), len(_8_SEGMENTS)]:
            inputs_to_remove.append(input)
        if len(input) == len(_1_SEGMENTS):
            encryption_dict[1] = "".join(sorted(input))
        elif len(input) == len(_4_SEGMENTS):
            encryption_dict[4] = "".join(sorted(input))
        elif len(input) == len(_7_SEGMENTS):
            encryption_dict[7] = "".join(sorted(input))
        elif len(input) == len(_8_SEGMENTS):
            encryption_dict[8] = "".join(sorted(input))
    inputs = [input for input in inputs if input not in inputs_to_remove]
    return inputs, encryption_dict

def get_6_chars_numbers_encryption(inputs, encryption_dict):
    # 9
    for input in inputs:
        check_list = [1 for char in encryption_dict[4] if char in input]
        if len(input) == len(_9_SEGMENTS) and len(check_list) == len(encryption_dict[4]):
            encryption_dict[9] = "".join(sorted(input))
            inputs.remove(input)
            break
    # 0
    for input in inputs:
        check_list = [1 for char in encryption_dict[7] if char in input]
        if len(input) == len(_0_SEGMENTS) and len(check_list) == len(encryption_dict[7]):
            encryption_dict[0] = "".join(sorted(input))
            inputs.remove(input)
            break
    
    # 6
    for input in inputs:
        if len(input) == len(_6_SEGMENTS):
            encryption_dict[6] = "".join(sorted(input))
            inputs.remove(input)
            break
    return inputs, encryption_dict

def get_5_chars_numbers_encryption(inputs, encryption_dict):
    # 3
    for input in inputs:
        check_list = [1 for char in encryption_dict[7] if char in input]
        if len(input) == len(_3_SEGMENTS) and len(check_list) == len(encryption_dict[7]):
            encryption_dict[3] = "".join(sorted(input))
            inputs.remove(input)
            break
    
    # 5
    for input in inputs:
        check_list = [1 for char in input if char in encryption_dict[6]]
        if len(input) == len(_5_SEGMENTS) and len(check_list) == len(_5_SEGMENTS):
            encryption_dict[5] = "".join(sorted(input))
            inputs.remove(input)
            break
    
    # 2
    for input in inputs:
        if len(input) == len(_2_SEGMENTS):
            encryption_dict[2] = "".join(sorted(input))
            inputs.remove(input)
            break
    return encryption_dict

def get_output(outputs, encryption_dict):
    output_str = ""
    encryption_keys = list(encryption_dict.keys())
    encryption_values = list(encryption_dict.values())
    for output in outputs:
        output = "".join(sorted(output))
        output_str += str(encryption_keys[encryption_values.index(output)])
        continue
    return int(output_str)

def count_outputs(file):
    count = 0
    for line in file:
        line = line.split(' | ')
        inputs = line[0].split()
        outputs = line[1].split()
        encryption_dict = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
        inputs, encryption_dict = get_easy_numbers_encryptions(inputs, encryption_dict)
        inputs, encryption_dict = get_6_chars_numbers_encryption(inputs, encryption_dict)
        encryption_dict = get_5_chars_numbers_encryption(inputs, encryption_dict)
        count += get_output(outputs, encryption_dict)
    return count

def seven_segment_search_part2():
    file = open(FILE_NAME, 'r')
    count = count_outputs(file)
    file.close()
    return count

## TESTS
### PART 1
print(seven_segment_search_part1()) # 530

### PART 2
print(seven_segment_search_part2()) # 1051087
