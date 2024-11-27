def players_as_dictionaries(squads_list):
    SQUADS_DATA = [
  [
    "1", "GK", "Juan Botasso", "(1908-10-23)23 October 1908 (aged 21)", "", "Quilmes", "Argentina", "Argentina", "1930"
  ],
  [
    "9", "FW", "Roberto Cherro", "(1907-02-23)23 February 1907 (aged 23)", "", "Boca Juniors", "Argentina", "Argentina", "1930"
  ]
]

players_dicts = [
    {
        'number': player[0],
        'position': player[1],
        'name': player[2],
        'date_of_birth': player[3],
        'caps': player[4],
        'club': player[5],
        'country': player[6],
        'club_country': player[7],
        'year': player[8]
    } for player in SQUADS_DATA
]

print(players_dicts)

