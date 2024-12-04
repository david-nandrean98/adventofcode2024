from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 4")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    data = open(args.input_file).read().splitlines()
    rows = len(data)
    cols = len(data[0])
    # Part 1
    print("====== Part 1 ======")
    words = {"XMAS", "SAMX"}
    solution_1 = 0
    for i in range(rows):
        for j in range(cols):
            if j + 3 < cols and data[i][j: j + 4] in words:
                solution_1 += 1
            if i + 3 < rows and "".join(data[i + k][j] for k in range(4)) in words:
                solution_1 += 1
            if i + 3 < rows and j + 3 < cols and "".join(data[i + k][j + k] for k in range(4)) in words:
                solution_1 += 1
            if i + 3 < rows and j - 3 >= 0 and "".join(data[i + k][j - k] for k in range(4)) in words:
                solution_1 += 1
    print(f"   Solution: {solution_1}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    words = {"MAS", "SAM"}
    solution_2 = 0
    for i in range(rows):
        for j in range(cols):
            if i - 1 >= 0 and i + 1 < rows and j - 1 >= 0 and j + 1 < cols and "".join(data[i - 1 + k][j - 1 + k] for k in range(3)) in words and "".join(data[i - 1 + k][j + 1 - k] for k in range(3)) in words:
                solution_2 += 1
    print(f"   Solution: {solution_2}")
