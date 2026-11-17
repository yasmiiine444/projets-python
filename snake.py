# snake avec pygame
# fleches pour bouger, R pour rejouer, Echap pour quitter
# ce que j'ai rajoute : ca accelere avec les pommes + record sauvegarde

import pygame
import random
import os

pygame.init()

largeur = 600
hauteur = 600
case = 20

noir = (20, 20, 20)
blanc = (240, 240, 240)
vert = (70, 200, 90)
vert_fonce = (40, 150, 60)
rouge = (220, 50, 50)

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")
horloge = pygame.time.Clock()
police = pygame.font.SysFont("arial", 24)
grosse_police = pygame.font.SysFont("arial", 48)


def lire_record():
    if os.path.exists("record_snake.txt") == False:
        return 0
    f = open("record_snake.txt", "r")
    r = int(f.read())
    f.close()
    return r


def sauver_record(r):
    f = open("record_snake.txt", "w")
    f.write(str(r))
    f.close()


def nouvelle_pomme(serpent):
    x = random.randint(0, largeur // case - 1) * case
    y = random.randint(0, hauteur // case - 1) * case
    # il ne faut pas qu'elle tombe sur le serpent
    while [x, y] in serpent:
        x = random.randint(0, largeur // case - 1) * case
        y = random.randint(0, hauteur // case - 1) * case
    return [x, y]


def dessiner(serpent, pomme, score, record):
    fenetre.fill(noir)
    pygame.draw.rect(fenetre, rouge, (pomme[0], pomme[1], case, case))

    for morceau in serpent:
        pygame.draw.rect(fenetre, vert, (morceau[0], morceau[1], case - 1, case - 1))
    # la tete un peu plus foncee
    pygame.draw.rect(fenetre, vert_fonce, (serpent[0][0], serpent[0][1], case - 1, case - 1))

    texte = police.render("Score : " + str(score) + "   Record : " + str(record), True, blanc)
    fenetre.blit(texte, (10, 10))


def ecran_perdu(score):
    texte = grosse_police.render("Perdu !", True, rouge)
    fenetre.blit(texte, (largeur // 2 - texte.get_width() // 2, 230))
    texte = police.render("Score : " + str(score), True, blanc)
    fenetre.blit(texte, (largeur // 2 - texte.get_width() // 2, 300))
    texte = police.render("R pour rejouer", True, blanc)
    fenetre.blit(texte, (largeur // 2 - texte.get_width() // 2, 335))


serpent = [[300, 300], [280, 300], [260, 300]]
dx = case
dy = 0
futur_dx = dx
futur_dy = dy
pomme = nouvelle_pomme(serpent)
score = 0
vitesse = 8
record = lire_record()
perdu = False
continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuer = False

            # on regarde dx et dy pour ne pas pouvoir faire demi-tour
            if event.key == pygame.K_UP and dy == 0:
                futur_dx = 0
                futur_dy = -case
            if event.key == pygame.K_DOWN and dy == 0:
                futur_dx = 0
                futur_dy = case
            if event.key == pygame.K_LEFT and dx == 0:
                futur_dx = -case
                futur_dy = 0
            if event.key == pygame.K_RIGHT and dx == 0:
                futur_dx = case
                futur_dy = 0

            if event.key == pygame.K_r and perdu == True:
                serpent = [[300, 300], [280, 300], [260, 300]]
                dx = case
                dy = 0
                futur_dx = dx
                futur_dy = dy
                pomme = nouvelle_pomme(serpent)
                score = 0
                vitesse = 8
                perdu = False

    if perdu == False:
        dx = futur_dx
        dy = futur_dy
        tete = [serpent[0][0] + dx, serpent[0][1] + dy]
        serpent.insert(0, tete)

        if tete == pomme:
            score = score + 1
            pomme = nouvelle_pomme(serpent)
            # toutes les 2 pommes ca va plus vite
            if score % 2 == 0 and vitesse < 20:
                vitesse = vitesse + 1
            if score > record:
                record = score
                sauver_record(record)
        else:
            serpent.pop()

        # les murs
        if tete[0] < 0 or tete[0] >= largeur or tete[1] < 0 or tete[1] >= hauteur:
            perdu = True
        # son propre corps
        if tete in serpent[1:]:
            perdu = True

    dessiner(serpent, pomme, score, record)
    if perdu == True:
        ecran_perdu(score)

    pygame.display.flip()
    horloge.tick(vitesse)

pygame.quit()
