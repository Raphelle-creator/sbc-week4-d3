text = input("Enter a sentence: ")
value = []

def words(text):
    sentence = ''
    for char in text:
        if char in '.!?':
            sentence += char
            value.append(sentence)
            sentence = ''
        else:
            if sentence or not char.isspace():
                sentence += char

    if sentence:
        value.append(sentence)

words(text)
print(value)
