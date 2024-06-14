num = str(input("Enter number: "))
x = 1
while len(num) > 1:
    x = 1
    for i in num:
        x *= int(i)
        num = str(x)
print(num)