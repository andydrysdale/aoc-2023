with open("puzzledata.txt") as file:
    time = int("".join(file.readline().split(":")[1].split()))
    record = int("".join(file.readline().split(":")[1].split()))

    # loop through every possibility and total up the ways of beating the record
    winning_count = 0
    for hold_time in range(time + 1):
        distance = hold_time * (time - hold_time)
        if distance > record: winning_count += 1

    print(winning_count)