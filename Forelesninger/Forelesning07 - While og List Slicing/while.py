# Variabel som while-løkken vil ta utganspunkt i
counter = 10

# En grunnleggende definisjon av en while løkke (som teller fra 10 til 1)
# Vi må definere en betingelse som definerer hvor lenge løkken skal kjøre.
# Konseptuelt vil denne bety "Så lenge <betingelsen>, kjør løkken om og om igjen".
while counter > 0:
    print(counter)
    # For at while-løkken skal slutte å kjøre må vi ha en exit-condition.
    # Her reduserer vi counter med 1 for hver gjennomkjøring av løkken slik at counter
    # før eller siden blir 0 og løkken slutter å kjøre
    counter -= 1