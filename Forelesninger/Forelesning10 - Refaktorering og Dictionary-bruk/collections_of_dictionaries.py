# Her oppretter vi en liste som inneholder elementer som hver representerer et individuelt spill.
# Hvert element er her en egen dictionary, men inneholdte nøkkel/verdi-par for navn, sjanger og antall spillere.
games = [
    {"name": "Dota 2", "genre": "MOBA", "max players": 10},
    {"name": "TEKKEN 7", "genre": "Fighting Game", "max players": 2}
]

print(games)

# Hvis vi skal legge til et element til spill-listen, kan vi i så fall benyttet append()-metoden, men
# sende med en dictionary som parameter.
games.append({"name": "Jump King", "genre": "Platformer", "max players": 1})

print(games)

print()
# Skriver ut første element i spill-listen (En dictionary).
print(games[0])
# Skriver ut første element i spill-listen (dictionarien) sin sjanger ved å referere til nøkkelen "genre".
print(games[0]["genre"])
