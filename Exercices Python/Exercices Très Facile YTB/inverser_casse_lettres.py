
def inverse_case(texte):
    inverted_text = ""
    for char in texte:
        if char.isupper():
            char.lower()
            inverted_text += char
        elif char.islower():
            char.upper()
            inverted_text += char
        else:
            inverted_text += char

    return inverted_text

message = input("Entrez un message : ")
print("Le message en casse inversée est : ", inverse_case(message))
