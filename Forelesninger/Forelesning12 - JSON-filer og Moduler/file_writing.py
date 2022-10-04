# Hvis vi ønsker å skrive til en fil kan vi stort sett benytt with-blokker som vanlig, men vi må i så fall
# spesifisere at vi ønsker å skrive til filen i åpnings-logikken. Dette gjør vi ved å sende en ekstra parameter.
# For denne parameteren har vi noen forskjellige valg. Hvis vi benytter "w" sier vi at vi skal overskrive alt innhold
# i filen. Hvis vi benytter "a" vil vi legge på innhold utover det som filen inneholder fra før av.
# Merk også at vi her egentlig burde benyttet try/except-blokker for å håndtere eventuelle feil, slik som
# FileNotFoundError.
with open("text_files/my_novel.txt", "a") as file:
    while True:
        # Vi tar her en input fra brukeren.
        user_input = input(": ")
        # Hvis brukereren skriver "q", bryter vi løkken og stopper skrivingen.
        if user_input == "q":
            break
        # Vi skriver inputen til fil.
        file.write(user_input + "\n")
