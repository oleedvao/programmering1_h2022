# Importerer modulen random, som er nødvendig for å bruke metoden randrange()
import random

# Genererer et initielt og tilfeldig gjett på et tall mellom 1 og 100
guess = random.randrange(1, 101)

# Så lenge gjettet ikke er det riktige tallet (69) skal vi gjette på nytt
while guess != 69:
    print(f"The guess was: {guess}")
    guess = random.randrange(1, 101) # Oppdaterer gjettet med et nytt gjett (nytt tilfeldig tall mellom 1 og 100)

#Hvis løkken er ferdig, vet vi at tallet må ha blitt 69.
print("The guess was correct. The number is 69.")