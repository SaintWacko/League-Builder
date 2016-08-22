"""This program is designed to take a csv formated spreadsheet of soccer
players and distribute them evenly among three teams, ensuring that each
team has the same number of experienced players.  It then, based on a
template file, generates form letters to the parents/guardians of each
player, informing them of the team their child is on and the time of the
first practice.
"""


import csv

sharks = []
dragons = []
raptors = []
experienced = []

# Read in list of players
with open('soccer_players.csv', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    players = list(reader)

# Sort experienced players into separate list
for player in players[:]:
    if player['Soccer Experience'] == 'YES':
        experienced.append(players.pop(players.index(player)))

# spread experienced players evenly between teams
try:
    while True:
        sharks.append(experienced.pop())
        raptors.append(experienced.pop())
        dragons.append(experienced.pop())
except(IndexError):
    pass

# spread inexperienced players evenly between teams
try:
    while True:
        sharks.append(players.pop())
        raptors.append(players.pop())
        dragons.append(players.pop())
except(IndexError):
    pass

# Read in template from file
with open('template', 'r') as file:
    letter = file.read()

# Write Sharks letters to files
for player in sharks:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Sharks", date="March 17 at 3PM"))

# Write Dragons letters to files
for player in dragons:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Dragons", date="March 17 at 1PM"))

# Write Raptors letters to file
for player in raptors:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Raptors", date="March 18 at 1PM"))
