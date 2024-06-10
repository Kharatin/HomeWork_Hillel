import string
import keyword

new_name = str(input("Enter your new name: "))
print()
for symbol in new_name:
    if new_name[0:2] == '__':
        print(False)
        print("Bad idea")
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
    elif new_name == '_':
        print(True)
        break

else:
    print(True)
    print(f'"{new_name}" is here! Welcome to \'FIGHT CLUB\'!!! ')