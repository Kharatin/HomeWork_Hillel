def first_word(text):
    import  string
    n = len(text)
    text = text.replace(".", " ", n).replace(",", " ", n)
    text = text.lstrip()
    text = text.split()
    new_text = []
    for i in text:
        if not i[0]  in string.punctuation:
            new_text.append(i)
    return new_text[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')







































