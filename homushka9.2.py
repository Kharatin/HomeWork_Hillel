# ВАРИАНТ №1
print()
def difference(*arcs):
    if arcs == ():
        answer = 0
        return answer
    else:
        lst = list(arcs)
        lst.sort()
        answer = (lst[-1] - lst[0])
        return round(answer, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK'"\n")

# ВАРИАНТ №2

def difference(*arcs):
    if arcs == ():
        d = 0
        return d
    else:
        d = max(arcs) - min(arcs)
        return round(d, 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
