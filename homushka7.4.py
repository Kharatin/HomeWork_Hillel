def common_elements():
    list_1 = set(range(0, 100, 3))
    list_2 = set(range(0, 100, 5))
    listik = list_1.intersection(list_2)
    print(listik)
    return listik


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('KARASAV4IK !!!')

print('----------------------------')
good = common_elements()
