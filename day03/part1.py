schematic = [""]

# searches around a given start and end position and returns True 
# if if finds a charachter that isn't a digit or a fullstop.
def search_surrounding(passed_y, x_start, x_end):
    for y in range(passed_y -1, passed_y + 2):
        for x in range(x_start - 1, x_end + 2):
            if not (schematic[y][x].isdigit() or schematic[y][x] == "."): return True
    return False


### ENTRY POINT ###
if __name__ == "__main__":
    running_total = 0

    # read the file into the schematic list, add extra fullstop at start and end
    with open("puzzledata.txt") as file:
        for line in file.readlines():
            schematic.append("." + line[:-1] + ".")

    # add full row of fullstops at start and end
    blank_row = ""
    for i in range(len(schematic[1])): blank_row += "."
    schematic[0] = blank_row
    schematic.append(blank_row)

    # loop through the schematic looking for digits. When it comes to the end of a
    # set of digits, calls to function to check for surrounding symbols and if it 
    # finds any adds that number to the running total.
    for y in range(len(schematic)):
        number_string = ""
        start_pos = -1
        for x in range(len(schematic[y])):
            if schematic[y][x].isdigit():
                number_string += schematic[y][x]
                if start_pos == -1: start_pos = x
            else:
                if start_pos != -1:
                    if search_surrounding(y, start_pos, x-1):
                        running_total += int(schematic[y][start_pos:x])
                    start_pos = -1

    print(running_total)
