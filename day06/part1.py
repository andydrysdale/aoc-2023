times = []
records = []

# read the file into the lists
with open("puzzledata.txt") as file:
    for time_string in file.readline().split(":")[1].split():
        times.append(int(time_string))
    for record_string in file.readline().split(":")[1].split():
        records.append(int(record_string))

running_product = 1

# loop through each record and multiply the number of winning options to the running product
for race in range(len(times)):
    winning_count = 0

    # loop through every possibility and total up the ways of beating the record
    for hold_time in range(times[race] + 1):
        distance = hold_time * (times[race] - hold_time)
        if distance > records[race]: winning_count += 1
    
    running_product *= winning_count

print(running_product)