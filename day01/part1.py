with open("puzzledata.txt") as file:
    running_total = 0

    for line in file.readlines():
        digit_string = ""
        for chr in line:
            if chr.isdigit(): 
                digit_string += chr

        running_total += int(digit_string[:1] + digit_string[-1:])

    print(running_total)

