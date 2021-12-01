def get_increasing_count(input_list):
    increase_count = 0
    for i, value in enumerate(input_list):
        if i == 0:
            continue
        else:
            if value > input_list[i-1]:
                increase_count += 1
    return increase_count


if __name__ == '__main__':
        # Get the input data
    with open('inputs/day_01.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split('\n')]
    print(f"Answer to part 1: {get_increasing_count(input_list)}")

    sum_list = [sum(input_list[i:i+3]) for i, value in enumerate(input_list) if i <= len(input_list)-3]
    print(f"Answer to part 2: {get_increasing_count(sum_list)}")
