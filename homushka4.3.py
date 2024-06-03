import random

my_list = [random.randint(1, 9) for i in range(random.randint(3,10))]
print(my_list)
print("len list: ", len(my_list))
new_list = []
new_list.append(my_list[0])
new_list.append(my_list[2])
new_list.append(my_list[-2])
print(new_list)


