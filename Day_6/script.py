FILE_NAME = 'fishes.txt'
NB_DAYS_PART1 = 80
NB_DAYS_PART2 = 256

def open_file():
    file = open(FILE_NAME, 'r')
    fishes = file.readline().split(',')
    fishes = [int(fish) for fish in fishes]
    file.close()
    return fishes

def lanternfish(nb_days):
    fishes = open_file()

    fishes_dict = {}
    for fish in fishes:
        if fish not in fishes_dict:
            fishes_dict[fish] = 1
        else:
            fishes_dict[fish] += 1

    for day in range(nb_days):
        dictionary = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
        for key, value in fishes_dict.items():
            if key == 0:
                dictionary[6] += value
                dictionary[8] += value
            else:
                dictionary[key-1] += value
        fishes_dict = dictionary
    return sum(fishes_dict.values())

## TESTS
### PART 1
print(lanternfish(NB_DAYS_PART1)) # 350149

### PART 2
print(lanternfish(NB_DAYS_PART2)) # 1590327954513
