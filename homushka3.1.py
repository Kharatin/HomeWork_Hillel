
number_one = float(input("Enter number one: "))
number_two = float(input("Enter number two: "))
action = input("Enter action(+,-,*,/): ")

if action == '+':
    summa = number_one + number_two
    print(summa)
elif action == '-':
    subtraction = number_one - number_two
    print(subtraction)
elif action == '*':
    multiplication = number_one * number_two
    print(multiplication)
elif action == '/':
    if number_two == 0:
        print("Upss, it is WRONG!!!!")
        print ("YOU CAN'T DIVIDE BY ZERO !!!")
        print("Try again.")
    else:
        division = number_one / number_two
        print(division)
else:
    print("Something goes wrong.\nDo it again, please.")
print("We're happy that we can help you.")