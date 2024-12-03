from argparse import ArgumentParser
import re

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 3")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    data = open(args.input_file).read()

    # Part 1
    print("====== Part 1 ======")
    instructions = re.findall("mul\([0-9]+,[0-9]+\)", data)
    solution_1 = 0
    for instruction in instructions:
        numbers = instruction[4:-1].split(',')
        solution_1 += int(numbers[0]) * int(numbers[1])
    print(f"   Solution: {solution_1}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    instructions = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data)
    solution_2 = 0
    enabled = True
    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            numbers = instruction[4:-1].split(',')
            solution_2 += int(numbers[0]) * int(numbers[1])
    print(f"   Solution: {solution_2}")
