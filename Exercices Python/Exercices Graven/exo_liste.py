from statistics import mean
import statistics
from random import shuffle

online_players = ["Banana", "Job", "Pancake"]
print(online_players)

online_players[0] = "APris"
print(online_players)

del online_players[0]
print(online_players)

online_players.remove("Pancake")
print(online_players)

online_players.append("Tofita")
print(online_players)

online_players.extend("Pistache")
print(online_players)

online_players.extend(["Pistache", "Banofee"])
print(online_players)

online_players.pop()
print(online_players)

online_players.pop(1)
print(online_players)

online_players[1:] = ["Pistache", "Water", "Tofifee"]
print(online_players)

online_players.clear()
print(online_players)

# travail sur le module statistics

notes = [
    14, 8, 11,
    17, 9, 7,
]

resultat = mean(notes)
print("La moyenne de l'eleve est {}".format(resultat))

moy_har = statistics.harmonic_mean(notes)
print("La moyenne harmonique est {}".format(moy_har))

# travail sur le module random

print(notes)
shuffle(notes)
print(notes)

# liste à partir d'un input

entree_donnee = input("Donnez dans l'ordre mail-pseudo-mdp : ")
liste_donnee = entree_donnee.split("-")
print("Bonjour {}, voici ton mail {}, et ton mdp {}".format(liste_donnee[1], liste_donnee[0], liste_donnee[2]))