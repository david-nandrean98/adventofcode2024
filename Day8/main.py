from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 8")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    city = [list(line) for line in open(args.input_file).read().splitlines()]
    rows = len(city)
    cols = len(city[0])

    antena_dict = dict()
    for i, line in enumerate(city):
        for j, c in enumerate(line):
            if c == '.':
                continue
            if c in antena_dict.keys():
                antena_dict[c].append((i, j))
            else:
                antena_dict[c] = [(i, j)]

    # Part 1
    print("====== Part 1 ======")
    antinode_set = set()
    for antenas in antena_dict.values():
        for i, (x1, y1) in enumerate(antenas):
            for x2, y2 in antenas[i + 1:]:
                antinode_1 = (2 * x2 - x1, 2 * y2 - y1)
                if  0 <= antinode_1[0] < rows and 0 <= antinode_1[1] < cols:
                    antinode_set.add(antinode_1)
                
                antinode_2 = (2 * x1 - x2, 2 * y1 - y2)
                if  0 <= antinode_2[0] < rows and 0 <= antinode_2[1] < cols:
                    antinode_set.add(antinode_2)
    
    solution_1 = len(antinode_set)
    print(f"   Solution: {solution_1}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")

    node_set = set()
    for antenas in antena_dict.values():
        for i, (x1, y1) in enumerate(antenas):
            for x2, y2 in antenas[i + 1:]:
                diff_x, diff_y = x1 - x2, y1 - y2
                antinode = (x1, y1)
                while 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                    antinode_set.add(antinode)
                    antinode = (antinode[0] + diff_x, antinode[1] + diff_y)

                antinode = (x1 - diff_x, y1 - diff_y)
                while 0 <= antinode[0] < rows and 0 <= antinode[1] < cols:
                    antinode_set.add(antinode)
                    antinode = (antinode[0] - diff_x, antinode[1] - diff_y)

    solution_2 = len(antinode_set)
    print(f"   Solution: {solution_2}")
