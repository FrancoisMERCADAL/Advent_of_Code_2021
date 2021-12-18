FILE_NAME = 'risk_points.txt'

def open_file():
    lines_array = []
    file = open(FILE_NAME, 'r')
    for line in file:
        lines_array.append([int(char) for char in line.strip('\n')])
    file.close()
    return lines_array

def get_neighbours(lines_array, i, k):
    neighbours = []
    ## upper edge
    if i == 0:
        ## upper left corner
        if k == 0:
            neighbours = [(i,k+1), (i+1,k)]
        ## upper right corner
        elif k == len(lines_array[i]) - 1:
            neighbours = [(i,k-1), (i+1,k)]
        ## normal upper edge
        else:
            neighbours = [(i,k-1),(i,k+1),(i+1,k)]
    ## down edge
    elif i == len(lines_array) - 1:
        ## down left corner
        if k == 0:
            neighbours = [(i-1,k), (i,k+1)]
        ## down right corner
        elif k == len(lines_array[i]) - 1:
            neighbours = [(i-1,k),(i,k-1)]
        ## normal down edge
        else:
            neighbours = [(i,k-1),(i,k+1),(i-1,k)]
    ## normal left edge
    elif k == 0 and i not in [0, len(lines_array)-1]:
        neighbours = [(i-1,k), (i,k+1), (i+1,k)]
    ## right edge
    elif k == len(lines_array[i]) - 1 and i not in [0, len(lines_array)-1]:
        neighbours = [(i-1,k), (i,k-1), (i+1,k)]
    else:
        neighbours = [(i-1,k), (i,k-1), (i,k+1), (i+1,k)]
    return neighbours

def chiton_part1():
    lines_array = open_file()
    costs_array = [[1000000 for i in range(len(lines_array[0]))] for k in range(len(lines_array))]
    for i in range(len(lines_array)):
        for k in range(len(lines_array[i])):
            if i == 0 and k == 0:
                costs_array[0][0] = lines_array[i][k]
            else:
                costs = []
                neighbours = get_neighbours(lines_array, i, k)
                for neighbour in neighbours:
                    costs.append(lines_array[i][k] + costs_array[neighbour[0]][neighbour[1]])
                costs_array[i][k] = min(costs)
                # perform a relaxation
                # recalculate costs for each neighbour
                spots_to_recalculate = get_neighbours(lines_array, i, k)
                relaxed_points = []
                while len(spots_to_recalculate) != 0:
                    costs = []
                    spot = spots_to_recalculate.pop(0)
                    check_neighbours = get_neighbours(lines_array, spot[0], spot[1])
                    for neighbour in check_neighbours:
                        costs.append(lines_array[spot[0]][spot[1]] + costs_array[neighbour[0]][neighbour[1]])
                    min_cost = min(costs)
                    if min_cost < costs_array[spot[0]][spot[1]] and (spot[0], spot[1]) not in relaxed_points:
                        costs_array[spot[0]][spot[1]] = min_cost
                        #spots_to_recalculate += get_neighbours(lines_array, spot[0], spot[1])
                    relaxed_points.append((spot[0], spot[1]))
    return costs_array[len(lines_array)-1][-1]

## TESTS
### PART 1
print(chiton_part1()) # 362

### PART 2
