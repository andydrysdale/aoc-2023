# processes a list of strings representing 'grabs' and returns the 
# 'power' which is the product of red, green and blue max counts
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

    return (red_max * green_max * blue_max)


if __name__ == "__main__":
    running_total = 0

    with open("puzzledata.txt") as file:
        for line in file.readlines():

            # parse the line to pick out the game number and list of 'grabs'
            game_number = int(line.split(":")[0][5:])
            list_of_grabs = line[:-1].split(":")[1].split(";")

            # get the 'power' for this game and add it to the running total 
            running_total +=  process_grabs(list_of_grabs)
   
    print(running_total)
                    