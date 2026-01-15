import random
def menu():
    '''
    cette fonction gère et relie toutes les autres fonction, elle retourne une fonction selon le choix de l'utilisateur
    :return:
    '''
    while True:
        print("\n--- MENU TÂCHES ---")
        print("1. Générer")
        print("2. Analyser")
        print("3. Ajouter compte")
        print("4. Lister comptes")
        print("5. Rechercher")
        print("6. Statistiques")
        print("7. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            return generer_mdp()
        elif choix == "2":
            return analyser_force()
        elif choix == "3":
            return ajouter_compte()
        elif choix == "4":
            return lister_compte()
        elif choix == "5":
            return rechercher()
        elif choix == "6":
            return statistiques()
        elif choix == "7":
            return quitter()


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
        type = random.randint(1,3)
        if type == 1:
            caractere = random.choice(voyelle)
            caractere = chr(caractere)
            choix_maj = random.randint(1, 6000)
            if choix_maj % 2 == 0:
                caractere = caractere.upper()
            mdp += caractere
        if type == 2:
            caractere = random.choice(consonne)
            caractere = chr(caractere)
            choix_maj = random.randint(1, 6000)
            if choix_maj % 2 == 0:
                caractere = caractere.upper()
            mdp += caractere
        if type == 3:
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




def rechercher():
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

