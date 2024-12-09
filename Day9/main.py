from argparse import ArgumentParser

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 9")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    orig_filesystem = list(map(int, open(args.input_file).read()))
    filesystem = orig_filesystem.copy()
    
    #Part 1
    print("\n====== Part 1 ======")
    front_id = 0
    back_id = len(filesystem) // 2

    curr_file_idx = 0

    front_idx = 0
    back_idx = len(filesystem) - 1

    checksum = 0
    while front_idx < back_idx:
        checksum += front_id * filesystem[front_idx] * (2 * curr_file_idx + filesystem[front_idx] - 1) // 2
        curr_file_idx += filesystem[front_idx]
        front_id += 1
        free_space_num = filesystem[front_idx + 1]
        front_idx += 2
        while free_space_num > 0:
            items_to_move = min(free_space_num, filesystem[back_idx])
            free_space_num -= items_to_move
            filesystem[back_idx] -= items_to_move
            checksum += back_id * items_to_move * (2 * curr_file_idx + items_to_move - 1) // 2
            curr_file_idx += items_to_move
            if filesystem[back_idx] == 0:
                back_idx -= 2
                back_id -= 1
    checksum += back_id * filesystem[back_idx] * (2 * curr_file_idx + filesystem[back_idx] - 1) // 2
    print(f"   Solution: {checksum}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    idx_start = 0
    space = list()
    filesystem = orig_filesystem.copy()
    for i, item in enumerate(filesystem):
        if i % 2 == 0:
            space.append([idx_start, item])
        else:
            space.append([idx_start, item])
        idx_start  += item


    for idx in reversed(range(0, len(filesystem), 2)):
        free_idx = 1
        while space[free_idx][0] < space[idx][0] and space[free_idx][1] < space[idx][1]:
            free_idx += 2
        if space[free_idx][0] < space[idx][0]:
            space[idx][0] = space[free_idx][0]
            space[free_idx][0] += space[idx][1]
            space[free_idx][1] -= space[idx][1]

    checksum = sum(block_id * block[1] * (2 * block[0] + block[1] - 1) // 2 for block_id, block in enumerate(space[::2]))
    print(f"   Solution: {checksum}")
