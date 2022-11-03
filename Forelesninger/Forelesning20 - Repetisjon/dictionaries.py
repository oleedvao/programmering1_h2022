# Nested dictionary som representerer en samling med spill. Vi benytter spillets navn som nøkkel og
# verdien blir satt til en egen dictionary med spillets informasjon
games = {
    "DOTA 2": {"genre": "MOBA", "max_players": 10},
    "Gothic 2": {"genre": "RPG", "max_players": 1},
    "Trackmania": {"genre": "Racing", "max_players": 64}
}

# For å hente ut spillets "informasjon" kan vi nå refere til spillets navn, ettersom dette benyttes som nøkkel.
# Dette vil resultere i en dictionary.
print(games["DOTA 2"])

# Hvis vi ønsker å aksessere en spesifikk verdi av et spill sin informasjon kan vi for eksempel mellomlagre
# resultatet av games["DOTA 2"] (en dictionary) for deretter å hente ut en verdi basert på nøkkel.
dota_2_info = games["DOTA 2"]
print(dota_2_info)
print(dota_2_info["max_players"]) # Henter ut antall spillere for DOTA 2

# Alternativt for å mellomlagre dictionarien vi får av games["DOTA 2"], kan vi hente ut antallspillere direkte.
# Linjen under vil også hente ut antall spillere for DOTA 2
print(games["DOTA 2"]["max_players"])

# Vi kan også endre verdier på samme måte:
games["DOTA 2"]["max_players"] = 11
print(games["DOTA 2"]["max_players"])

print()
# Under "kopierer" vi alle multiplayer-spill (2 eller flere spillere) til en ny dictionary.
multiplayer_games = {}
# For å holde på en referanse til både spillets navn og info, benytter vi .items().
for name, info in games.items():
    # info er nå en egen dictionary med nøkkel/verdi-par for sjanger og antall spillere.
    # Vi kan derfor hente ut verdier fra info via nøklene.
    if info["max_players"] >= 2:
        multiplayer_games[name] = info
print(multiplayer_games)
