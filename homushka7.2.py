def correct_sentence(text):
    if "," in text:
        if text[-1] != ".":
            x = "."
            text = text.replace(text[0], text[0].upper(), 1)
            text = text + x
            return str(text)
        else:
            text = text.replace(text[0], text[0].upper(), 1)
            return text

    elif text[-1] != ".":
        x = "."
        text = text.title()
        text = text + x
        return text
    else:
        text = text.title()
        return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
