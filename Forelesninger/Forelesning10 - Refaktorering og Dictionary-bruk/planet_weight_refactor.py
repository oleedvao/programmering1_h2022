# Programmet har i dette eksemplet blitt refaktorert til å skille ut abstrakte handlinger i egne, "self contained"
# funksjoner.


planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15]


# Funksjon som henter vekt fra brukeren, kontrollerer den, og returnerer den.
def get_user_weight():
    user_weight = input("What is your weight on earth?: ")
    user_weight = float(user_weight)

    if user_weight <= 0:
        print("The weight must be a positive number.")
        exit()

    return user_weight


# Funksjon som skriver ut planetene brukeren kan kan velge fra.
# Funksjonen er definert til å være dynamisk basert på hvilken planet-liste vil sender med som
# parameter, ved funksjonskall
def print_planet_choices(planet_list):
    print("\n====Planets====")
    for index in range(len(planet_list)):
        print(f"{index + 1} - {planet_list[index]}")

# Funksjon som henter brukerens planetvalg (nummer på planet), kontrollerer det, og returnerer
# den tilsvarende indexen.
# Funksjonen er også definert til å være dynamisk basert på antall planeter (Tar dette som parameter).
def get_planet_choice_index(number_of_planets):
    planet_number = input("\nPick a planet by typing a number (int): ")
    planet_number = int(planet_number)

    if planet_number < 1 or planet_number > number_of_planets:
        print("The number you entered is outside of the accepted range.")
        exit()

    return planet_number - 1


# Funksjon som beregner og viser frem vekten på planeten.
# Funksjonen er definert til å være dynamisk basert på bruker-vekt, liste med tyngdekraft, liste med
# planeter, og indexen for den valge indexen.
def calculate_and_display_planet_weight(user_weight, gravity_list, planet_list, index):
    planet_weight = user_weight / gravity_list[2] * gravity_list[index]

    print(f"\nYour weight on {planet_list[index]} is: {planet_weight}")

# Funksjonen gir brukeren et valg om å avslutte programmet. Hvis brukeren svarer "yes", blir
# programmet avsluttet.
def user_quit_choice():
    quit = input("Do you want to quit?: ")

    if quit == "yes":
        exit()


while True:
    # Resultatet av å skille kodelinjene i funksjoner er at de overordnede handlingene i programmet
    # blir en god del tydeligere. Forsøk å lese linjene under. Ut ifra disse er det relativt enkelt
    # å forstå hva programmet gjør i overordnet forstand.

    # Vi henter her brukerens vekt.
    your_weight = get_user_weight()

    # Vi skriver ut planetene brukeren kan velge fra.
    # Her baserer vi oss på listen, planets, men vi kunne også basert oss på en annen liste med
    # planeter, simpelthen ved å sende med an annen liste som parameter.
    # Dette hadde da heller ikke krevd noen endring i selve funksjonsdefinisjonen.
    print_planet_choices(planets)

    # Vi henter her brukerens valgte planet og returnerer den i form av en index.
    # Internt til brukerens valg kontrollert og vi baserer denne kontrollen på antall planeter, som
    # vi sender med som paramter (ved bruk av len()-funkjonen)
    planet_index = get_planet_choice_index(len(planets))

    # Vi beregner og viser frem resultatet av planetvekt-utregningen.
    # Merk at dette også blir dynamisk beregnet basert på brukervekt, tyngdekrefter for forskjellige
    # planeter, de forskjellige planetnavnene, samt indexen for den valge planeten (blir benyttet)
    # i henhold til listene.
    calculate_and_display_planet_weight(your_weight, planets_gravity, planets, planet_index)

    # Vi gir til slutt brukeren et valg om han/hun vil avslutte programmet.
    user_quit_choice()