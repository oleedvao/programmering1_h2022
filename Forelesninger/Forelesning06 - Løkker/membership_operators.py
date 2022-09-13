games_list = ["Disco Elysium", "Hunt: Showdown", "Jump King", "Stardew Valley"]

# Sjekker om "Disco Elysium" er et inneholdt element i games_list listen.
# I så fall, skriver vi ut en passende tekst.
if "Disco Elysium" in games_list:
    print("Cool!")

# Sjekker om Dark Souls IKKE er en del av games_list.
# I så fall, skriver vi ut en passende tekst.
if "Dark Souls" not in games_list:
    print("Bro, you need to play that!")

# Sjekker om teksten "Battle Royale" er delvis eller fulstendig inneholdt i tekststrengen opinion.
# I så fall skriver vi ut en passende(?) melding.
opinion = "I hecking love Battle Royale games!"
if "Battle Royale" in opinion:
    print("Washed up genre...")

# NB! Merk at alle disse sjekkene er Case Sensitive.
# Store og små bokstaver må være samvarig med det vi sjekker opp mot.