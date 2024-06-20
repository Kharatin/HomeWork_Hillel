def is_palindrome(text):
    small_text = text.lower()
    only_letters = small_text.replace(",", "").replace(":", '').replace(" ", '').replace(".", '').replace("!", '')

    reverse_text = only_letters[::-1]
    return only_letters == reverse_text




assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

print()

def is_palindrome(text):
    import string

    small_text = text.lower()
    my_list = []
    for i in small_text:
        if i not in string.punctuation and i != " ":
            my_list.append(i)

    reverse_text = my_list[::-1]
    return my_list == reverse_text

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

assert is_palindrome('arora') == True, 'Test5'
assert is_palindrome('Arora!') == True, 'Test6'
assert is_palindrome('!ar ora#') == True, 'Test7'
assert is_palindrome('#OP@PO.') == True, 'Test8'
print("ОК")