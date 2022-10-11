import random

# Liste med ord vi kan velge tilfeldig av.
# Dette kan være et fint sted å starte koden ettersom all annen funksjonalitet er direkte eller indirekte
# basert på et ord vi skal forsøke å gjette.
words = ["World", "Pineapple", "Cat", "Python", "Armadillo"]

# Henter ut et tilfeldig valgt ord basert på en tilfeldig index.

word_to_guess = words[random.randrange(0, len(words))]

# Oppretter en ny liste med hver bokstav i ordet som individuelle elementer
# Dette benyttes lenger ned i koden for å holde oversikt over forskjellige bokstaver sin posisjon
word_to_guess_list = list(word_to_guess)

# Utskrifter benyttet til testing under programmets skrivning
#print("".join(word_to_guess_list))
#print(word_to_guess_list)
#print(word_to_guess)

# Generer en liste med "_" som hvert element og antallet av dette elementet er basert på ordets lengde.
# Denne listen er ment til å representere et "hint" til spilleren og skal senere oppdateres basert på hvilken bokstav
# spilleren gjetter.
# Denne teknikken ble funnet ved å google. Alternativt kunne vi gjort dette mer manuelt ved å lage en
# for-løkke som iterativt fyller listen med "_" basert på ordet lengde.
hint = ["_"] * len(word_to_guess)
# Skriver ut en tekstlig representasjon av hintet: ''.joint(hint)
# og sørger for at første bokstav blir uppercase .capitalize()
# Begge disse teknikkene ble funnet ved å google.
print(f"Hint: {''.join(hint).capitalize()}")

# Variabel som representerer spillerens antall liv. Blir initielt satt til 6.
lives = 6

# Vi gjetter på bokstaver så lenge det er flere ukjente bokstaver og så lenge vi har flere liv igjen.
while "_" in hint and lives > 0:
    print()

    # Vi henter en gjettet bokstav fra spilleren
    guess = input("Guess a letter: ")

    # Vi sjekker om spillerens gjettede bokstav er inneholdt i ordet eller ikke
    # For å sørge for at vi ikke får problemer hvor vi sammenligner en lowercase bokstav mot en uppercase sørger vi
    # for at både bokstaven spilleren gjettet og ordet vi sjekker innholdet av begge behandles i lowercase format
    # ved bruk av .lower().
    if guess.lower() in word_to_guess.lower():
        # Hvis bokstaven er inneholdt i ordet:
        # Gjennomgår hver posisjon i ordet vi skal gjette
        for index in range(len(word_to_guess_list)):
            # Hvis den gjettede bokstaven er likt bokstaven på den nåværende posisjonen ...
            if guess.lower() == word_to_guess_list[index].lower():
                # ... oppdaterer vi denne posisjonen i hintet til å være bokstaven vi gjettet.
                hint[index] = guess
    else:
        # Hvis bokstaven ikke er inneholdt i ordet mister vi ett liv.
        lives -= 1

    print()
    # Skriver ut det oppdaterte hintet og hvor mange liv vi har igjen.
    print(f"Hint: {''.join(hint).capitalize()}")
    print(f"Current lives: {lives}")



