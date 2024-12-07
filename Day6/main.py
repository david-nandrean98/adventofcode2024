from argparse import ArgumentParser


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def find_guard(mapped_area):
    for i, line in enumerate(mapped_area):
        for j, c in enumerate(line):
            if c not in ['.', '#']:
                return i, j
    return -1, -1


if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 6")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    mapped_area = [list(line) for line in open(args.input_file).read().splitlines()]
    rows = len(mapped_area)
    cols = len(mapped_area[0])

    start_x, start_y = find_guard(mapped_area)
    start_direction = mapped_area[start_x][start_y]
    mapped_area[start_x][start_y] = '.'

    rotation_dict = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    direction_dict = {'^': Vec2(-1, 0), '>': Vec2(0, 1), 'v': Vec2(1, 0), '<': Vec2(0, -1)}


    # Part 1
    print("====== Part 1 ======")

    direction = start_direction
    direction_vec = direction_dict[direction]
    position = Vec2(start_x, start_y)
    visited_set = set()
    while 0 <= position.x < rows and 0 <= position.y < cols:
        if mapped_area[position.x][position.y] == '.':
            visited_set.add((position.x, position.y))
        else:
            position -= direction_vec
            direction = rotation_dict[direction]
            direction_vec = direction_dict[direction]
        position += direction_vec
    solution_1 = len(visited_set)
    print(f"   Solution: {solution_1}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    solution_2 = 0
    for visited in visited_set:
        pos_x, pos_y = visited
        if Vec2(pos_x, pos_y) == Vec2(start_x, start_y):
            continue
        mapped_area[pos_x][pos_y] = '#'
        direction = start_direction
        direction_vec = direction_dict[direction]
        position = Vec2(start_x, start_y)
        visited_set_with_direction = set()
        while 0 <= position.x < rows and 0 <= position.y < cols and (position.x, position.y, direction) not in visited_set_with_direction:
            if mapped_area[position.x][position.y] == '.':
                visited_set_with_direction.add((position.x, position.y, direction))
            else:
                position -= direction_vec
                direction = rotation_dict[direction]
                direction_vec = direction_dict[direction]
            position += direction_vec
        mapped_area[pos_x][pos_y] = '.'
        if 0 <= position.x < rows and 0 <= position.y < cols:
            solution_2 += 1

    print(f"   Solution: {solution_2}")
