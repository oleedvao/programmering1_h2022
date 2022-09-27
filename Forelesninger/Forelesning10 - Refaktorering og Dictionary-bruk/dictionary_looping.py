# Dictionary som representerer ett spill.
game = {
    "name": "Dota 2",
    "genre": "MOBA",
    "max players": 10
}

# Hvis vi definerer en løkke på vanlig måte, men med en dictionary vil vi som standard iterere gjennom alle
# nøkkelnavnene i dictionarien.
for key in game:
    print(key)

print()
# Alternativt kan vi iterere gjennom nøkkelnavnene ved å bruke dictionarien sin keys()-metoden, som gjør
# akkurat det samme som løkken over, men som gjør ting litt mer eksplisitt i måten ting blir skrevet.
for key in game.keys():
    print(key)

print()
# Hvis vi ønsker å iterere gjennom alle verdiene i dictionarien, kan vi benytte dictionarien sin values()-metode.
for key in game.values():
    print(key)

print()
# Til slutt, hvis vi ønsker å iterere gjennom både nøkkelnavn og verdi for hvert element i en dictionary
# kan vi benytte dictionarien sin items()-metode, samt definere opp referanser for både nøkkel og verdi.
# Merk her at referansene må være skilt med komma, og vi må alltid definere en referanse for nøkkelen
# først, så for verdien.
for key, value in game.items():
    # Resultatet av de to referansene, er at vi kan benytte både nøkkel og verdi, samtidig i løkken.
    print(f"{key} -> {value}")