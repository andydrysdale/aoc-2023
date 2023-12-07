winning_info = {}
count = 0
line_count = 0

# function is run recursively to check cards
def check(card_no):
    global count
    count += 1
    for i in range(winning_info[card_no]):
        check(card_no + 1 + i)

# read the file and build a dictionary with card number 
# as the key and number of wins as the value
with open("puzzledata.txt") as file:
    for line in file.readlines():
        line_count += 1
        # find how many winning numbers there are by putting both my numbers and winning
        # numbers in set and getting the length of the intersection of the sets
        my_numbers = set(line.split(":")[1].split("|")[0].split())
        winning_numbers = set(line.split(":")[1].split("|")[1].split())
        winning_info[line_count] = len(my_numbers.intersection(winning_numbers))

# run the recursive function to check each initial card
for i in range(line_count): check(i + 1)

print(count)
