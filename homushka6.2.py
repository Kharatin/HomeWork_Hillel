d = int(input("ENTER: "))

days_1 = [1, 21, 31, 41, 51, 61, 71, 81, 91]
days_2 = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
day_3 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 55]
day_4 = [56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99]

if d < 60:
    x, y = divmod(d, 1)
    print("0 дней", f'00:00:{str(x).zfill(2)}')

elif d < 3600:
    x, y = divmod(d, 60)
    print("0 дней", '00:%.2d:%.2d' % (x, y))

elif d < 86400:
    x, y = divmod(d, 3600)
    z = 0
    if y >= 60:
        a, b = divmod(y, 60)
        print("0 дней", '%.2d:%.2d:%.2d' % (x, a, b))
    else:
        print("0 дней", '%.2d:%.2d:%.2d' % (x, z, y))

elif d < 8640000:
    x, y = divmod(d, 86400)
    x2, y2 = divmod(y, 60)
    if x2 >= 60:
        x3, y3 = divmod(x2, 60)
        x2, y2 = divmod(y, 60)
        if int(x) in days_1:
            print(f"{x} день, {str(x3).zfill(2)}:{str(y3).zfill(2)}:{str(y2).zfill(2)}")
        elif int(x) in days_2:
            print(f"{x} дня, {str(x3).zfill(2)}:{str(y3).zfill(2)}:{str(y2).zfill(2)}")
        elif int(x) in day_3 or int(x) in day_4:
            print(f"{x} дней, {str(x3).zfill(2)}:{str(y3).zfill(2)}:{str(y2).zfill(2)}")

    elif y >= 60:
        x2, y2 = divmod(y, 60)
        if int(x) in days_1:
            print(f"{x} день, {str(0).zfill(2)}:{str(x2).zfill(2)}:{str(y2).zfill(2)}")
        elif int(x) in days_2:
            print(f"{x} дня, {str(0).zfill(2)}:{str(x2).zfill(2)}:{str(y2).zfill(2)}")
        elif int(x) in day_3 or int(x) in day_4:
            print(f"{x} дней, {str(0).zfill(2)}:{str(x2).zfill(2)}:{str(y2).zfill(2)}")

    else:
        if int(x) in days_1:
            print(f"{x} день, {str(0).zfill(2)}:{str(0).zfill(2)}:{str(y).zfill(2)}")
        elif int(x) in days_2:
            print(f"{x} дня, {str(0).zfill(2)}:{str(0).zfill(2)}:{str(y).zfill(2)}")
        elif int(x) in day_3 or int(x) in day_4:
            print(f"{x} дней, {str(0).zfill(2)}:{str(0).zfill(2)}:{str(y).zfill(2)}")

elif d == 8640000:
    print("100 дней! ")

else:
    print("!!!! БОЛЕЕ  100  дней !!!! ")
