# quiz anatomie / histologie
# pour reviser mes cours en meme temps que python
# pour ajouter une question il suffit de copier un bloc dans la liste

import random
import os

fichier_score = "meilleur_score.txt"

questions = [
    {"q": "Combien d'os a un adulte ?",
     "choix": ["a) 186", "b) 206", "c) 226", "d) 306"],
     "rep": "b"},
    {"q": "Quel est l'os le plus long du corps ?",
     "choix": ["a) L'humerus", "b) Le tibia", "c) Le femur", "d) Le perone"],
     "rep": "c"},
    {"q": "Combien y a-t-il de vertebres cervicales ?",
     "choix": ["a) 5", "b) 7", "c) 10", "d) 12"],
     "rep": "b"},
    {"q": "Quel os de l'avant-bras est du cote du pouce ?",
     "choix": ["a) Le radius", "b) L'ulna", "c) L'humerus", "d) Le scaphoide"],
     "rep": "a"},
    {"q": "Quel est le principal muscle de l'inspiration ?",
     "choix": ["a) Le grand pectoral", "b) Le trapeze", "c) Le grand dorsal", "d) Le diaphragme"],
     "rep": "d"},
    {"q": "Quel nerf innerve le diaphragme ?",
     "choix": ["a) Le nerf vague", "b) Le nerf phrenique", "c) Le nerf radial", "d) Le nerf facial"],
     "rep": "b"},
    {"q": "Dans quelle cavite arrivent les veines pulmonaires ?",
     "choix": ["a) Oreillette droite", "b) Ventricule droit", "c) Oreillette gauche", "d) Ventricule gauche"],
     "rep": "c"},
    {"q": "Quelle valve separe l'oreillette gauche du ventricule gauche ?",
     "choix": ["a) La tricuspide", "b) L'aortique", "c) La pulmonaire", "d) La mitrale"],
     "rep": "d"},
    {"q": "Quel est l'epithelium de l'epiderme ?",
     "choix": ["a) Pavimenteux stratifie keratinise", "b) Cylindrique simple", "c) Cubique simple", "d) Pseudostratifie cilie"],
     "rep": "a"},
    {"q": "Quel epithelium tapisse la vessie ?",
     "choix": ["a) Pavimenteux simple", "b) Urothelium", "c) Cylindrique simple", "d) Cubique stratifie"],
     "rep": "b"},
    {"q": "Quel epithelium tapisse la trachee ?",
     "choix": ["a) Pavimenteux stratifie", "b) Cubique simple", "c) Pseudostratifie cilie", "d) Urothelium"],
     "rep": "c"},
    {"q": "Comment s'appellent les cellules du cartilage ?",
     "choix": ["a) Osteocytes", "b) Adipocytes", "c) Fibroblastes", "d) Chondrocytes"],
     "rep": "d"},
    {"q": "Quelles cellules detruisent la matrice osseuse ?",
     "choix": ["a) Les osteoclastes", "b) Les osteoblastes", "c) Les osteocytes", "d) Les chondroblastes"],
     "rep": "a"},
    {"q": "Quelle cellule fabrique le collagene du tissu conjonctif ?",
     "choix": ["a) Le mastocyte", "b) Le fibroblaste", "c) Le macrophage", "d) Le plasmocyte"],
     "rep": "b"},
    {"q": "Avec la coloration HE, de quelle couleur sont les noyaux ?",
     "choix": ["a) Rose", "b) Vert", "c) Bleu-violet", "d) Jaune"],
     "rep": "c"},
    {"q": "Qui fabrique la myeline dans le systeme nerveux central ?",
     "choix": ["a) Les astrocytes", "b) Les cellules de Schwann", "c) La microglie", "d) Les oligodendrocytes"],
     "rep": "d"},
]


def poser_question(numero, question):
    print()
    print("Question", numero, ":", question["q"])
    for c in question["choix"]:
        print("  ", c)

    rep = input("Ta reponse : ").lower().strip()
    while rep not in ["a", "b", "c", "d"]:
        rep = input("a, b, c ou d : ").lower().strip()

    if rep == question["rep"]:
        print("Juste !")
        return 1

    print("Faux, c'etait la", question["rep"])
    return 0


def lire_score():
    if os.path.exists(fichier_score) == False:
        return 0
    f = open(fichier_score, "r")
    meilleur = int(f.read())
    f.close()
    return meilleur


def sauver_score(score):
    f = open(fichier_score, "w")
    f.write(str(score))
    f.close()


meilleur = lire_score()

print("--- Quiz anatomie / histologie ---")
print("Il y a", len(questions), "questions")
print("Meilleur score :", meilleur)

random.shuffle(questions)

score = 0
numero = 1
for question in questions:
    score = score + poser_question(numero, question)
    numero = numero + 1

print()
print("Fini ! Score :", score, "/", len(questions))

if score > meilleur:
    print("Nouveau record !")
    sauver_score(score)
else:
    print("Record a battre :", meilleur)
