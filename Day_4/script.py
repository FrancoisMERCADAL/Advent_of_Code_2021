FILE_NAME = 'inputs.txt'

def open_file():
    bingo_tables = []
    table = []
    file = open(FILE_NAME, 'r')
    numbers = file.readline().split(',')
    file.readline()
    for line in file:
        if line == '\n':
            bingo_tables.append(table)
            table = []
        else:
            table.append(line.split())
    bingo_tables.append(table)
    file.close()
    return numbers, bingo_tables

def check_if_line_is_complete(line):
    check_array = [1 if '.' in char else 0 for char in line]
    if check_array == [1] * len(line):
        return True
    else:
        return False

def check_if_column_is_complete(table, column_index):
    check_array = [1 if '.' in line[column_index] else 0 for line in table]
    if check_array == [1] * len(table):
        return True
    else:
        return False

def check_if_table_has_complete_line(table):
    has_complete_line = None
    for line in table:
        has_complete_line = check_if_line_is_complete(line)
        if has_complete_line == True:
            return True
    return False

def check_if_table_has_complete_column(table):
    has_complete_column = None
    for index in range(len(table[0])):
        has_complete_column = check_if_column_is_complete(table, index)
        if has_complete_column == True:
            return True
    return False

def sum_unmarked_values(table):
    values_to_sum = []
    for line in table:
        values_to_sum += [int(char) if '.' not in char else 0 for char in line]
    return sum(values_to_sum)

## PART 1
def get_final_score():
    numbers, bingo_tables = open_file()
    for index_nb in range(len(numbers)): # numbers in list
        for index_table in range(len(bingo_tables)): # for loop in tables
            for index_line in range(len(bingo_tables[index_table])): # in a table: for loop in lines
                for index_char in range(len(bingo_tables[index_table][index_line])): # in a line: for loop in the chars
                    if bingo_tables[index_table][index_line][index_char] == numbers[index_nb]:
                        bingo_tables[index_table][index_line][index_char] += '.'
                        # check if table has complete line or column
                        has_complete_line = check_if_table_has_complete_line(bingo_tables[index_table])
                        has_complete_column = check_if_table_has_complete_column(bingo_tables[index_table])
                        if True in [has_complete_line, has_complete_column]:
                            # Calculate
                            values_to_sum = sum_unmarked_values(bingo_tables[index_table])
                            return values_to_sum * int(numbers[index_nb])

## PART 2
def get_final_score_part2():
    winning_tables = []
    numbers, bingo_tables = open_file()
    original_bingo_tables_length = len(bingo_tables)
    for index_nb in range(len(numbers)): # numbers in list
        for index_table in range(len(bingo_tables)): # for loop in tables
            for index_line in range(len(bingo_tables[index_table])): # in a table: for loop in lines
                for index_char in range(len(bingo_tables[index_table][index_line])): # in a line: for loop in the chars
                    if bingo_tables[index_table][index_line][index_char] == numbers[index_nb]:
                        bingo_tables[index_table][index_line][index_char] += '.'
                        # check if table has complete line or column
                        has_complete_line = check_if_table_has_complete_line(bingo_tables[index_table])
                        has_complete_column = check_if_table_has_complete_column(bingo_tables[index_table])
                        if True in [has_complete_line, has_complete_column] and index_table not in winning_tables:
                            if len(winning_tables) != original_bingo_tables_length - 1:
                                winning_tables.append(index_table)
                                break
                            else:
                                # Calculate
                                sum_values = sum_unmarked_values(bingo_tables[index_table])
                                return sum_values * int(numbers[index_nb])

## TESTS
### PART 1
#print(get_final_score()) # 27027

### PART 2
#print(get_final_score_part2()) # 36975
