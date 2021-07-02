with open('E:\code\AoC\day6\input.txt', 'r') as fd:
    groups = fd.read().split("\n\n")

    # Part 1
    counter = 0
    for group in groups:
        answers = group.replace("\n", "")
        counter += len(set(answers))
    print("Part 1: Number of different questions that got a 'yes'-answer: " + str(counter))