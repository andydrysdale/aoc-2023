seeds = []
maps = []

# takes a value and a 'map' of transformations and returns the new value
def process_value(value, map):
    for line in map:
        destination_range_start = line[0]
        source_range_start = line[1]
        range_length = line[2]
        if value >= source_range_start and value <= (source_range_start + range_length - 1):
            return destination_range_start + (value - source_range_start)
    return value

### ENTRY POINT ###
if __name__ == "__main__":
    with open("puzzledata.txt") as file:
        # read in the seed values, then skip the next empty line
        seed_strings = file.readline()[:-1].split(" ")
        for s in range(1, len(seed_strings)): seeds.append(int(seed_strings[s]))
        file.readline()
        
        # read the rest of the file
        temp_map = []
        for line in file.readlines(): 
            if line.endswith(":\n"):  # skip map headings
                pass
            elif line == "\n":        # process the map block at when the end is reached
                maps.append(list(temp_map))
                temp_map.clear()
            else:                     # split the line up and add it to the current map
                temp_map.append([int(x) for x in line[:-1].split(" ")])

    # run every seed
    location = []
    for seed in seeds:
        for m in range(len(maps)):
            seed = process_value(seed, maps[m])
        location.append(seed)

    location.sort()
    print(location[0])
