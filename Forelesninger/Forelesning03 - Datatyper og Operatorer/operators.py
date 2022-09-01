# Bruk av operator med tall direkte (Multiplikasjon).
print(2 * 3)

# Variabler for å gjøre operasjoner med
int_variable = 42
operation_variable = 2

# Addisjon
# Resultatet av operasjonen blir lagret i addition_result-variabelen
addition_result = int_variable + operation_variable
print(f"Addition: {addition_result}")

# Divisjon
# Her gjør vi operasjonen direkte i sting-definisjonen
# Merk at resultatet av divisjon blir en float uansett hvilke tall-typer vi opererer med
print(f"Division: {int_variable / operation_variable}")

# Divisjon med nedrunning
# Fungerer likt som vanlig divisjon, men runder alltid NED til nærmeste heltall og returnerer som int
print(f"Floor division: {int_variable // operation_variable}")

# Opphøyning - Ganger et tall med seg selv et antall ganger
# Operasjonen nedenfor er tilsvarende: int_variable * int_variable.
# Altså int_variable ganges med seg selv 2 ganger fordi operation_variable = 2
print(f"Exponentiation: {int_variable ** operation_variable}")

# Modulo (norsk)
# Gir resten etter heltallsdividering
print(f"Modulus: {int_variable % operation_variable}")


float_variable = 3.14

# Operasjon hvor vi benytter både int og float
# Merk at resultatet også blir float, siden en float-verdi er med i beregningen (uavhengig av den spesifikke verdien).
print(f"Operation with int and float: {int_variable + float_variable}")


# Bruk av assignment-operatorer
number = 0 # Setter number til å være lik 0
number = number + 1 # Oppdaterer number ved å ta den nåværende verdien (0) og plusse på 1
print(f"Number: {number}")
number += 1 # Samme resultat som number = number + 1
print(f"Number: {number}")
number *= 2 # Tilsvarer number = number * 2
print(f"Number: {number}")