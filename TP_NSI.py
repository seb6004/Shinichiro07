Test saisie

NB_saisie= int(input('Saisir un nombre compris entre 1 et 6'))

while True:
    if NB_saisie > 6 or NB_saisie < 0:
        NB_saisie= int(input('Saisir un nombre compris entre 1 et 6'))
    else:
        break
