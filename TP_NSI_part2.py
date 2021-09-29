#Jeu du lievre et de la tortue
import random

D= random.randint(1, 6)
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