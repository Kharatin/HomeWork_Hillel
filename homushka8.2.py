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

