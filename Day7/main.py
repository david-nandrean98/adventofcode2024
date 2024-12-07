from argparse import ArgumentParser


def equation_can_be_true(result, numbers, operator_idx, curr_result):
    if curr_result > result:
        return False

    if operator_idx == len(numbers) - 2:
        return result in [curr_result + numbers[operator_idx + 1], curr_result * numbers[operator_idx + 1]]

    return equation_can_be_true(result, numbers, operator_idx + 1, curr_result + numbers[operator_idx + 1]) or equation_can_be_true(result, numbers, operator_idx + 1, curr_result * numbers[operator_idx + 1])


def equation_can_be_true_part2(result, numbers, operator_idx, curr_result):
    if curr_result > result:
        return False

    if operator_idx == len(numbers) - 2:
        return result in [curr_result + numbers[operator_idx + 1], curr_result * numbers[operator_idx + 1], int(f"{curr_result}{numbers[operator_idx + 1]}")]

    return equation_can_be_true_part2(result, numbers, operator_idx + 1, curr_result + numbers[operator_idx + 1]) or equation_can_be_true_part2(result, numbers, operator_idx + 1, curr_result * numbers[operator_idx + 1]) or equation_can_be_true_part2(result, numbers, operator_idx + 1, int(f"{curr_result}{numbers[operator_idx + 1]}")) 


if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 7")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    calibrations = [line.split(': ') for line in open(args.input_file).read().splitlines()]
    calibrations = [(int(result), list(map(int, numbers.split(' ')))) for result, numbers in calibrations]

    # Part 1
    print("====== Part 1 ======")
    solution_1 = sum(result for result, numbers in calibrations if equation_can_be_true(result, numbers, 0, numbers[0]))
    print(f"   Solution: {solution_1}")

    print('\n')
    # Part 2
    print("====== Part 2 ======")
    solution_2 = sum(result for result, numbers in calibrations if equation_can_be_true_part2(result, numbers, 0, numbers[0]))
    print(f"   Solution: {solution_2}")
