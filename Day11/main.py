from argparse import ArgumentParser

def calculate_number_of_stones_after_blinks(orig_stones, blink_number):
    stones = orig_stones.copy()
    num_stones = 0
    while len(stones) > 0:
        blink_num, value = stones.pop()
        if blink_num == blink_number:
            num_stones += 1
        elif value == 0:
            stones.append((blink_num + 1, 1))
        elif len(str(value)) % 2 == 0:
            value_str = str(value)
            len_value_str = len(value_str)
            stones.append((blink_num + 1, int(value_str[:len_value_str // 2])))
            stones.append((blink_num + 1, int(value_str[len_value_str // 2:])))
        else:
            stones.append((blink_num + 1, 2024 * value))
    return num_stones


def calculate_number_of_stones_after_blinks_part2(stone, blink, target_blink, stone_blink_dict):
    remaining_blinks = target_blink - blink
    if stone in stone_blink_dict.keys() and remaining_blinks in stone_blink_dict[stone].keys():
        return stone_blink_dict[stone][remaining_blinks]

    result = 0
    if blink == target_blink:
        return 1
    elif stone == 0:
        result += calculate_number_of_stones_after_blinks_part2(1, blink + 1, target_blink, stone_blink_dict)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        len_stone_str = len(stone_str)
        start_idx = len_stone_str // 2
        result += calculate_number_of_stones_after_blinks_part2(int(stone_str[len_stone_str // 2:]), blink + 1, target_blink, stone_blink_dict)
        result += calculate_number_of_stones_after_blinks_part2(int(stone_str[:len_stone_str // 2]), blink + 1, target_blink, stone_blink_dict)
    else:
        result += calculate_number_of_stones_after_blinks_part2(2024 * stone, blink + 1, target_blink, stone_blink_dict)

    if stone in stone_blink_dict.keys():
        stone_blink_dict[stone][remaining_blinks] = result
    else:
        stone_blink_dict[stone] = dict()
        stone_blink_dict[stone][remaining_blinks] = result

    return result    


if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 11")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    orig_stones = [(0, int(stone)) for stone in open(args.input_file).read().split(' ')]
    
    #Part 1
    print("\n====== Part 1 ======")
    print(f"   Solution: {calculate_number_of_stones_after_blinks(orig_stones, 25)}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    stone_blink_dict = dict()
    stone_num = sum(calculate_number_of_stones_after_blinks_part2(stone, 0, 75, stone_blink_dict) for _, stone in orig_stones)
    print(f"   Solution: {stone_num}")
