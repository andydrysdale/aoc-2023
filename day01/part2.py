def find_first_digit(search_string):
    for x in range(len(search_string)):   
        if search_string[x].isdigit(): 
            return search_string[x]    
        else:
            if search_string[x:x+3] == "one": return "1"
            if search_string[x:x+3] == "two": return "2"
            if search_string[x:x+3] == "six": return "6"
            if search_string[x:x+4] == "four": return "4"
            if search_string[x:x+4] == "five": return "5"
            if search_string[x:x+4] == "nine": return "9"
            if search_string[x:x+5] == "three": return "3"
            if search_string[x:x+5] == "seven": return "7"
            if search_string[x:x+5] == "eight": return "8"

def find_last_digit(search_string):
    for x in reversed(range(len(search_string))):
        if search_string[x].isdigit(): 
            return search_string[x]    
        else:
            if search_string[x-2:x+1] == "one": return "1"
            if search_string[x-2:x+1] == "two": return "2"
            if search_string[x-2:x+1] == "six": return "6"
            if search_string[x-3:x+1] == "four": return "4"
            if search_string[x-3:x+1] == "five": return "5"
            if search_string[x-3:x+1] == "nine": return "9"
            if search_string[x-4:x+1] == "three": return "3"
            if search_string[x-4:x+1] == "seven": return "7"
            if search_string[x-4:x+1] == "eight": return "8"


with open("puzzledata.txt") as file:
    running_total = 0

    for line in file.readlines():
        first_digit = find_first_digit(line[:-1])
        last_digit = find_last_digit(line[:-1])

        running_total += int(first_digit + last_digit)

    print(running_total)

