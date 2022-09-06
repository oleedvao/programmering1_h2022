# Demonstrer hvordan else fungerer.
if False:
    # Denne linjen vil ikke kjøre ettersom betingelsen er False
    print("Look the if-statment is False.")
else:
    # else-blokken, altså den inneholdte linjen, vil bare kjøre dersom if-betingelsen tilsvarer False
    print("This line will run, because the statement is False")

# Utskriften vil bli "The texts are NOT the same" ettersom if-betingelsen tilsvarer False og
# else-blokken vil dermed kjøre, men if-blokken vil ikke kjøre.
if "text" == "TEXT":
    print("The texts are the same.")
else:
    print("The texts are NOT the same.")


print() # Lager mellomrom i utskriften

# Demonstrerer hvordan vi kan benytte if, elif og else for å definere sammenhengende betingelser.
# Merk at disse betinelsene vil testes sekvensielt (fra toppen og nedover) og bare den første
# oppfylte betingelsen (altså som tilsvarer True) vil kjøre. Resten vil hoppes over.
number = 30
if number == 10: #Sjekker om number er nøyaktig 10
    print(f"{number} is ten.")
elif number > 0: #Sjekker om number er større enn 0 bare hvis forrige betingelse ikke er oppfylt
    print(f"{number} is a positive number.")
elif number < 0: #Sjekker om number er mindre enn 0 bare hvis forrige betingelse ikke er oppfylt
    print(f"{number} is a negative number.")
else: #Kjører hvis ingen av betingelsene over er oppfylt
    print(f"{number} is zero.")

print()


number = 69
# Demonstrerer bruk av and-operatoren for å definere en tallrekkevidde fra 0-100
# Hvis tallet er innenfor denne rekkevidden (100 inkludert) vil betingelsen være True.
# Dette kan gjøres ved bruk av and-operatoren og sjekke om tallet er større enn
# 0 OG mindre enn eller lik 100 på samme tid .
if number > 0 and number <= 100:
    print("The number is in the right range.")

# Demonstrerer bruk av or-operatoren for å definere en if-test som sjekker om tallet
# er nøyaktig 69 ELLER 42. Hvis tallet er enten 69 eller 42 vil koden kjøre.
if number == 69 or number == 42:
    print("Special number!")
