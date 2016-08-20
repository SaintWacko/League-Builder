import csv

sharks = []
dragons = []
raptors = []

with open('soccer_players.csv', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    rows = list(reader)
    for row in rows:
        print(row)

