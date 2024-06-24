  # Способ № 1
def popular_words(text, words):
    simple_text = str(text.lower())
    text = simple_text.split()
    m = dict.fromkeys( words, 0 )
    for i in text:
        if i in words:
            m[i] = m.get(i, 0) + 1
    return m

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

  # Способ № 2

def popular_words (text, words):
    simple_text = str(text.lower())
    text = simple_text.split()
    m = dict.fromkeys( words, 0 )
    for i in text:
        if i in words:
            m.setdefault(i, 0)
            m[i] += 1
    return m

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')



text = '''When I was One I had just begun When I was Two I was nearly new '''
words = ['i', 'was', 'three', 'near']
print(popular_words(text, words))





