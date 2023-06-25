# Written by: Hu Bowen (S10255800)
# Date: 25 June 2023
# Class: CSF02

# Program to calculate total games, wins and scores based
# on a input list of names & corresponding scores

# Variables
player = [
    'Hafu', 'Toast', 'Pokimane',
    'Pewdiepie', 'Ninja', 'Markiplier'
]

results = [
    [98, 107, 87, 121],
    [88, 111],
    [79, 130, 99],
    [86, 100, 121, 66, 98],
    [108, 79, 92],
    [77, 126, 93, 100, 73, 89],
]

# Print headers
print("{:12} {:5} {:4} {:5}".format("Player", "Games", "Wins", "Total"))

# Loop through players and calculate their respective data
# And display it
for i in range(len(player)):
    player_name = player[i]
    games = len(results[i])
    wins = sum([1 if score >= 100 else 0 for score in results[i]])
    total = sum(results[i])

    print("{:12} {:^5} {:^4} {:^5}".format(player_name, games, wins, total))
