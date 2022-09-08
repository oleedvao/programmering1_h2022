# Oppretter en liste av tilfeldige elementer (av tilfeldige datatyper)
random_list = ["Europe", 8, 2.4, False, ["Some element", 42]]
print(f"Random list: {random_list}")

# Oppretter en liste med tekststrenger som representerer navn på spill
games = ["Dark Souls", "Disco Elysium", "God of War", "Hunt: Showdown", "Dota 2"]
print(f"Games list: {games}")

# Referer til en spesifikk verdi i listen ved bruk av index.
# Husk at indexer starter på 0 og går oppover. 0 -> første element, 1 -> andre element, osv.
print(f"Index 2 in games: {games[2]}") # Referer til og skriver ut verdien på index 2 (tredje element -> "God of War")

# Kopierer verdien på index 1 ("Disco Elysium") til en variabel
specific_game = games[1]
print(f"Copy of index 1 in games: {specific_game}")

# Endrer/oppdaterer verdien på index 2 ("God of War")
games[2] = "God of War (2018)"
print(f"Games after changing the element on index 2: {games}")

# Legger til "Stardew Valley" på slutten av listen
games.append("Stardew Valley")
print(f"Games after appending 'Stardew Valley': {games}")

# Setter inn verdien "Jump King" på index 1
games.insert(1, "Jump King")
print(f"Games after inserting 'Jump King' on index 1: {games}")
# Setter inn verdien "TEKKEN 7" på index 4
games.insert(4, "TEKKEN 7")
print(f"Games after inserting 'TEKKEN 7' on index 4: {games}")

#Fjerne siste element i lista
games.pop()
print(f"Games after removing (popping) the last element: {games}")

# Fjerner elementet på index 3
games.pop(3)
print(f"Games after removing (popping) the element on index 3: {games}")

# Fjerner elementet på index 3 og setter det inn i en variabel
popped_game = games.pop(3)
print(f"Popped game (from index 3): {popped_game}")
print(f"Games after removing (popping) the element on index 3 (again): {games}")

# Lager en sortert kopi av listen og setter den inn i en variabel
sorted_games = sorted(games)
# sorted_games = sorted(games, reverse=True) # Vi kunne også sortert i reversert rekkefølge
print(f"Sorted Copy of games: {sorted_games}")
print(f"Games after creating sorted copy (No change): {games}")

# Sorterer listen direkte
games.sort()
print(f"Games after creating sorting the list directly: {games}")

# Sorterer listen direkte, men reversert. I dette tilfellet hvor elementene i listen er tekst
# vil det si at elementene vil sorteres fra Å til A.
games.sort(reverse=True)
print(f"Games after creating sorting the list directly (reversed): {games}")

# Returnerer lengden av en liste. Altså hvor mange elementer listen inneholder.
# Siste index vil da være lengden av listen - 1.
print(f"Lenght of list: {len(games)}")
