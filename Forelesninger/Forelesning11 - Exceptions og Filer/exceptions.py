# I enkelte tilfeller kan koden vår føre til såkalte exceptions, som typisk sette krasjer programmet vårt.
# For å håndtere slike tilfeller og forhindre at programmet krasjer, kan vi benytte try/except-blokker
# I try-blokken spesifiserer vi de kodelinjene vi vet kan feile (ofte slik som input, filhåndtering o.l.).
# Merk at vi helst bare bør spesifisere kode som KAN føre til exceptions i try-blokker. Altså skal vi sjeldent definere
# all kode i større programmer i en try-blokk. Bare de stedene hvor det er linjer som kan føre til exceptions.
# Vi kan lage en exception-blokk for hver type exception vi ønsker å håndtere. Hvis en gitt exception forekommer,
# kjører vi koden definert i exception blokker for denne exception-en og koden vil deretter forsette som normalt.
try:
    # Vi forsøker her å konvertere resultatet av to bruker-inputs til int-verdier.
    # Hvis verdiene vi får fra brukeren ikke er mulig å konvertere til int, vil vi får en ValueError, og programmet
    # # vil krasje.
    number_1 = int(input("Type in a whole number: "))
    number_2 = int(input("Type in another whole number: "))
    # Her deler vi to tall med hverandre. Dette går stort sett bra, men hvis vi forsøker å dele ett tall på 0 vil
    # dette føre til at vi får en ZeroDivisionError
    result = number_1 / number_2
except ValueError:
    # Hvis det forekommer en ValueError, skriver vi her ut en passende melding.
    print("You have to input a whole number!")
except ZeroDivisionError:
    # Hvis det forekommer en ZeroDivisionError, skriver ut en passende melding for det.
    print("You can't divide dy zero.")
else:
    # Hvis ingen exceptions forekommer, vil else-blokken kjøre og (i dette tilfellet) skrive ut resultatet av
    # utregningen, som er avhengig av kodelinjene i try-blokken
    print(f"{number_1} / {number_2} = {result}")

# Denne kodelinjen demonstrer ved kjøring at programet ikke vil krasje, selv om det forekommer en av exception-ene over.
print("End of Program")