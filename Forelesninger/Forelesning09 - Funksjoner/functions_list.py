import random


def pick_random_boardgame(boardgames):
    boardgame_index = random.randrange(len(boardgames))
    return boardgames.pop(boardgame_index)


def print_list(list_to_print):
    for element in list_to_print:
        print(element)


print("Board Games:")
board_games = ['Ubungo', 'Pandemic', 'Ticket To Ride', 'Monopoly', 'Risk']
print_list(board_games)

# picked_boardgame = pick_random_boardgame(board_games)
picked_boardgame = pick_random_boardgame(board_games[:])

print(f"\nYou picked {picked_boardgame}. Have fun playing!")

print("\nUpdated board games list:")
print_list(board_games)



# print("\nRandom list:")
# random_list = [42, 9001, 3.14, 'Norway', 'Python']
# print_list(random_list)
