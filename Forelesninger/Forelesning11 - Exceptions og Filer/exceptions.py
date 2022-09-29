# Kommentarer kommer
try:
    number_1 = int(input("Type in a whole number: "))
    number_2 = int(input("Type in another whole number: "))
    result = number_1 / number_2
except ValueError:
    print("You have to input a whole number!")
except ZeroDivisionError:
    print("You can't divide dy zero.")
else:
    print(f"{number_1} / {number_2} = {result}")

print("End of Program")