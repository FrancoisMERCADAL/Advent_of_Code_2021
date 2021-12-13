FILE_NAME = 'cave_system.txt'

cave_dict = {}
file = open(FILE_NAME, 'r')
for line in file:
    line_array = line.split('-')
    cave_dict[line_array[0]] = [line_array[1].strip('\n')]
file.close()
print(cave_dict)
