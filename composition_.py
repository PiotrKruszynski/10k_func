def create_sentence(fn, text):
    return fn(text)

def capitalize(text):
    return text.upper()

def lower(text):
    return text.lower()


# ternary operator
# True if condition else False

# duża mała na zmianę
def mocking_caps(text):
    text_list = list(text)
    for i in range(len(text_list)):
        if i % 2 == 0:
            text_list[i] = text_list[i].upper()
        else:
            text_list[i] = text_list[i].lower()
    return ''.join(text_list)

def mocking_caps2(text):
        return ''.join(letter.lower() if index % 2 else letter.upper() for index, letter in enumerate(text))


sentence = "ala ma kota"
r1 = create_sentence(capitalize, sentence)
r2 = create_sentence(lower, sentence)
r3 = create_sentence(mocking_caps, sentence)
r4 = create_sentence(mocking_caps2, sentence)

print(r1,r2,r3,r4, sep="\n")
