# Lister for planetnavn og planetgravitasjoner. Disse blir brukt til utregninger lenger ned samt for å gi
# brukeren en oversikt over hvilke planeter som det kan velges fra.
# Verdiposisjonene i planets_gravity tilsvarer planetnavnene i planets. Det vil si at 2.7 -> Mercury, 8.87 -> Venus osv.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15]

# Henter brukerens vekt fra input og konverterer til float.
your_weight = input("What is your weight on earth?: ")
your_weight = float(your_weight)

# Sjekker om brukerens vekt er negativ. Dette er i så fall et unntakstilfelle og behandles ved å avslutte programmet.
if your_weight <= 0:
    print("The weight must be a positive number.")
    exit() # Avslutter programmet. Det vil si at videre kode ikke vil bli kjørt hvis denne funksjonen kalles.

# Skriver ut en oversikt til brukeren om hvilke planeter det kan velges fra. Disse representeres som et heltall
# Utskriftene baserer seg på planetnavnene i planets-listen
print("\n====Planets====")
print(f"1 - {planets[0]}")
print(f"2 - {planets[1]}")
print(f"3 - {planets[2]}")
print(f"4 - {planets[3]}")
print(f"5 - {planets[4]}")
print(f"6 - {planets[5]}")
print(f"7 - {planets[6]}")
print(f"8 - {planets[7]}")

# Henter brukerens valgte planet (heltall) fra input og konverterer det til int
planet_number = input("\nPick a planet by typing a number (int): ")
planet_number = int(planet_number)

# Sjekker om tallet brukeren ga er mindre enn 1 eller større en 8.
# Dette er i så fall et unntakstilfelle og håndteres essensielt likt som vi gjorde over med feil i angitt vekt.
if planet_number < 1 or planet_number > 8:
    print("The number you entered is outside of the accepted range.")
    exit() # Avslutter programmet.

# Konverterer planettallet brukeren ga til en index, slik at vi kan benytte denne til å dynamisk referere til
# den tilsvarende planeten og planetgravitasjonen i listene planets og planets_gravity
planet_index = planet_number - 1

# Beregner brukerens vekt på planeten som ble valgt. For dette benyttes planet_gravity-listen og indexer.
# jordvekt / jordtyngdekraft * planettyngdekraft
planet_weight = your_weight / planets_gravity[2] * planets_gravity[planet_index]

# Skriver ut resultatet av utregningen.
print(f"\nYour weight on {planets[planet_index]} is: {planet_weight}")
