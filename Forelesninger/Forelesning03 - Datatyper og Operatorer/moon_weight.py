

# Henter en verdi som representer vekt på jorden fra bruker (når programmet kjøres)
# input() returnerer her alltid en string-verdi
my_earth_weight = input("Specify weight on earth: ")

# For at verdien hentet med input() skal tolkes som et tall, må vi konvertere fra tekst til enten int eller float.
# Dette forutsetter imidlertid at tekst-verdien vi forsøker å konverte er samsvarig med disse datatypene.
# Å konvertere til float er stort sett det sikreste, ettersom alle tall i tekstformat kan konverteres til float og
# det er alltid en mulighet for at brukeren ønsker å benytte float, noe int-konvertering ikke støtter.
my_earth_weight = float(my_earth_weight)

# Variabler for tyngdekraft på jorden og månen.
# Verdiene er målt i m/s^2.
earth_gravity = 9.807
moon_gravity = 1.622

# Formel for å beregne vekten på månen utifra vekten på jorden.
moon_weight = my_earth_weight / earth_gravity * moon_gravity

# Skriver ut resultatet av utregningen
print(f"My weight on the moon is {moon_weight} kg")