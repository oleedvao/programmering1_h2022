# Vi har nå definert logikken for å finne multiplayer-spill som en funksjon.
# Merk at vi benytter en parameter for å ta imot en dictionry for spill. På den måten trenger vi ikke å forholde oss
# til spesifikke liste. Vi bestemmer denne senere når vi kaller funksjonen (den spesifikke listen sendes som argument).
# Merk at vi også har definert funksjonen til å returnere en ny dictionary. Dette kan ofte være fordelaktig overfor å
# bare skrive den ut, fordi vi da kan ta den imot ved funksjonskall og eventuelt gjør noe med den etterpå.
def get_multiplayer_games(games_dict):
    multiplayer_games = {}
    for name, info in games_dict.items():
        if info["max_players"] >= 2:
            multiplayer_games[name] = info
    return multiplayer_games



games = {
    "DOTA 2": {"genre": "MOBA", "max_players": 10},
    "Gothic 2": {"genre": "RPG", "max_players": 1},
    "Trackmania": {"genre": "Racing", "max_players": 64}
}

print(get_multiplayer_games(games))

games_2 = {
    "Tekken 7": {"genre": "Fighting", "max_players": 2},
    "Jump King": {"genre": "Platformer", "max_players": 1}
}

multiplayer_games_2 = get_multiplayer_games(games_2)
print(multiplayer_games_2)

games_3 = {
    "Tekken 7": {"genre": "Fighting", "max_players": 2},
    "Jump King": {"genre": "Platformer", "max_players": 1}

}

multiplayer_games_3 = get_multiplayer_games(games_3)
print(multiplayer_games_3)








