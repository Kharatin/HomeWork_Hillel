import string
import keyword

new_name = str(input("Enter your new name: "))
print()
for symbol in new_name:
    if new_name == '_':
        print(True)
        print("OK! Short and locanically!")
        print(f'"{new_name}" is here! Welcome to \'FIGHT CLUB\'!!! ')
        break
    elif new_name == '__' or new_name == '___':
        print(False)
        print("It's impossible, I'm very sorry.")
        break
    elif new_name[0] in string.digits:
        print(False)
        print("The name does not start with a digit.")
        break
    elif new_name in keyword.kwlist:
        print(False)
        print("This name is reserved. Try something else.")
        break
    elif symbol in string.punctuation:
        if symbol == "_":
            continue
        else:
            print(False)
            print("Only digits and letters.")
            break
    elif new_name.islower() == False:
        print(False)
        print("Only small latters")
        break
    elif symbol == ' ':
        print(False)
        print("Space is not acceptable.")
        break

else:
    print(True)
    print(f'"{new_name}" is here! Welcome to \'FIGHT CLUB\'!!! ')

