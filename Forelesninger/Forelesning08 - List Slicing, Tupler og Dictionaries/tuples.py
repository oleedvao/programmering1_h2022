# Oppretter en tuple med (). Denne "liste-typen" fungerer mye likt som en vanlig liste, men er immutable.
# Det vil si at vi ikke kan endre på en tuple etter den er opprettet. Altså ikke legge til elementer,
# endre elementer eller fjerne elementer.
games = ("Dark Souls", "Disco Elysium", "Hunt: Showdown",
        "TEKKEN 7", "Dota 2", "Hollow Knight", "Jump King")

print(games)

print()
# Vi har lov til å refere til eller kopiere elementer i en tuple...
print(games[1])
print(games[5])

# ..., men vi kan ikke endre på tuplen på noen som helst måte
games[3] = "TEKKEN 8"
# Metoder for å legge til eller fjerne elementer eksisterer faktisk ikke for tuple-datatypen, og er dermed ikke
# tilgjengelig.
games.append("Tetris")
games.insert(4, "Tetris")
games.pop(5)
games.remove("Jump King")