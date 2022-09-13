# En for-løkke som vil iterere gjennom tallene 0 - 9, generert ved bruk av range()-funksjonen
# Merk at her bare definerer slutt-tallet med range men at dette tallet vil definere "til, men ikke med".
# Hvis vi bare definerer slutt-tallet, vil start-tallet være 0 som standard.
# Dermed 0 - 9
for number in range(10):
    print(number)

# En for-løkke som iterer gjennom tallene 5 - 10
# Her benytter vi range() til definere både start- og slutt-tall.
# Løkken vil da starte fra og med første verdi i parantesen, til, men ikke med, andre verdi i parantesen.
print()
for number in range(5, 11):
    print(number)

# En for-løkke som iterer gjennom tallene 5 - 10, med 3 som stegstørrelse
# Her benytter vi range() til definere både start- og slutt-tall, samt stegstørrelse/intervall mellom hvert tall.
# Første verdi i parantesen vil da representere start-tall, andre verdi slutt-tall, og tredje verdi stegstørrelsen.
print()
for number in range(5, 11, 3):
    print(number)

# Hvis vi skriver ut range vil vi se at vi får en "rar" datatype, men som egentlig fungerer mye likt som en liste.
print()
print(range(10))

# Hvis vi skulle ønske å "konvertere" range til en liste, kunne vi forsåvidt gjort dette manuelt.
# Her gjør vi dette ved å fylle en initielt tom liste med tallene vi gjennomgår i for-løkken under
print()
number_list = []
for number in range(5):
    number_list.append(number)
    print(number_list)

print()
print(number_list)

# Alternativt, og lettere, kan vi direkte konvertere en range til en liste ved bruk av list()-funksjonen.
print()
range_list = list(range(5, 15))
print(range_list)