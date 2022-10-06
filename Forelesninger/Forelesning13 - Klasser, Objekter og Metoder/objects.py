# Vi importerer Student-klassen fra college_module for å få tilgang til denne klassen direkte i denne filen.
from college_module import Student

# Vi benytter her Student-klassen til å opprette et Student-objekt. Dette kan konseptuelt tenkes på som at vi
# oppretter en unik student, med unike verdier for dens "egenskaper". Hvilke "egenskaper" er basert på klassens
# definisjon og verdiene for disse settes under opprettelse.
# For å opprette et objekt av en klasse, skriver vi <Klassenavn>(<parameter 1>, <parameter 2>, ...)
# Parameterene vil her være basert på de vi definerte (etter self) i klassens __init__()-metode.
# Altså vil parameteren under representere firstname, lastname, age og student_id, respektivt.
# Med andre ord, oppretter vi en student med fornavn - Ola, etternavn - Nordmann, alder - 25 og studentID - 123456, og
# vi lagrer dette objektet i en variabel som heter student_1.
student_1 = Student("Ola", "Nordmann", 25, 123456)

# Når vi har opprettet et objekt kan vi benytte dette objektet til å hente ut de spesifikke verdiene for dette
# objektets "egenskaper".
# Dette gjøres med formatet <objekt>.<instansvariabel> og vil returnere den gjeldende verdien for akkurat dette
# objektet sin instansvariabel.
print(student_1.firstname) # -> Ola
print(student_1.lastname) # -> Nordmann
print(student_1.age) # -> 25
print(student_1.student_id) # -> 123456
print(f"{student_1.firstname} {student_1.lastname}") # -> Ola Nordmann

# Vi kan også endre verdiene for et objekt sine instansvariabler
student_1.age = 35
print(student_1.age) # -> 35

print()
# Vi kan også opprette så mange Student-objekter vi ønsker, hver med sine unike verdier.
# Her oppretter vi en student med navn Kari Nordmann, med alder 30 og 654321
student_2 = Student("Kari", "Nordmann", 30, 654321)
print(student_2.firstname) # -> Kari
print(student_2.age) # -> Nordmann

print()
# Vi kan fremdeles refere til og hente ut verdier for det første studentobjektet, og dette vil fremdeles ha
# verdiene i satt for akkurat DET objektet.
print(student_1.firstname) # -> Ola

print()
# Under benytter vi metoden get_description() for å hente ut en tekstlig beskrivelse av hvert Student-objekt.
# Merk at hver av disse beskrivelsene er unike basert på hvert objekt sine verdier for firstname, lastname, age og
# student_id
print(student_1.get_description())
print(student_2.get_description())