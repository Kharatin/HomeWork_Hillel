print("Home Work 2.1")
print('-------------')
# способ № 1
number = int(input("Enter a number from 1000 to 9999:"))
x = 100
left, right = divmod(number, x)
y = 10
left_l, left_r = divmod(left, y)
right_l, right_r = divmod(right, y)
print(left_l)
print(left_r)
print(right_l)
print(right_r)
# способ № 2

number_2 = int(input("Enter please a number from 1000 to 9999:"))
up, downn = divmod(number_2, 1000)
print(up)
up, down = divmod(number_2, 100)
up_t, down_t = divmod(up, 10)
print(down_t)
up_ti, down_ti = divmod(down, 10)
print(up_ti)
up, down = divmod(number_2, 10)
print(down)



