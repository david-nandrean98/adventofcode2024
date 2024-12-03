from argparse import ArgumentParser

def check_if_remove_any(d):
    for i in range(len(d)):
        new_d = d[:i] + d[i + 1:]
        if all(d1 != d2 and (d2 - d1) // abs(d2 - d1) == (new_d[1] - new_d[0]) // abs(new_d[1] - new_d[0]) and 1 <= abs(d2 - d1) <= 3 for d1, d2 in zip(new_d, new_d[1:])):
            return True

    return False

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 2")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    data = [list(map(int, line.split(' '))) for line in open(args.input_file).read().splitlines()]

    #Part 1
    print("====== Part 1 ======")
    solution_1 = sum(1 for d in data if all(d1 != d2 and (d2 - d1) // abs(d2 - d1) == (d[1] - d[0]) // abs(d[1] - d[0]) and 1 <= abs(d2 - d1) <= 3 for d1, d2 in zip(d, d[1:])))
    print(f"   Solution: {solution_1}")

    print('\n')

    #Part 2
    print("====== Part 2 ======")
    solution_2 = sum(1 for d in data if all(d1 != d2 and (d2 - d1) // abs(d2 - d1) == (d[1] - d[0]) // abs(d[1] - d[0]) and 1 <= abs(d2 - d1) <= 3 for d1, d2 in zip(d, d[1:])) or check_if_remove_any(d))
    print(f"   Solution: {solution_2}")
    

