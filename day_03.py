from collections import Counter

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_03.txt') as f:
        file_data = f.read()
    input_list = [x for x in file_data.split('\n')]

    num_bits = len(input_list[0])
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(0, num_bits):
        bit_list = [x[i] for x in input_list]
        counter = Counter(bit_list)
        gamma_rate += counter.most_common()[0][0]
        epsilon_rate += counter.most_common()[-1][0]

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print(f"Answer to part 1: {gamma_rate * epsilon_rate}")

    ogr_input_list = input_list.copy()

    while len(ogr_input_list) > 1:
        for i in range(0, num_bits):
            bit_list = [x[i] for x in ogr_input_list]
            counter = Counter(bit_list)
            most_common = counter.most_common()[0][0]
            most_common_count = counter.most_common()[0][1]
            least_common_count = counter.most_common()[-1][1]
            if most_common_count == least_common_count:
                most_common = "1"
            ogr_input_list = [x for x in ogr_input_list if x[i] == most_common]
            if len(ogr_input_list) == 1:
                break

    oxygen_generator_rating = int(ogr_input_list[0], 2)

    CO2sr_input_list = input_list.copy()

    while len(CO2sr_input_list) > 1:
        for i in range(0, num_bits):
            bit_list = [x[i] for x in CO2sr_input_list]
            counter = Counter(bit_list)
            least_common = counter.most_common()[-1][0]
            most_common_count = counter.most_common()[0][1]
            least_common_count = counter.most_common()[-1][1]
            if most_common_count == least_common_count:
                least_common = "0"
            CO2sr_input_list = [x for x in CO2sr_input_list if x[i] == least_common]
            if len(CO2sr_input_list) == 1:
                break

    c02_rating = int(CO2sr_input_list[0], 2)

    print(f"Answer to part 1: {oxygen_generator_rating * c02_rating}")
