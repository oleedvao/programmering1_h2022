games_list = ["Disco Elysium", "Hunt: Showdown", "Jump King", "Stardew Valley"]

# Gjennomgår hvert element i listen games_list og skriver ut dette elementet i en passende utskrift.
# Mer at game praktisk talt vil fungere som en referanse til et gitt element for en gitt iterasjon i løkken.
for game in games_list:
    print(f"{game} is a good game!") # game vil her ha en unik verdi for hver iterasjon i løkken (elementen i listen)
    print("You should try it!\n")


dark_souls = "Dark Souls"
# Itererer gjennom hvert tegn i en tekststreng og skriver det ut
for character in dark_souls:
    print(character)
