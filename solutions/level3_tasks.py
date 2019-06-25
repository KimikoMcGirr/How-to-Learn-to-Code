## Level 3 tasks

# Task 1
def is_nucleic_acid(seq):
    seq = seq.upper()
    na = 'ACTGUWSMKRYBDHVNZ'
    return (all(i in na for i in seq))
# print(is_nucleic_acid('GGhg'))
# print(is_nucleic_acid('GgXG'))

# Task 2
def has_digit(strings_list):
    return [string for string in strings_list if any(char.isdigit() for char in string)]
# print(has_digit(['salknalsd8','ashdas2','asdad']))

# Task 3
def intersects(region1, region2):
    return (region1[0] <= region2[0] <= region1[1]) or (region2[0] <= region1[0] <= region2[1])
# print(intersects([0,5],[3,6]))
