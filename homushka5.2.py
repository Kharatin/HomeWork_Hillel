answer = 'yes'

while answer == 'yes' or answer == 'y':
    print('---------------------------')
    number_one = int(input("Number one: "))
    action = input("(+,-,*,/): ")
    number_two = int(input("Number two: "))
    if action == '+':
        summa = number_one + number_two
        print('RESULT:', summa)

    elif action == '-':
        subtraction = number_one - number_two
        print('RESULT:', subtraction)

    elif action == '*':
        multiplication = number_one * number_two
        print('RESULT:', multiplication)

    elif action == '/':
        if number_two == 0:
            print("WRONG!!!!")
            print("YOU CAN'T DIVIDE BY ZERO !!!")

        else:
            division = number_one / number_two
            print('RESULT:', '%.1f' % (division))

    else:
        print("Something goes wrong.")
    answer = input("Continue 'yes(y)' or ... ")
print('\nBye Bye!')
print("\t\tSee You Soon!")
