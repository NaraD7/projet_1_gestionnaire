import random
def menu():
    '''
    cette fonction gère et relie toutes les autres fonction, elle retourne une fonction selon le choix de l'utilisateur
    :return:
    '''


def generer_mdp():
    '''
    cette fonction a générer un mot de passe et va retourner le mot de passe créer
    :return:
    '''
    voyelle = [97, 101, 105, 111, 117, 121]
    consonne = [98, 99, 100, 102, 103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 122]
    mdp = ""
    longueur = random.randint(8,64)
    for i in range (0, longueur):
        j = random.randint(1,3)
        if j == 1:
            l = random.choice(voyelle)
            l = chr(l)
            j = random.randint(1, 6000)
            if j % 2 == 0:
                l = l.upper()
            mdp += l
        if j == 2:
            l = random.choice(consonne)
            l = chr(l)
            j = random.randint(1, 6000)
            if j % 2 == 0:
                l = l.upper()
            mdp += l
        if j == 3:
            mdp += str(random.randint(0,9))
    return mdp


def analyser_force() :
    '''
    cette fonction va analyser le mot de passe générer et va retourner un score de sécurité entre 0 et 100
    :return:
    '''

def ajouter_compte():
    '''
    cette fonction va demander à l'utilisateur d'entrer un nom et une catégorie afin de sauvegarder
    le mot de passe avec le site qui correspond dans le fichier externe
    :return:
    '''

def lister_compte():
    '''
    cette fonction va afficher les comptes présent dans le fichier externe
    :return:
    '''

def statistiques():
    '''
    cette fonction va afficher le score moyen de tous les mots de passe de l'utilisateur
    :return:
    '''

def quitter():
    '''
    cette fonction va arrêter le programme
    :return:
    '''

menu()
print(generer_mdp())