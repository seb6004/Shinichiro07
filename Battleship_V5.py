# First Version of Battleship
#test
import random

Coordonee_aleatoire_bat1_X= random.randint(1, 6)
Coordonee_aleatoire_bat1_Y= random.randint(1, 6)
Coordonee_aleatoire_bat2_X= random.randint(1, 6)
Coordonee_aleatoire_bat2_Y= random.randint(1, 6)
while Coordonee_aleatoire_bat1_X == Coordonee_aleatoire_bat2_X and Coordonee_aleatoire_bat1_Y == Coordonee_aleatoire_bat2_Y:
    Coordonee_aleatoire_bat1_X= random.randint(1, 6)
    Coordonee_aleatoire_bat1_Y= random.randint(1, 6)

Nb_essais= 0
coule= 0
etatbat1= 0
etatbat2= 0

print('A vous de jouer')

Nb_essais_demande= int(input("Combien d'essais voulez vous ?"))

while coule < 2 and Nb_essais < Nb_essais_demande:
    Coordonee_remplit_X= int(input('Quel est le nombre correspondant à la ligne ?'))
    Coordonee_remplit_Y= int(input('Quel est le nombre correspondant à la colonne ?'))
    Nb_essais= Nb_essais + 1
    if Coordonee_remplit_X == Coordonee_aleatoire_bat1_X and Coordonee_remplit_Y == Coordonee_aleatoire_bat1_Y and etatbat1== 0:
        print('Vous avez coulé le 1er bateau')
        coule= coule + 1
        etatbat1= 1
    elif Coordonee_remplit_X == Coordonee_aleatoire_bat2_X and Coordonee_remplit_Y == Coordonee_aleatoire_bat2_Y and etatbat2== 0:
        print('Vous avez coulé le 2eme bateau')
        coule= coule + 1
        etatbat2= 1
    elif Coordonee_remplit_X == Coordonee_aleatoire_bat1_X and etatbat1== 0 or (Coordonee_remplit_Y == Coordonee_aleatoire_bat1_Y and etatbat1== 0):
        if Coordonee_remplit_X == Coordonee_aleatoire_bat1_X and etatbat1== 0 or Coordonee_remplit_Y == Coordonee_aleatoire_bat1_Y and etatbat1== 0 and Coordonee_remplit_X == Coordonee_aleatoire_bat2_X and etatbat2== 0 or Coordonee_remplit_Y == Coordonee_aleatoire_bat2_Y and etatbat2== 0: 
            print('Les 2 bateaux sont en vue')
        else:
            print('Le 1er bateau est en vue')
    elif Coordonee_remplit_X == Coordonee_aleatoire_bat2_X and etatbat2== 0 or Coordonee_remplit_Y == Coordonee_aleatoire_bat2_Y and etatbat2== 0:
        print('Le 2eme bateau est en vue')
    else:
        print("Votre missile est tombé à l'eau")

if coule == 2:
    print("******************************")
    print("*                            *")
    print("* BRAVO ! Vous avez gagné !! *")
    print("*                            *")
    print("******************************")
else:
    print("GAME OVER")
