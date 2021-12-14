FILE_NAME = 'polymer.txt'
NB_STEPS_PART1 = 10
NB_STEPS_PART2 = 40

def generate_new_polymer(original_polymer, polymer_rules, nb_steps):
    new_polymer = []
    for j in range(nb_steps):
        new_polymer = []
        for i in range(len(original_polymer)-1):
            new_polymer.append(original_polymer[i])
            new_polymer.append(polymer_rules[original_polymer[i] + original_polymer[i+1]])
        new_polymer.append(original_polymer[-1])
        original_polymer = new_polymer
    return original_polymer

def open_file():
    polymer_rules = {}
    file = open(FILE_NAME, 'r')
    original_polymer = [char for char in file.readline()][:-1]
    file.readline()
    for line in file:
        line_array = line.split(' -> ')
        polymer_rules[line_array[0]] = line_array[1].strip('\n')
    file.close()
    return original_polymer, polymer_rules

def array_to_dict(polymer_array):
    polymer_dict = {}
    for char in polymer_array:
        if char not in polymer_dict:
            polymer_dict[char] = 0
        polymer_dict[char] += 1
    return polymer_dict

## PART 1
def extended_polymerization_part1(nb_steps):
    original_polymer, polymer_rules = open_file()
    new_polymer = generate_new_polymer(original_polymer, polymer_rules, nb_steps)
    polymer_dict = array_to_dict(new_polymer)
    dict_values = polymer_dict.values()
    return max(dict_values) - min(dict_values)

## PART 2
def extended_polymerization_part2(nb_steps):
    original_polymer, polymer_rules = open_file()
    dict_pairs = {}
    for i in range(len(original_polymer)-1):
        if original_polymer[i] + original_polymer[i+1] not in dict_pairs:
            dict_pairs[original_polymer[i] + original_polymer[i+1]] = 0
        dict_pairs[original_polymer[i] + original_polymer[i+1]] += 1

    for _ in range(nb_steps+1):
        atoms_counts = {}
        for key in dict_pairs.keys():
            if key[0] not in atoms_counts:
                atoms_counts[key[0]] = 0
            atoms_counts[key[0]] += dict_pairs[key]
        atoms_counts[original_polymer[-1]] += 1

        new_dict_pairs = {}
        for key in dict_pairs.keys():
            new_atom = polymer_rules[key]
            if key[0] + new_atom not in new_dict_pairs:
                new_dict_pairs[key[0] + new_atom] = 0
            if new_atom + key[1] not in new_dict_pairs:
                new_dict_pairs[new_atom + key[1]] = 0
            new_dict_pairs[key[0] + new_atom] += dict_pairs[key]
            new_dict_pairs[new_atom + key[1]] += dict_pairs[key]
        dict_pairs = new_dict_pairs
    dict_values = atoms_counts.values()
    return max(dict_values) - min(dict_values)

## TESTS
### PART 1
print(extended_polymerization_part1(NB_STEPS_PART1)) # 2988

### PART 2
print(extended_polymerization_part2(NB_STEPS_PART2)) # 3572761917024
