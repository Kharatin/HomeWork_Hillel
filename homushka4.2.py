my_bestlist = [0, 1, 7, 2, 4, 8]
i = 0
x = 0
listick = []

for number in my_bestlist:
    if not my_bestlist == []:
        if i % 2 == 0:
            listick.append(number)
            x = (sum(listick) * my_bestlist[-1])
    i += 1
print(x)


my_bestlist_2 = [1, 3, 5]
j = 0
y = 0
listick_2 = []

for number_2 in my_bestlist_2:
    if not [] == my_bestlist_2:
        if j % 2 == 0:
            listick_2.append(number_2)
            y = (sum(listick_2) * my_bestlist_2[-1])
    j += 1
print(y)


my_bestlist3 = [6]
q = 0
z = 0
listick3 = []

for number3 in my_bestlist3:
    if not my_bestlist3 == []:
        if q % 2 == 0:
            listick3.append(number3)
            z = (sum(listick3) * my_bestlist3[-1])
    q += 1
print(z)


my_bestlist4 = []
b = 0
w = 0
listick4 = []

for number4 in my_bestlist4:
    if not my_bestlist4 == []:
        if b % 2 == 0:
            listick.append(number4)
            w = (sum(listick4) * my_bestlist4[-1])
    b += 1
print(w)