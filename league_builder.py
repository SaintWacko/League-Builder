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
for player in players:
    print(player)
