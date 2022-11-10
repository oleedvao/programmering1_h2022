
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.name} serves {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"\n{self.name} is open! Welcome!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, inc_number_served):
        self.number_served += inc_number_served


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type="ice cream", flavours=[]):
        super().__init__(name, cuisine_type)
        self.flavours = flavours

    def show_flavours(self):
        print("\nWe have these flavours avalaible:")
        for flavour in self.flavours:
                print(f"- {flavour}")


if __name__ == "__main__":
    flurryflavour = IceCreamStand("flurry flavour", flavours=["vanilla", "chocolate", "pistachio", "lollipop"])
    flurryflavour.describe_restaurant()
    flurryflavour.show_flavours()


'''olivegarden = Restaurant("the olive garden", "italian")
print(olivegarden.number_served)
olivegarden.set_number_served(50)
print(olivegarden.number_served)
olivegarden.increment_number_served(50)
print(olivegarden.number_served)'''


'''print(olivegarden.name)
print(olivegarden.cuisine_type)
olivegarden.describe_restaurant()
olivegarden.open_restaurant()

mcd = Restaurant("mcdonalds", "junk food")
mcdnewyork = Restaurant("mcdonalds", "junk food")
mcdnewyork.name = "McDonalds NY"
mcd.describe_restaurant()
mcdnewyork.describe_restaurant()'''



