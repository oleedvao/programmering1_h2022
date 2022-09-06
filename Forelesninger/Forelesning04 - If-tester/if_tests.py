# Generel definisjon og funksjonalitet av en if-test

if True: #if <betingelse tilsvarende True/False>:
    # Disclaimer: Vanligvis ville vi ikke satt True/False direkte, men heller definere en betingelse
    # med sammenligningsoperatorer.
    # Merk at bare de linjene som er indenterte tilhører if-testen og disse vil bare kjøre
    # hvis betingelsen tilsvarer True.
    print("Look, the if-statement is True.")
    print("We can add more than one line.")


# Eksempel hvor vi definerer en betingelse som tilsvarer en True-verdi
statement = 2 == 2 # Sjekker om 2 er lik 2. Dette stemmer og returnerer True.
if statement:
    print(f"The if-statement runs because the statement is {statement}")

# Eksempel hvor vi definerer betingelsen direkte i if-testen. Dette er det vanligste.
# Det er likevel vanligere å definere betingelsen ved å benytte variabler overfor å
# definere verdiene direkte.
if "text" == "TEXT":
    print("The texts are the same.")

print() # tom print for å lage opphold i utskriften

# En rekke uavhengige if-tester som sjekker om et tall, number, er positivt, negativt
# eller lik 0
number = 0
if number > 0: # Sjekker om tallet er positivt (større enn 0)
    print(f"{number} is a positive number.")

if number < 0: # Sjekker om tallet er negativt (mindre enn 0)
    print(f"{number} is a negative number.")

if number == 0: # Sjekker om tallet er nøyaktig 0
    print(f"{number} is zero.")
