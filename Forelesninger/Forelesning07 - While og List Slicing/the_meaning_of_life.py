
# Løkken vil i utganspunktet kjøre uendelig med mindre vi manuelt avbryter den
while True:
    # For hver gjennomgang av løkken spør vi brukeren etter et svar på meningen med livet
    guess = input("What is the meaning of life?: ")

    # Håndterer tilfellene hvor svaret er riktig og feil
    if guess == "42":
        print("Correct!")
        # Hvis svaret er riktig ønsker vi å bryte den uendelige løkken. Dette kan vi gjøre med nøkkelordet break.
        # Alternativt kunne vi avsluttet hele programmet med exit(), men i så fall ville ikke kodelinjen etter
        # løkken kjørt.
        break
    else:
        print("Nope! Try again.")

print("Thanks for guessing!")