running_total = 0
with open("puzzledata.txt") as file:
    for line in file.readlines():
        # find how many winning numbers there are by putting both my numbers and winning
        # numbers in set and getting the length of the intersection of the sets
        my_numbers = set(line.split(":")[1].split("|")[0].split())
        winning_numbers = set(line.split(":")[1].split("|")[1].split())
        interstection_count = len(my_numbers.intersection(winning_numbers))

        # calculate the points and add to the running total (the power of 2 
        # calculation doesnt work for 0, so only do this if not 0)
        if interstection_count: running_total += pow(2, interstection_count - 1)

print(running_total)
