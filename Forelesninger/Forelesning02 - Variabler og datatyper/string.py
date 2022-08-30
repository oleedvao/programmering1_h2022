# String kan defineres med enten " eller '
print("A string")
print('Another string')

# Hvis vi ønsker å inkludere " eller ' i teksten har vi følgende valg
print('Quote: "First, solve the problem. Then write the code." - John Johnson')
print("Apostrophe: It's harder to read code than to write it")
print('''Both: "It's harder to read code than to write it" - Joel Spolsky''')


quote = "It's harder to read code than to write it"
author = "Joel Spolsky"
print('A quote: "<sitat>" - <forfatter>') # Tiltenkt format
print(f'A quote: "{quote}" - {author}') # Formaterer tekst til å benytte variabler

#Alternativ måte å formatere utskrift. Dette funker ikke for tekst alene
print('A quote: "', quote, '" - ', author)

