#Test saisie

#NB_saisie= int(input('Saisir un nombre compris entre 1 et 6'))

#while True:
#    if NB_saisie > 6 or NB_saisie < 0:
#        NB_saisie= int(input('Saisir un nombre compris entre 1 et 6'))
#    else:
#        break


#Devine mon nombre
#import random

#NB_aléatoire= random.randint(0, 100)
#print(NB_aléatoire)
#NB_choisi= int(input('Devine mon nombre'))
#WIN= False
#score= 1

#while WIN== False:
#    if NB_aléatoire == NB_choisi:
#        print('Bravo tu a gagné avec un score de', score, '!')
#        WIN= True
#    elif NB_aléatoire > NB_choisi:
#        print('Trop petit !')
#        NB_choisi= int(input('Devine mon nombre'))
#        score= score + 1
#    elif NB_aléatoire < NB_choisi:
#        print('Trop grand')
#        NB_choisi= int(input('Devine mon nombre'))
#        score= score + 1

#Jeu du lievre et de la tortue
import random

D= random.randint(1, 6)
print(D)
WIN= False
ts= 0

while WIN== False:
    if D == 6:
        print('Le lièvre a gagné')
        WIN= True
    elif ts== 6:
        print('La tortue a gagné')
        WIN= True
    elif D < 6:
        print('La tortue avance de 1')
        ts= ts + 1
        D= random.randint(1, 6)
        print(D)