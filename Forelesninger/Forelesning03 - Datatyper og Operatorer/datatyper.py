
# Opprettelse av en int-variabel
int_variable = 42
print(int_variable)

# Opprettelse av en float variabel
# Merk at float verdier har tegnet . og desimaler
float_variable = 3.14
print(float_variable)

# Opprettelse av de to bool-verdiene
# Merk at både True og False må ha store forbokstaver for å være gyldige bool-verdier
bool_true = True
bool_false = False
print(bool_true)
print(bool_false)

# Opprettelse av en "tom" variabel.
# Merk at None må ha stor N for å være gyldig.
# Fører til en variabel uten verdi (i praksis), men har teknisk sett verdien None.
no_value = None
print(no_value)

# Eksempler på konverteringer mellom datatyper.
# Vær bevist på at konvertering til tall fra tekst, krever at innholdet av tekst-verdiene samsvarer med
# datatypen vi ønsker å konvertere til.
print(float(int_variable))
print(int(float_variable))
print(int("11"))
print(float("11.6"))
print(float("11"))
#print(int("fjdsklfj"))
print(int(bool_true))
print(int(bool_false))