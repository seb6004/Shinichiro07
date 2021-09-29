#Devine mon nombre
import random

NB_aléatoire= random.randint(0, 100)
NB_choisi= int(input('Devine mon nombre'))
WIN= False
score= 1

while WIN== False:
    if NB_aléatoire == NB_choisi:
        print('Bravo tu a gagné avec un score de', score, '!')
        WIN= True
    elif NB_aléatoire > NB_choisi:
        print('Trop petit !')
        NB_choisi= int(input('Devine mon nombre'))
        score= score + 1
    elif NB_aléatoire < NB_choisi:
        print('Trop grand')
        NB_choisi= int(input('Devine mon nombre'))
        score= score + 1
