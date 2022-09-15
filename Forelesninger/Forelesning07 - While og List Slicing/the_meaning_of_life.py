#NB! Mer utfyllende kommentarer kommer


# Løkken vil i utganspunktet kjøre uendelig med mindre vi manuelt avbryter den
while True:

    guess = input("What is the meaning of life?: ")
    if guess == "42":
        print("Correct!")
        break
        #exit()
    else:
        print("Nope! Try again.")

print("Thanks for guessing!")