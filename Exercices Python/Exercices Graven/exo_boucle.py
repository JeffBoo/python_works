
emails = ["erode@ertdyt", "tryo@ert.com", "trz@frtv.fr", "retf@zat.cer"]
listblak = ["tryo@ert.com"]
for mail in emails:
    if mail in listblak:
        print("mail {} non valide".format(mail))
        continue

    print("La vida loka {}".format(mail))