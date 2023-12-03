TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

# processes a list of strings representing 'grabs' and returns the 
# maximum occuring red, green and blue counts across all gralbs
def process_grabs(list_of_grabs):
    red_max = 0
    green_max = 0
    blue_max = 0
    for grab in list_of_grabs:
        for colour_group in grab.split(","):
            colour = colour_group.split(" ")[2]
            count = int(colour_group.split(" ")[1])
            if colour == "red" and count > red_max: red_max = count
            elif colour == "green" and count > green_max: green_max = count
            elif colour == "blue" and count > blue_max: blue_max = count

    return (red_max, green_max, blue_max)


if __name__ == "__main__":
    running_total = 0

    with open("puzzledata.txt") as file:
        for line in file.readlines():

            # parse the line to pick out the game number and list of 'grabs'
            game_number = int(line.split(":")[0][5:])
            list_of_grabs = line[:-1].split(":")[1].split(";")

            # get the maximum occuring counts in the list of grabs 
            max_colours_from_grabs = process_grabs(list_of_grabs)

            # if the counts are possible based on the specified number of total 
            # reds, greens and blues, add the game number to the running total
            if (max_colours_from_grabs[0] <= TOTAL_RED and 
                max_colours_from_grabs[1] <= TOTAL_GREEN and 
                max_colours_from_grabs[2] <= TOTAL_BLUE):
                running_total += game_number
    
    print(running_total)
                    
