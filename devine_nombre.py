# jeu du nombre mystere
# l'ordi choisit un nombre et il faut le trouver

import random

nombre = random.randint(1, 100)
essais = 7
trouve = False

print("--- Nombre mystere ---")
print("J'ai choisi un nombre entre 1 et 100.")
print("Tu as", essais, "essais.")
print()

while essais > 0 and trouve == False:
    rep = input("Ton nombre : ")

    # si on tape des lettres ca plantait avec int()
    if rep.isdigit() == False:
        print("Ecris un nombre stp")
        continue

    rep = int(rep)

    if rep < 1 or rep > 100:
        print("Entre 1 et 100 !")
        continue

    essais = essais - 1

    if rep == nombre:
        trouve = True
    elif rep < nombre:
        print("Plus grand")
        print("Il te reste", essais, "essais")
    else:
        print("Plus petit")
        print("Il te reste", essais, "essais")

print()
if trouve == True:
    print("Bravo ! C'etait bien", nombre)
    print("Il te restait", essais, "essais")
else:
    print("Perdu... le nombre etait", nombre)
