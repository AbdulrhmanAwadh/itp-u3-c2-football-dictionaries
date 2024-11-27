def players_by_position(squads_list):
    players_by_position = {}

for player in players_dicts:
    position = player['position']
    if position not in players_by_position:
        players_by_position[position] = []
    players_by_position[position].append(player)

print(players_by_position)
