def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end="")
        print("")
    print("")


def update_grid(grid, x, y):
    value = grid[y][x]
    if value == ".":
        grid[y][x] = 1
    else:
        grid[y][x] = value + 1

def determine_2_counts(grid):
    two_count = 0
    for row in grid:
        for value in row:
            if type(value) != str and value >= 2:
                two_count += 1
    return two_count


def update_line_h_v(grid, coord):
    start_x = coord["start_x"]
    start_y = coord["start_y"]
    finish_x = coord["finish_x"]
    finish_y = coord["finish_y"]
    if start_y == finish_y:
        # Horizontal Line
        if start_x < finish_x:
            for i in range(start_x, finish_x+1):
                update_grid(grid, i, start_y)
        else:
            for i in range(finish_x, start_x+1):
                update_grid(grid, i, start_y)
    if start_x == finish_x:
        # Vertical Line
        if start_y < finish_y:
            for i in range(start_y, finish_y+1):
                update_grid(grid, start_x, i)
        else:
            for i in range(finish_y, start_y+1):
                update_grid(grid, start_x, i)

def extrapolate_points(start_x, finish_x, start_y, finish_y):
    points = [(start_x, start_y)]
    if start_x > finish_x:
        diff = start_x - finish_x
        x_op = "-"
    else:
        diff = finish_x - start_x
        x_op = "+"
    if start_y > finish_y:
        y_op = "-"
    else:
        y_op = "+"

    x = start_x
    y = start_y
    for i in range(0, diff):
        x = eval("x "+x_op+' 1')
        y = eval("y "+y_op+' 1')
        points.append((x, y))
    return points


def update_line(grid, coord):
    start_x = coord["start_x"]
    start_y = coord["start_y"]
    finish_x = coord["finish_x"]
    finish_y = coord["finish_y"]
    if start_y == finish_y:
        # Horizontal Line
        if start_x < finish_x:
            for i in range(start_x, finish_x+1):
                update_grid(grid, i, start_y)
        else:
            for i in range(finish_x, start_x+1):
                update_grid(grid, i, start_y)
    elif start_x == finish_x:
        # Vertical Line
        if start_y < finish_y:
            for i in range(start_y, finish_y+1):
                update_grid(grid, start_x, i)
        else:
            for i in range(finish_y, start_y+1):
                update_grid(grid, start_x, i)
    else:
        full_points = extrapolate_points(start_x, finish_x, start_y, finish_y)
        for x, y in full_points:
            update_grid(grid, x, y)


if __name__ == '__main__':
    # Get the input data
    with open('inputs/day_05.txt') as f:
        file_data = f.read()
    input_list = [x for x in file_data.split("\n")]
    input_list = [x.split(" -> ") for x in input_list]

    max_x, max_y = 0, 0
    coord_list = []
    for start, finish in input_list:
        start_x, start_y = start.split(",")
        finish_x, finish_y = finish.split(",")
        start_x = int(start_x)
        start_y = int(start_y)
        finish_x = int(finish_x)
        finish_y = int(finish_y)

        if finish_x > max_x:
            max_x = finish_x
        if start_x > max_x:
            max_x = start_x
        if finish_y > max_y:
            max_y = finish_y
        if start_y > max_y:
            max_y = start_y

        coord_list.append({"start_x": start_x, "start_y": start_y,
            "finish_x": finish_x, "finish_y": finish_y})
    coord_list_2 = coord_list.copy()

    # build the grid
    width = max_x + 1
    grid = [["."] * width for i in range(0, max_y+1)]
    for coord in coord_list:
        if coord["start_x"] == coord["finish_x"] or coord["start_y"] == coord["finish_y"]:
            update_line_h_v(grid, coord)
    # print_grid(grid)
    print(f"Answer to part 1: {determine_2_counts(grid)}")

    grid = [["."] * width for i in range(0, max_y+1)]
    for coord in coord_list_2:
        update_line(grid, coord)
    # print_grid(grid)
    print(f"Answer to part 2: {determine_2_counts(grid)}")
