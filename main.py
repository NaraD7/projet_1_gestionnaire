import random
def menu():
    '''
    cette fonction gère et relie toutes les autres fonction, elle retourne une fonction selon le choix de l'utilisateur
    :return:
    '''
    d = {}
    while True:
        print("\n--- MENU TÂCHES ---\n"
              "1. Générer\n"
              "2. Analyser\n"
              "3. Ajouter compte\n"
              "4. Lister comptes\n"
              "5. Rechercher\n"
              "6. Statistiques\n"
              "7. Quitter")
        while True:
            try:
                choix = int(input("Votre choix : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide.")
        match choix:
            case 1 :
                mdp = generer_mdp()
                print(mdp)
            case 2:
                score = analyser_force(mdp)
                print(score)
            case 3:
                ajouter_compte(mdp,score,d)
            case 4:
                lister_compte(d)
            case 5:
                rechercher_compte()
            case 6:
                statistiques_compte()
            case 7:
                break



def generer_mdp():
    '''
    cette fonction a générer un mot de passe et va retourner le mot de passe créer
    :return:
    '''
    voyelle = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'u', 'U', 'y', 'Y']
    consonne = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'z', 'Z']
    speciaux = ['!', '@', '#', '$', '%', '&', '*', '?', '2', '3', '4', '5', '6', '7', '8', '9']

    mdp = ""
    longueur = random.randint(3,6)
    for i in range (0, longueur):
            caractere = random.choice(consonne)
            mdp += caractere
            caractere = random.choice(voyelle)
            mdp += caractere
            mdp += random.choice(speciaux)
    return mdp





def analyser_force() :
    '''
    cette fonction va analyser le mot de passe générer et va retourner un score de sécurité entre 0 et 100
    :return:
    '''
    score = 0
    longueur =len(mdp)
    if longueur >= 12:
        score += 25
    elif 12<longueur<15:
        score += 50
    elif 15<longueur<18:
        score += 75
    else:
        score += 100
    return score


def ajouter_compte():
    '''
    cette fonction va demander à l'utilisateur d'entrer un nom et une catégorie afin de sauvegarder
    le mot de passe avec le site qui correspond dans le fichier externe
    :return:
    '''
    nom_site = str(input("Entrez le nom du site : "))
    type_site = str(input("entrez le type du site (email, réseaux, banque, ..."))
    d[nom_site] = {
        "type": type_site,
        "mot de passe": mdp
    }
    print(d)



def lister_compte(d):
    '''
    cette fonction va afficher les comptes présent dans le fichier externe
    :return:
    '''
    print("--------------------------------------------")
    for cle, valeur in d.items():
        print(cle)
        for cle2 in valeur:
            print (cle2,":",valeur[cle2])
    print("--------------------------------------------")



def statistiques():
    '''
    cette fonction va afficher le score moyen de tous les mots de passe de l'utilisateur
    :return:
    '''


