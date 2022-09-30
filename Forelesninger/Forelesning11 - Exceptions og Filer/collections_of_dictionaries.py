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

# Endrer navnet for andre spill (dictionary) i spill-listen
games[1]["name"] = "TEKKEN 8"

print(games[1])

print()
# Itererer og skriver ut alle spillene (dictionareis) i spill-listen
for game in games:
    print(game)

print()
# Iterer gjennom spill (dictionary) i spill-listen og skriver ut hvert spill sine nøkkel/verdi-par
# Altså skriver ut inneholdt informasjon for hvert spill
for game in games:
    for key, value in game.items():
        print(f"{key} - {value}")
    print()

print("\n---------Using a dictionary--------")
# Her oppretter vi en dictionary for å holde på spill.
# Vi benytter spillets navn som nøkkel og setter verdien til å være en dictionary med resten av informasjonen for
# dette spillet. Vi kunne eventuelt latt "name" forbli i dictionarien og laget en unik nøkkel for hvert spill.
games_dict = {
    "Dota 2": {"genre": "MOBA", "max players": 10},
    "TEKKEN 7": {"genre": "Fighting Game", "max players": 2}
}

print(games_dict)

print()
# For å hente ut informasjonen om et gitt spill, kan vi nå benytte spillets navn.
print(games_dict["Dota 2"])

# Her oppretter vi et nytt spill, ved å spesifierse spillets navn som nøkkel og en dictionary med
# den resterende informasjonen som verdi.
games_dict["Jump King"] = {"genre": "Platformer", "max players": 1}


print(games_dict)

print()
# Her henter vi ut sjangeren for spillet TEKKEN 7
print(games_dict["TEKKEN 7"]["genre"])

print()
# Vi iterer her gjennom spillene i spill-dictionarien.
for key, value in games_dict.items():
    # Basert på spill-dictionariens struktur, kan vi skrive ut en beskrivelse av et gitt spill ved å benytte
    # nøkkelen til å refere til navnet, og vi kan hente ut resten av informasjonen (sjanger og max antall spillere)
    # fra verdien.
    print(f"The game {key} is of the {value['genre']} genre and has "
          f"{value['max players']} max players.")


