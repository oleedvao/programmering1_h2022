# For å få tilgang til funksjonene definert i json_module.py, kan vi importere denne filen som en modul.
import json_module

# Vi definerer en dictionary vi kan benytte for å skrive til fil.
game = {"name": "Trackmania", "genre": "Racing",
        "max players": 64}

# Vi spesifiserer en variabel for å holde på filnavnet vi ønsker å jobbe med, for å unngå unødvendig repetisjon
# av dette navnet.
filename = "text_files/game2.json"

# For å skrive en dictionary til fil kan vi nå benytte write_json()-funksjonen gjennom json_module
json_module.write_json(game, filename)

# For å laste en dictionary fra JSON-fil kan vi nå benytte load_json()-funksjonen gjennom json_module
dict_from_file = json_module.load_json(filename)
print(dict_from_file)
print(dict_from_file["name"])

# Ettersom vi nå benytter funksjoner med parametere, kan vi dynamisk like enkelt også gjøre noe med andre filer.
# Under benytter vi igjen load_json()-funksjonen, men laster her fra en annen fil.
other_dict_from_file = json_module.load_json("text_files/game.json")
print(other_dict_from_file)
print(other_dict_from_file["name"])

