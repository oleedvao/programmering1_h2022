# I koden under forsøker vi å finne multiplayer spill for tre forskjellige spill-samlinger uten funksjoner.
# Dette blir fort uoversiktig og uintuitivt å lese.
# Hvis vi skal endre noe i logikken for å finne multiplayer-spill, må vi i så fall gjøre det individuellt for
# Alle listene.
# Å benytte "samme" logikk flere ganger og tungvinte endringer er begge gode indikasjoner på at man bør lage en
# funksjon.

games = {
    "DOTA 2": {"genre": "MOBA", "max_players": 10},
    "Gothic 2": {"genre": "RPG", "max_players": 1},
    "Trackmania": {"genre": "Racing", "max_players": 64}
}

print()
multiplayer_games = {}
for name, info in games.items():
    if info["max_players"] >= 2:
        multiplayer_games[name] = info
print(multiplayer_games)

games_2 = {
    "Tekken 7": {"genre": "Fighting", "max_players": 2},
    "Jump King": {"genre": "Platformer", "max_players": 1}
}

print()
multiplayer_games_2 = {}
for name, info in games_2.items():
    if info["max_players"] >= 2:
        multiplayer_games_2[name] = info
print(multiplayer_games_2)

games_3 = {
    "Tekken 7": {"genre": "Fighting", "max_players": 2},
    "Jump King": {"genre": "Platformer", "max_players": 1}

}

print()
multiplayer_games_3 = {}
for name, info in games_3.items():
    if info["max_players"] >= 2:
        multiplayer_games_3[name] = info
print(multiplayer_games_3)








