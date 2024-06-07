import string

str_1 = 'Python Community'
print(str_1)
str_1 = str_1.title()
lst = str_1.split()
str_1 = "".join(lst)
g = ""
for i in str_1:
    if not i in string.punctuation:
        g += i
y = '#%.139s'%(g)
print(y)
print('Len:', len(y), 'from 140' )


print('----------------------------------------')


str_2 = 'i like python community!'
print(str_2)
str_2 = str_2.title()
lst = str_2.split()
str_2 = "".join(lst)
g = ""
for i in str_2:
    if not i in string.punctuation:
        g += i
y = '#%.139s'%(g)
print(y)
print('Len:', len(y), 'from 140' )

print('----------------------------------------')


str_3 = 'Should, I. subscribe? Yes!'
print(str_3)
str_3 = str_3.title()
lst = str_3.split()
str_3 = "".join(lst)
g = ""
for i in str_3:
    if not i in string.punctuation:
        g += i
y = '#%.139s'%(g)
print(y)
print('Len:', len(y), 'from 140' )
print('----------------------------------------')


str_4 = str(input("Enter everything what you want and you'll have hashtag: "))
print(str_4)
str_4 = str_4.title()
lst = str_4.split()
str_4 = "".join(lst)
g = ""
for i in str_4:
    if not i in string.punctuation:
        g += i
y = '#%.139s'%(g)
print(y)
print('Len:', len(y), 'from 140' )
