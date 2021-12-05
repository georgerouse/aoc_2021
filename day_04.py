def print_card(card):
    for row in card:
        for number_dict in row:
            if number_dict["drawn"]:
                print(f"\033[1m{number_dict['number'].rjust(2)}\033[0m", end = ' ')
            else:
                print(f"{number_dict['number'].rjust(2)}", end = ' ')
        print("")
    print("\n")

def check_off_number(card, drawn_number):
    for row in card:
        for number_dict in row:
            if number_dict["number"] == drawn_number:
                number_dict["drawn"] = True
                continue

def get_sum_unmarked(card):
    unmarked_sum = 0
    for row in card:
        for number_dict in row:
            if not number_dict["drawn"]:
                unmarked_sum += int(number_dict["number"])
    return unmarked_sum


def bingo(card):
    for row in card:
        if all([x["drawn"] for x in row]):
            return True, row
    for i in range(0, len(card)):
        if all([row[i]["drawn"] for row in card]):
            return True, [row[i]["number"] for row in card]

    return False, []

if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_04.txt') as f:
        file_data = f.read()

    # Build up cards
    drawn_numbers = [x for x in file_data.split('\n')][0].split(",")
    raw_grids = [x for x in file_data.split('\n')][2:]
    list_of_cards = []
    card = []
    for raw_grid in raw_grids:
        if raw_grid  != "" :
            card.append([{"number": x, "drawn": False} for x in raw_grid.split(" ") if x != ""])
        if len(card) == 5:
            list_of_cards.append(card)
            card = []
    winner = False
    for drawn_number in drawn_numbers:
        for i, card in enumerate(list_of_cards):
            check_off_number(card, drawn_number)
            #print_card(card)
            is_bingo, winning_row = bingo(card)
            if is_bingo:
                #print(f"Winning card: {i}")
                #print_card(card)
                #print(winning_row)
                winner = True
                break
        if winner:
            break

    sum_unmarked = get_sum_unmarked(card)
    drawn_number = int(drawn_number)
    print(f"Answer to part 1: {sum_unmarked * drawn_number}")

    # Build up cards
    drawn_numbers = [x for x in file_data.split('\n')][0].split(",")
    raw_grids = [x for x in file_data.split('\n')][2:]
    list_of_cards = []
    card = []
    for raw_grid in raw_grids:
        if raw_grid  != "" :
            card.append([{"number": x, "drawn": False} for x in raw_grid.split(" ") if x != ""])
        if len(card) == 5:
            list_of_cards.append(card)
            card = []

    for drawn_number in drawn_numbers:
        list_of_cards_copy = list_of_cards.copy()
        bingo_list = []
        for i, card in enumerate(list_of_cards_copy):
            check_off_number(card, drawn_number)
            # print_card(card)
            is_bingo, winning_row = bingo(card)
            if is_bingo:
                bingo_list.append(i)
                last_drawn = drawn_number
        for i in sorted(bingo_list, reverse=True):
            last_card = list_of_cards.pop(i)

    sum_unmarked = get_sum_unmarked(last_card)
    last_drawn = int(last_drawn)
    print(f"Answer to part 2: {sum_unmarked * last_drawn}")
