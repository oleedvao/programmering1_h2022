# Definerer en klasse for å represenetere studenter og deres egenskaper
# Bruker nøkkelordet class og et selvalg klasse navn for å definere en klasse.
# Merk at klassenavn konvensjonellt skrives med stor forbokstav
class Student:
    # De fleste klasser krever av vi definerer en spesiell metode som heter __init__().
    # Denne metoden hjelper oss å opprette objekter (instanser av klassen), samt definere klassens instansvariabler.
    # Merk at denne metoden ligner en del på en vanlig funksjon, men må ha __init__ som navn og self, som første
    # parameter. Utover dette kan vi definere parameterene selv.
    # Parameteren definert etter self benyttes typisk til å ta imot verdier for klassens instansvariabler, tiltenkt,
    # spesifikke verdier for et gitt Student-objekt (en gitt student) sine "egenskaper".
    # I dette tilfellet tar parameteren imot verider for "egenskapene" - firstname, lastname, age og student_id
    def __init__(self, firstname, lastname, age, student_id):
        # Under definerer vi klassens instansvariabler.
        # Instansvariabler er variabler som alle objekter av klassen vil ha, men verdiene for disse vil være unike
        # for hvert objekt og settes via parameterene over når objektet blir opprettet.
        # For å opprette en instansvariabel skriver vi self.<variabelnavn>, og setter den til en verdi,
        # som typisk er basert på parameterene.
        # Konseptuelt det vi gjør for hver av variablene under er å spesifisere at "ethvert 'student' (self)
        # skal ha en 'egenskap' (variabel) og skal settes til å være det vi spesifiserer når dette objektet opprettes
        # (parameter).
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.student_id = student_id

    # Dette er en definisjon på en metode som kan benyttes for å få en tekstlig beskrivelse av en gitt student, altså
    # ett gitt Student-objekt
    # Slike metoder er praktisk talt det samme som funksjoner, men tilhører en klasse og må typisk ha self som første
    # parameter.
    def get_description(self):
        # Når vi kaller denne metoden vil vi returnere en tekststreng som gir en beskrivelse basert på
        # "egentkapsverdiene" (instansvariabel-verdiene) til studenten (Student-objektet) metoden kalles gjennom.
        return f"The students name is {self.firstname} {self.lastname}, is {self.age} years old with student id" \
               f" {self.student_id}"
