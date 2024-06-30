def prime_generator(end):
    number = int(end) + 1
    def innet():
        for result in range(2, number):
            k = 0
            for j in range(1, result + 1):
                if result % j == 0:
                    k += 1
            if k == 2:
                if result <= end:
                    yield result
    return innet()

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'

assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')





