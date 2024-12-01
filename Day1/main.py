if __name__ == "__main__":

    # Reading the input file
    data = list(map(lambda s: s.split('   '), open('input.txt').read().splitlines()))
    
    #Creating the 2 lists
    list_1 = [int(d[0]) for d in data]
    list_2 = [int(d[-1]) for d in data]
    

    #Part 1
    print("====== Part 1 ======")
    solution_1 = sum(abs(num_1 - num_2) for num_1, num_2 in zip(sorted(list_1), sorted(list_2)))
    print(f"   Solution: {solution_1}")


    print("\n")

    #Part 2
    print("====== Part 2 ======")
    solution_2 = sum(num * list_2.count(num) for num in list_1)
    print(f"   Solution: {solution_2}")
