from argparse import ArgumentParser

def trailhead_finder(topographic_map, position, hiking_trail_set):
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    x, y = position
    if topographic_map[x][y] == 9:
        hiking_trail_set.add((x, y))
    else:
        if x + 1 < rows and topographic_map[x + 1][y] - topographic_map[x][y] == 1:
            trailhead_finder(topographic_map, (x + 1, y), hiking_trail_set)

        if x - 1 >= 0 and topographic_map[x - 1][y] - topographic_map[x][y] == 1:
            trailhead_finder(topographic_map, (x - 1, y), hiking_trail_set)

        if y + 1 < cols and topographic_map[x][y + 1] - topographic_map[x][y] == 1:
            trailhead_finder(topographic_map, (x, y + 1), hiking_trail_set)

        if y - 1 >= 0 and topographic_map[x][y - 1] - topographic_map[x][y] == 1:
            trailhead_finder(topographic_map, (x, y - 1), hiking_trail_set)

def trailhead_rating(topographic_map, position):
    rows = len(topographic_map)
    cols = len(topographic_map[0])
    x, y = position
    if topographic_map[x][y] == 9:
        return 1
    rating = 0
    if x + 1 < rows and topographic_map[x + 1][y] - topographic_map[x][y] == 1:
        rating += trailhead_rating(topographic_map, (x + 1, y))

    if x - 1 >= 0 and topographic_map[x - 1][y] - topographic_map[x][y] == 1:
        rating += trailhead_rating(topographic_map, (x - 1, y))

    if y + 1 < cols and topographic_map[x][y + 1] - topographic_map[x][y] == 1:
        rating += trailhead_rating(topographic_map, (x, y + 1))

    if y - 1 >= 0 and topographic_map[x][y - 1] - topographic_map[x][y] == 1:
        rating += trailhead_rating(topographic_map, (x, y - 1))
        
    return rating


if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 10")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    topographic_map = [list(map(int, line)) for line in open(args.input_file).read().splitlines()]
    
    #Part 1
    print("\n====== Part 1 ======")
    score  = 0
    for x, line in enumerate(topographic_map):
        for y, p in enumerate(line):
            if p == 0:
                hiking_trail_set = set()
                trailhead_finder(topographic_map, (x, y), hiking_trail_set)
                score += len(hiking_trail_set)
    print(f"   Solution: {score}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    rating_sum  = 0
    for x, line in enumerate(topographic_map):
        for y, p in enumerate(line):
            if p == 0:
                rating_sum += trailhead_rating(topographic_map, (x, y))
    print(f"   Solution: {rating_sum}")
