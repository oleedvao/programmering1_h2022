
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_gravity = [3.7, 8.87, 9.807, 3.721, 24.79, 19.44, 8.87, 11.15]


# Hele programmsekvensen er inneholdt i en uendelig løkke.
# For at programmet skal avslutte må vi derfor ha en egen logikk inneholdt i løkken, som gjør dette manuelt.
while True:
    your_weight = input("What is your weight on earth?: ")
    your_weight = float(your_weight)

    if your_weight <= 0:
        print("The weight must be a positive number.")
        exit()

    # I stedet for å skrive uten individuell linje for hver planet i planetoversikten kan vi heller benytte
    # en for-løkke for å gjøre dette på ferre linjer og dynamisk basert på hvor mange planeter det er.
    print("\n====Planets====")
    for index in range(len(planets)):
        print(f"{index + 1} - {planets[index]}")

    planet_number = input("\nPick a planet by typing a number (int): ")
    planet_number = int(planet_number)

    if planet_number < 1 or planet_number > 8:
        print("The number you entered is outside of the accepted range.")
        exit()

    planet_index = planet_number - 1

    planet_weight = your_weight / planets_gravity[2] * planets_gravity[planet_index]

    print(f"\nYour weight on {planets[planet_index]} is: {planet_weight}")

    # På slutten av hver løkkeiterasjon (etter hver planetvekt-beregning) spør vi brukeren om han/hun vil avslutte.
    quit = input("Do you want to quit?: ")

    # Hvis brukeren ønsker å avslutte, benytter vi exit() for å stoppe hele programmet.
    # Underforstått: Hvis ikke, vil programmet kjøre på nytt i en ny løkkeiterasjon.
    if quit == "yes":
        exit()

