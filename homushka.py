

print("Home Work 2.2")
print('-------------')

number_mirror = int(input("Enter a number from 10000 to 99999:"))

tuta, tama = divmod(number_mirror, 10)
tuta_2, tama_2 = divmod(tuta, 10)
tuta_3, tama_3 = divmod(tuta_2, 10)
tuta_4, tama_4 = divmod(tuta_3, 10)
tuta_5, tama_5 = divmod(tuta_4, 10)

print(tama * 10**4 + tama_2 * 10 ** 3 + tama_3 * 10 ** 2 + tama_4 * 10 ** 1 + tama_5 * 10 ** 0)
