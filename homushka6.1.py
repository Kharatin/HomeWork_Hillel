import string
letters_line = str(input("Write letters with a hyphen: "))
print(letters_line)
all_leters = string.ascii_letters
x = all_leters.find(letters_line[0])
y = all_leters.find(letters_line[2])
print(all_leters[x:y+1])


print('-----------------------------------------------------------------')

letters_line = "a-c"
all_leters = string.ascii_letters
x = all_leters.find(letters_line[0])
y = all_leters.find(letters_line[2])
print(letters_line)
print( all_leters[x:y+1])


print('-----------------------------------------------------------------')

letters_line = "a-a"
all_leters = string.ascii_letters
x = all_leters.find(letters_line[0])
y = all_leters.find(letters_line[2])
print(letters_line)
print( all_leters[x:y+1])


print('-----------------------------------------------------------------')

letters_line = "s-H"
all_leters = string.ascii_letters
x = all_leters.find(letters_line[0])
y = all_leters.find(letters_line[2])
print(letters_line)
print( all_leters[x:y+1])


print('-----------------------------------------------------------------')

letters_line = "a-A"
all_leters = string.ascii_letters
x = all_leters.find(letters_line[0])
y = all_leters.find(letters_line[2])
print(letters_line)
print( all_leters[x:y+1])

print('-----------------------------------------------------------------')