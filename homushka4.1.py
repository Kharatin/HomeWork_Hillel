first_list = [0, 1, 0, 12, 3]
my_list = [0, 1, 0, 12, 3]
for i, el in enumerate(my_list):
    if el == 0:
        my_list.remove(0)
        my_list.append(0)
print(first_list, ' -> ', my_list)


first_list_2 = [0]
my_list2 = [0]
for i, el in enumerate(my_list2):
    if el == 0:
        my_list2.remove(0)
        my_list2.append(0)
print(first_list_2, ' -> ', my_list2)


first_list_3 = [1, 0, 13, 0, 0, 0, 5]
my_list3 = [1, 0, 13, 0, 0, 0, 5]
for i, el in enumerate(my_list3):
    if el == 0:
        my_list3.remove(0)
        my_list3.append(0)
print(first_list_3, ' -> ', my_list3)


first_list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
my_list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
for i, el in enumerate(my_list4):
    if el == 0:
        my_list4.remove(0)
        my_list4.append(0)
print(first_list_4, ' -> ', my_list4)
