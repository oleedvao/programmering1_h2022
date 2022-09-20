# Oppretter en dictionary med {}. Merk at hvert element består av to ting: En nøkkel og en tilhørende verdi,
# skilt med :. Nøkler kan i utganspunktet være hva som helst, men er typisk tekstverdier, mens den tilhørende verdien
# er helt opp til oss; Tekst, tall, boolean, en liste - Anything goes.
# Med dictionaries kan vi relativt enkelt lage en variabel som kan representere "noe" som har flere konseptuelt
# sammenhengende verdier. Her tar vi utgangspunktet i et spill som har verdier for navn og sjanger.
game = {
    "name": "Dota 2",
    "genre": "MOBA"
}

# Hvis vi skal refere til en verdi i en dictionary må vi refere til dens sammenhengende nøkkel.
# Dictionaries har ikke indexer, så vi kan ikke hente ut elementer basert på posisjon.
# første alternativ for å hente ut et element er å benytte []. Merk at denne måten gir en feilmelding hvis nøkkelen
# ikke eksisterer. Merk også at nøkler er Case Sensitive, så store og små bokstaver må stemme overens.
print(game["name"])
# Alternativt kan vi hente ut verdier ved bruk av get()-metoden. Denne vil returnere None hvis nøkkelen ikke finnes.
print(game.get("Genre"))

# For å endre elementer i en dictionary gjør vi det på følgende måte.
# Merk at dette igjen forutsetter at nøkkelen eksisterer i dictionarien.
print()
game["name"] = "DOTA 2"
print(game)

# For å legge til elementer i en dictionary gjør vi det med samme syntaks som når vi endrer et element.
# Dette forutsetter imidlertid at nøkkelen vi spesifiserer ikke allerede eksisterer i dictionarien, ettersom vi da
# hadde endret på verdien for den nøkkelen.
# Den følgende koden legger til en ny nøkkel, "max players", med verdien 10.
print()
game["max players"] = 10
print(game)

# For å fjerne elementer kan vi benytte pop()-metoden, og spesifisere en nøkkel for å fjerne denne nøkkelen og
# dens tilhørende verdi.
print()
game.pop("max players")
print(game)
# Alternativt kan vi benytte nøkkelordet del sammen med en referanse til nøkkelen (og dens verdi) vi ønsker å fjerne. 
print()
del game["genre"]
print(game)
