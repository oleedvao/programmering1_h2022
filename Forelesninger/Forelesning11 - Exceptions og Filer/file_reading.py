# Kommentarer kommer
'''
file = open("zen_of_python.txt")
print(file.read())
file.close()

print(file.read())
'''

try:
    with open("text_files/zen_of_python.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found.")

print()
with open("text_files/zen_of_python.txt") as file:
    print(file.readlines())

print()
with open("text_files/zen_of_python.txt") as file:
    print(file.readline().rstrip())
    print(file.readline().rstrip())

