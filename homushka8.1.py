def add_one(some_list):
    s_t_r ="".join([str(i) for i in some_list])
    i_n_t = int(s_t_r)
    i_n_t += 1
    new_s_t_r = str(i_n_t)
    new_some_list = []
    for i in new_s_t_r:
        new_some_list.append(int(i))
    return new_some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


print()
god = [2, 9, 9, 9, 9]
print(god)
my = add_one(god)
print(my)

print(':)')