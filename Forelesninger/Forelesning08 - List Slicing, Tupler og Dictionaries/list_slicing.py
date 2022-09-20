games = ["Dark Souls", "Disco Elysium",
         "Hunt: Showdown", "TEKKEN 7", "Dota 2", "Hollow Knight", "Jump King"]

# Kopierer en del av listen
print(games[1:5]) # Lager en liste med elementene fra index 1 i games til, men ikke med, index 5
print(games[2:4]) # Lager en liste elementene fra index 2 til, men ikke med, index 4

# Lager en liste med hvert tredje element innenfor rekkevidden av index 1 til, men ikke med, index 5
print(games[1:5:3])

print()
print(games[:]) # Lager en fullstendig kopi av den orginale listen.
print(games[2:]) # Lager en liste med alle elementer fra og med index 2 til slutten av listen
print(games[:2]) # Lager en liste med alle elementer fra starten av listen til, men ikke med, index 2

print()
#Benytter negative indexer for å arbeide med elementer relativt til slutten av listen
print(games[-2]) # referer til nest siste element (siste element er alltid på index -1)
print(games[-5:-2]) # Lager en liste fra det femte siste elementet til det nest siste elementet

print()
# Vi kan også benytte slicing basert på index. Hvert tegn vil få en egen index som starter på 0.
classic_game = "Shadow of the Colussus"
print(classic_game[10:]) # Lager en ny tekststreng med tegnene fra index 10 til slutten av stengen.