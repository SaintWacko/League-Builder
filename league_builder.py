import csv

sharks = []
dragons = []
raptors = []
experienced = []

with open('soccer_players.csv', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    players = list(reader)
    for player in players:
        print(player)
print("\n\n")

for player in players:
    if player['Soccer Experience'] == 'YES':
        experienced.append(players.pop(players.index(player)))

for player in experienced:
    print(player)
print("\n\n")

try:
    while True:
        sharks.append(experienced.pop())
        raptors.append(experienced.pop())
        dragons.append(experienced.pop())
except(IndexError):
    pass

try:
    while True:
        sharks.append(players.pop())
        raptors.append(players.pop())
        dragons.append(players.pop())
except(IndexError):
    pass

with open('template', 'r') as file:
    letter = file.read()

for player in sharks:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Sharks", date="March 17 at 3PM"))

for player in dragons:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Dragons", date="March 17 at 1PM"))

for player in raptors:
    with open(player['Name'].lower().replace(" ", "_") + ".txt", 'w') as file:
        file.write(letter.format(**player, league="Raptors", date="March 18 at 1PM"))
