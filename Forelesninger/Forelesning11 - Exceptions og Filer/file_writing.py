# Hvis vi ønsker å skrive til en fil kan vi stort sett benytt with-blokker som vanlig, men vi må i så fall
# spesifisere at vi ønsker å skrive til filen i åpnings-logikken. Dette gjør vi ved å sende en ekstra parameter.
# For denne parameteren har vi noen forskjellige valg. Hvis vi benytter "w" sier vi at vi skal overskrive alt innhold
# i filen. Hvis vi benytter "a" vil vi legge på innhold utover det som filen inneholder fra før av.
with open("text_files/my_novel.txt", "w") as file:
    # Vi tar her en input fra brukeren og skriver den til filen.
    user_input = input(": ")
    file.write(user_input)

# Dette eksemplet blir fortsatt og fullført i forelesning 12.