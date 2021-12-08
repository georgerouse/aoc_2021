import difflib

def get_mapping_dict(records):
    mapping = {}

    records = [''.join(sorted(x)) for x in records]
    for record in records:
        if len(record) == 2:
            mapping[1] = record
        elif len(record) == 4:
            mapping[4] = record
        elif len(record) == 3:
            mapping[7] = record
        elif len(record) == 7:
            mapping[8] = record

    top = [s[-1] for s in difflib.ndiff(mapping[1], mapping[7]) if s.startswith('+')][0]
    middle_top_left = [s[-1] for s in difflib.ndiff(mapping[1], mapping[4]) if s.startswith('+')]
    bottom_bottom_left = [s[-1] for s in difflib.ndiff(mapping[4], mapping[8]) if s.startswith('+') and s[-1] != top]

    for record in records:
        if len(record) == 6 and all(x in record for x in middle_top_left) and all(x in record for x in bottom_bottom_left):
            mapping[6] = record

    for record in records:
        if len(record) == 6 and not all(x in record for x in middle_top_left):
            mapping[0] = record
        elif len(record) == 6 and all(x in record for x in middle_top_left) and not all(x in record for x in bottom_bottom_left):
            mapping[9] = record
        elif len(record) == 5 and all(x in record for x in middle_top_left):
            mapping[5] = record
        elif len(record) == 5 and all(x in record for x in bottom_bottom_left):
            mapping[2] = record

    for record in records:
        if record not in list(mapping.values()):
            mapping[3] = record

    return mapping

def apply_mapping_dict_to_digits(mapping_dict, digits):
    digits = [''.join(sorted(x)) for x in digits]
    inv_map = {v: k for k, v in mapping_dict.items()}
    mapped_list = [inv_map[k] for k in digits]
    return int(''.join([str(x) for x in mapped_list]))


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_08.txt') as f:
        file_data = f.read()

    inputs = [x.split(' | ')[-1] for x in file_data.split('\n')]
    inputs = [x.split(' ') for x in inputs]
    digit_dict = {1: 2, 4: 4, 7: 3, 8: 7}
    counter = 0
    for input in inputs:
        counter += len([x for x in input if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7])
    print(f"Answer to part 1: {counter}")

    rows = [x for x in file_data.split('\n')]
    sum = 0
    for row in rows:
        records = [x for x in row.split(' | ')][0].split(' ')
        digits = [x for x in row.split(' | ')][-1].split(' ')
        mapping_dict = get_mapping_dict(records)
        sum += apply_mapping_dict_to_digits(mapping_dict, digits)
    print(f"Answer to part 2: {sum}")
