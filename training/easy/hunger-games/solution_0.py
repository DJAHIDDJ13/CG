players = []
tributes = int(input())
for i in range(tributes):
    player_name = input()
    players += [player_name]
players.sort()

kills = {player: [] for player in players}
deaths = {player: "Winner" for player in players}
turns = int(input())
for i in range(turns):
    killer, victims = input().split(' killed ')
    victims = victims.split(', ')

    kills[killer] += victims
    for victim in victims:
        deaths[victim] = killer

for player in players:
    print("Name:", player)
    print("Killed:", ', '.join(sorted(kills[player])) if kills[player] else 'None')
    print("Killer:", deaths[player])
    if player != players[-1]:
        print()
