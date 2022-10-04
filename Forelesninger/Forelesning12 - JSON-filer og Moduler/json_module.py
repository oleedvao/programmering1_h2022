# Denne filen (json_module.py) er en vanlig python-fil, men vi benytter den til å samle funksjoner for å skrive og
# lese JSON-filer. Vi kan dermed benytte denne filen som en modul og importere den i andre filer for å tilgang
# til de inneholdte funksjonene.

import json # for å benytte json.dump() og json.load() under, må vi fremdeles importere json-moduel.

#Funksjonene under er basert på de anbefale implementasjonene for å skrive og lese JSON-filer, som demonstrert i
# json_filehandling.py. Altså variantene med feilhåndtering.

# Denne funksjonen skriver en dictionary til en fil.
# Vi spesifiserer akkurat hvilken dictionary og hvilken fil dette skal gjelde via parametere.
def write_json(dictionary, filename):
    try:
        # Vi åpner filen basert på det spesifiserte filnavnet i filename-parameteren.
        with open(filename, "w") as file:
            # Vi skriver dictionarien spesifisert i parameteren dictionary til filen vi åpnet.
            json.dump(dictionary, file, indent=4)
    except FileNotFoundError:
        print("File not found.")

# Denne funksjonen laster og returnerer en dictionary fra en JSON-fil.
# Vi spesifisere hvilken fil dette skal gjelde via parametere.
def load_json(filename):
    try:
        # Vi åpner filen basert på det spesifiserte filnavnet i filename-parameteren.
        with open(filename) as file:
            # Vi laster en en dictionary basert på filen vi åpnet.
            dict_from_file = json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except json.decoder.JSONDecodeError:
        print("File content is not JSON.")
    else:
        return dict_from_file
