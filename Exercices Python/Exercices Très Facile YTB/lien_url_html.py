
def url_to_html(text_url, message):
    lien = "<a href = " + text_url + "> " + message + "</a>"
    htmlFile = open("PageTest.html","w")
    htmlFile.write(lien)
    htmlFile.close()


url = input("Entrez l'adresse url : ")
commentaire = input("Insérez le commentaire de lien : ")
url_to_html(url, commentaire)