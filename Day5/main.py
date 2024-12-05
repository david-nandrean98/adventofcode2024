from argparse import ArgumentParser

def sort_update(update, precedes_dict):
    update_set = set(update)
    precede_rules = {page: preceding_pages.intersection(update_set) for page, preceding_pages in precedes_dict.items() if page in update_set}
    index_dict = {page: -1 for page in update_set}
    idx = 0
    while len(update_set) > 0:
        no_precede_pages = [page for page, preceding_pages in precede_rules.items() if len(preceding_pages) == 0]
        for page in no_precede_pages:
            index_dict[page] = idx
            update_set.remove(page)
        precede_rules = {page: preceding_pages.intersection(update_set) for page, preceding_pages in precede_rules.items() if page in update_set}
        idx += 1
    update.sort(key=lambda page: index_dict[page])

if __name__ == "__main__":

    parser = ArgumentParser(prog="Advent of Code 2024 - Day 5")
    parser.add_argument("--input_file", required=True, type=str, help="The path to the input file")
    args = parser.parse_args()

    # Reading the input file
    ordering_rules, updates = open(args.input_file).read().split("\n\n")
    updates = [list(map(int, update.split(','))) for update in updates.splitlines()]

    precedes_dict = dict()

    for ordering_rule in ordering_rules.splitlines():
        fst, snd = tuple(map(int, ordering_rule.split('|')))
        if snd not in precedes_dict.keys():
            precedes_dict[snd] = {fst}
        else:
            precedes_dict[snd].add(fst)
        

    # Part 1
    print("====== Part 1 ======")
    solution_1 = 0
    for update in updates:
        valid = True
        cannot_follow_set = set()
        for page in update:
            if page in cannot_follow_set:
                valid = False
                break
            if page in precedes_dict.keys():
                cannot_follow_set.update(precedes_dict[page])
        if valid:
            solution_1 += update[len(update) // 2]

    print(f"   Solution: {solution_1}")

    print('\n')

    # Part 2
    print("====== Part 2 ======")
    solution_2 = 0
    for update in updates:
        valid = True
        cannot_follow_set = set()
        for idx, page in enumerate(update):
            if page in cannot_follow_set:
                valid = False
            if page in precedes_dict.keys():
                cannot_follow_set.update(precedes_dict[page])
        if not valid:
            sort_update(update, precedes_dict)
            solution_2 += update[len(update) // 2]
    print(f"   Solution: {solution_2}")
