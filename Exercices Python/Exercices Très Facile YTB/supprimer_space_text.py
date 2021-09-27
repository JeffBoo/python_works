
def supprim_space(message):
    text_collage = ""
    list_message = message.split()
    for mot in list_message:
        text_collage += mot
    return text_collage

phrase = input("Insérez une phrase à espaces multiples : ")
print("La phrase collée est : ", supprim_space(phrase))