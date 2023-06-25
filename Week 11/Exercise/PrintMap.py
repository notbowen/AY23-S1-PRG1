# Written by: Hu Bowen (S10255800)
# Date: 25 June 2023
# Class: CSF02

# Program to render a map based on a variable

# Function to return raw index on rendered map based on list index
def get_raw_index(x, y):
    raw_x = 4 * x + 2
    raw_y = 2 * y + 1

    return (raw_x, raw_y)


# Initialise map
map = [
    ['T', ' ', ' ', ' ', 'T'],
    [' ', 'P', ' ', ' ', ' '],
    [' ', ' ', ' ', 'T', ' '],
    [' ', 'T', ' ', ' ', ' ']
]

# Initialise blank rendered map
# Even rows should follow +---+---+
# Odd rows should follow  |   |   |
total_rows = len(map) * 2 + 1
total_columns = len(map[0])

rendered_map = ""  # Variable to store the map in

# Loop through the rows and init blank map
for i in range(total_rows):
    if i % 2 == 0:
        rendered_map += "+"
        for col in range(total_columns):
            rendered_map += "---+"
        rendered_map += '\n'

    else:
        rendered_map += '|'
        for col in range(total_columns):
            rendered_map += "   |"
        rendered_map += '\n'

# Right now the map should look similar to:
# +---+---+---+
# |   |   |   |
# +---+---+---+
# |   |   |   |
# +---+---+---+
#
# It should not contain any values

# Split rendered map into a 2D list (so that it can be modified via list[x][y])
rendered_map = rendered_map.splitlines()
rendered_map = [list(row) for row in rendered_map]

# Now we fill up the map with the values in the `map` variable
for y in range(len(map)):
    for x in range(len(map[y])):
        raw_x, raw_y = get_raw_index(x, y)
        rendered_map[raw_y][raw_x] = map[y][x]

# Join rendered map back into a string and display
rendered_map = ["".join(row) for row in rendered_map]
rendered_map = "\n".join(rendered_map)

print(rendered_map)
