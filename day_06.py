if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_06.txt') as f:
        file_data = f.read()
    input_list = [int(x) for x in file_data.split(",")]
    input_list_2 = input_list.copy()

    for day in range(1, 80+1):
        # Decrement all by 1
        input_list = [x-1 for x in input_list]
        # If Zero values then make 6 and append 8
        zero_indexes = []
        for i, value in enumerate(input_list):
            if value == -1:
                zero_indexes.append(i)
        for index in zero_indexes:
            input_list[index] = 6
            input_list.append(8)

    print(f"Answer to part 1: {len(input_list)}")

    buckets = [input_list_2.count(i) for i in range(9)]
    for i in range(256):
        buckets[(i+7) % 9] += buckets[i % 9]

    print(f"Answer to part 2: {sum(buckets)}")
