games_list = ["Disco Elysium", "Hunt: Showdown", "Jump King", "Stardew Valley"]

# Her benytter vi en for-løkke til å fylle listen med spillene i Dark Souls serien.
# Altså Dark Souls 1 til 3.
# Vi benytter da range for å iterere gjennom tallene 1 til 3 og benytter referansen
# til det gjeldende tallet i en iterasjon, number_in_series, for å lage en dynamisk tekstreng vi legger til i listen.
for number_in_series in range(1, 4):
    games_list.append(f"Dark Souls {number_in_series}")

print(games_list)

# Fyller opp en ny liste med bare de spillene i game_list som IKKE er i Dark Souls serien.
games_without_ds = []
for game in games_list: # Vi går gjennom alle spillene (spill-titlene) i game_list
    if "Dark Souls" not in game: # sjekker om teksten IKKE er inneholdt i spillets tittel
        games_without_ds.append(game) # i så fall, legger vi til dette spillet i den nye listen

# Resultatet blir da en ny liste med spill utenom de som var i Dark Souls serien.
print()
print(f"Games without Dark Souls games: {games_without_ds}")