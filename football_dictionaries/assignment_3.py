def players_by_country_and_position(squads_list):
    players_by_country_and_position = {}

for player in players_dicts:
    country = player['country']
    position = player['position']
    
    if country not in players_by_country_and_position:
        players_by_country_and_position[country] = {}
    
    if position not in players_by_country_and_position[country]:
        players_by_country_and_position[country][position] = []
    
    players_by_country_and_position[country][position].append(player)

print(players_by_country_and_position)
