import random
def menu():
    '''
    cette fonction gère et relie toutes les autres fonction, elle retourne une fonction selon le choix de l'utilisateur
    :paramètres : None
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
    :paramètres : None
    :return:
    '''
    voyelle = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'u', 'U', 'y', 'Y']
    consonne = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'z', 'Z']
    speciaux = ['!', '@', '#', '$', '%', '&', '*', '?', '2', '3', '4', '5', '6', '7', '8', '9']

    mdp = ""
    longueur_mdp = random.randint(3,6)
    for i in range (0, longueur_mdp):               # cette boucle va choisir une consonne, une voyelle et un caractère spécial afin de construire le mot de passe 
            caractere = random.choice(consonne)
            mdp += caractere
            caractere = random.choice(voyelle)
            mdp += caractere
            mdp += random.choice(speciaux)
    return mdp





def analyser_force(mdp) :
    '''
    cette fonction va analyser le mot de passe générer et va retourner un score de sécurité entre 0 et 100
    paramètres : mot de passe
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


def ajouter_compte(mdp, dictionnaire_sauvegarde):
    '''
    cette fonction va demander à l'utilisateur d'entrer un nom et une catégorie afin de sauvegarder
    le mot de passe avec le site qui correspond dans le fichier externe
    paramètres : mot de passe généré, score , dictionnaire "d" pour sauvegarder les infos
    :return:
    '''
    nom_site, type_site = "", ""        # initialisation de nom_site et type_site 
    while len(nom_site) == 0:           # tant que nom_site est vide on demande à l'utilisateur d'entrer le nom du site 
        nom_site = str(input("Entrez le nom du site : "))
    while len(nom_site) == 0:           # tant que nom_site est vide on demande à l'utilisateur d'entrer le type du site
        type_site = str(input("entrez le type du site (email, réseaux, banque, ..."))
    dictionnaire_sauvegarde[nom_site] = {       # mise à jour du dictionnaire de sauvegarde avec les infos entrées 
        "type": type_site,
        "mot de passe": mdp
    }
    print(dictionnaire_sauvegarde)       # print de debogage 

def sauvegarder(dictionnaire_sauvegarde):
    with open("sauvegarder_compte.json","w", encoding="utf-8") as compte_ecriture:      # cette ligne ouvre le fichier de sauvegarde json ("w") et y sauvegarde les sites sauvegardés par l'utilisateur 
        json.dump(dictionnaire_sauvegarde, compte_ecriture, indent = 2)

def lister_compte(dictionnaire_sauvegarde):
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


