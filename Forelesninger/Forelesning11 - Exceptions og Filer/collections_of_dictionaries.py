# Kommentarer kommer
games = [
    {"name": "Dota 2", "genre": "MOBA", "max players": 10},
    {"name": "TEKKEN 7", "genre": "Fighting Game", "max players": 2}
]

print(games)

games.append({"name": "Jump King", "genre": "Platformer", "max players": 1})

print(games)

print()
print(games[0])
print(games[0]["genre"])

games[1]["name"] = "TEKKEN 8"

print(games[1])

print()
for game in games:
    print(game)

print()
for game in games:
    for key, value in game.items():
        print(f"{key} - {value}")
    print()

print("\n---------Using a dictionary--------")
games_dict = {
    "Dota 2": {"genre": "MOBA", "max players": 10},
    "TEKKEN 7": {"genre": "Fighting Game", "max players": 2}
}

print(games_dict)

print()
print(games_dict["Dota 2"])

games_dict["Jump King"] = {"genre": "Platformer", "max players": 1}


print(games_dict)

print()
print(games_dict["TEKKEN 7"]["genre"])

print()
for key, value in games_dict.items():
    print(f"The game {key} is of the {value['genre']} genre and has "
          f"{value['max players']} max players.")


