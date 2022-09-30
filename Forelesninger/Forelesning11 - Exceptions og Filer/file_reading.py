# Kommentaren under demonstrerer hvordan vi manduelt kan opne og benytte en fil.
'''
file = open("zen_of_python.txt")
print(file.read())

# Vi bør sørge for filen lukkes når vi er ferdig med den.
file.close()

# Denne linjen ville ført til en exception fordi filen har blitt lukket.
print(file.read())
'''

# with-blokker er den anbefalte måten å åpne filer på i python.
# Med denne blokken kan vi definere åpningslogikken, oprette en midlertidig referanse til filen (en variabel), samt
# utføre operasjoner på denne filen. Når vi har gjennomgått all kode i with-blokken blir filen vi åpnet automatisk
# lukket.
with open("text_files/zen_of_python.txt") as file:
    # Skriver ut alt innholdet av filen zen_of_python.txt
    print(file.read())

print()
with open("text_files/zen_of_python.txt") as file:
    # readlines()-metoden kan benyttes for å få en liste med alle linjene i filen vi jobber med.
    print(file.readlines())

print()
with open("text_files/zen_of_python.txt") as file:
    # Hvis vi ønsker å jobbe med en og en linje i filen vi jobber med kan vi benytte readline()-metoden.
    # Merk at denne metoden er forskjellig fra readlines()-metoden.
    # Python vil holde styr på linejene vi har og ikke har gjennom gått, så hvert readline()-kall vil hente den
    # "neste" linjen i filen.
    # Under skriver vi dermed ut de to første linjene i filen. Vi benytter også rstrip()-metoden, som tilhører
    # str-datatypen for å fjerne linjeskiftet som er inneholdt for hver av disse linjene.
    print(file.readline().rstrip())
    print(file.readline().rstrip())

# Merk også at det er viktig at vi benytter riktig navn og filsti for filen vi ønsker å åpne
# Vi tar utgangspunkt i mappen til python filen vi jobber i.
# Hvis oppgitt navn og/eller filsti ikke stemmer, vil dette føre til en FileNotFoundException.
# Det kan dermed være fornuftig å benytte en try/except-blokk for å håndtere dette.
# Dette er generelt lurt når vi åpner filer, med mindre vi som programmerer har veldig stor kontroll på filen og
# hvor den ligger.
try:
    with open("text_files/zen_of_python.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found.")

