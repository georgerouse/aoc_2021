def calc_moves(anchor_pos, a_list):
    total = 0
    for item in a_list:
        diff = abs(item-anchor_pos)
        total += sum([i for i in range(1, diff+1)])
    return total

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_07.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(",")]

    min_element = min(input_list)
    max_element = max(input_list)

    permutations = {}

    for anchor_pos in range(min_element, max_element+1):
        a_list = input_list.copy()
        moves = sum([abs(x-anchor_pos) for x in a_list])
        permutations[anchor_pos] = moves

    min_moves = {k: v for k, v in permutations.items() if v == min(permutations.values())}

    if len(min_moves) == 1:
        print(f"Answer to part 1: {list(min_moves.values())[0]}")

    for anchor_pos in range(min_element, max_element+1):
        a_list = input_list.copy()
        moves = calc_moves(anchor_pos, a_list)
        permutations[anchor_pos] = moves

    min_moves = {k: v for k, v in permutations.items() if v == min(permutations.values())}

    if len(min_moves) == 1:
        print(f"Answer to part 2: {list(min_moves.values())[0]}")
