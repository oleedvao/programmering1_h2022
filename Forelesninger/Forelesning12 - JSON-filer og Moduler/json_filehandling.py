# For å håndtere JSON-filer på en enkel måte kan vi importere json-modulen, som har en rekke med funksjoner
# som gjør dette meget enkelt.
import json

# Oppretter en dictionary som vi ønsker å skrive til fil i JSON-format
# Denne dictionarien kunne være mye mer komplisert, med inneholde lister eller dictionaries uten at dette hadde
# vært et problem.
game = {"name": "Gothic", "genre": "RPG", "max players": 1}



# ---------JSON filskriving og -lesing uten feilhåndtering (essensen)---------
# Denne koden skriver en dictionary til fil i JSON-format
# Merk at vi må spesifisere enten "w" eller "a" som opsjon for open() for å kunne skrive til fil.
with open("text_files/game.json", "w") as file:
    # json.dump()-funksjonen tar en dictionary og en fil som parameter, og skriver dictionarien til den gitte
    # filen. Vi kan eventuelt formatere JSON-innholdet som vi skriver på en pen måte ved å definere en verdi for
    # parameteren indent. F.eks. 4 for å få 4 mellomrom som indentering i filen.
    json.dump(game, file, indent=4)

# Denne koden leser en JSON-fil og konverterer innholdet til en dictionary.
# Ettersom vi leser fra fil, trenger vi ikke definere noen ekstra opsjon.
with open("text_files/game.json") as file:
    # Vi kan benytte json.load() med en fil som parameter for å konvertere JSON-innholdet til en dictionary
    # vi kan benytte i videre programmering. Mer at dette forutsetter at filen faktisk har JSON-innhold. (Se
    # feilhåndtering under.)
    dict_from_file = json.load(file)

# Etter å lastet innholdet av en JSON-fil, kan vi benytte det som en vanlig dictionary
# Dette forutsetter også at det ikke har skjedd noe feil i konverteringen.
print(dict_from_file)
print(dict_from_file["name"])



# ---------JSON filskriving og -lesing med feilhåndtering (Anbefalt løsning)---------

# Her skriver vi en dictionary til JSON-fil, med feilhåndtering.
# Når vi skriver til fil kan det forekomme en FileNotFoundError, hvis vi ikke finner lokasjonen av filen.
try:
    # Dette er den hovedsakelige koden for å skrive dictionary til JSON-fil. Se det essenseielle
    # løsningsforlaget for mer informasjon
    with open("text_files/game.json", "w") as file:
        json.dump(game, file, indent=4)
except FileNotFoundError:
    # Hvis vi ikke finner filen, gir vi en enkel tilbakemelding til brukeren.
    print("File not found.")

# Denne koden leser en JSON-fil og konverterer innholdet til en dictionary med feilhåndtering.
# Når vi leser en JSON-fil kan det forekomme en FileNotFoundError, hvis vi ikke finner lokasjonen av filen,
# samt at vi kan få en json.decoder.JSONDecodeError hvis innholdet av filen vi leser ikke er på JSON-format.
try:
    # Dette er den hovedsakelige koden for å laste en dictionary fra en JSON-fil. Se det essenseielle
    # løsningsforlaget for mer informasjon
    with open("text_files/game.json") as file:
        dict_from_file = json.load(file)
except FileNotFoundError:
    # Hvis vi ikke finner filen, gir vi en enkel tilbakemelding til brukeren.
    print("File not found.")
except json.decoder.JSONDecodeError:
    # Hvis innholdet av filen ikke er i JSON-format, gir vi en enkel tilbakemelding til brukeren.
    print("File content is not JSON.")
else:
    # Hvis alt går bra (ingen feil forekommer) vet vi at dictionarien har blir riktig lastet fra fil og
    # kan trygt benytte den.
    print(dict_from_file)
    print(dict_from_file["name"])