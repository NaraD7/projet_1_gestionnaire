import random
import json

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
                print(ajouter_compte(mdp,score,d))
            case 4:
                lister_compte()
            case 5:
                rechercher_compte()
            case 6:
                statistiques_compte()
            case 7:
                break



def generer_mdp():
    '''
    cette fonction va générer un mot de passe et va retourner le mot de passe créer, si le mot de passe ne convient pas à l'utilisateur il va proposer de le modifier manuellement
    :paramètres : None
    :return:
    '''
    voyelle = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'u', 'U', 'y', 'Y']
    consonne = ['b', 'B', 'c', 'C', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'v', 'V', 'w', 'W', 'x', 'X', 'z', 'Z']
    speciaux = ['!', '@', '#', '$', '%', '&', '*', '?', '2', '3', '4', '5', '6', '7', '8', '9']

    mdp = ""
    longueur = random.randint(3,11)
    for i in range (0, longueur):               # Cette boucle va choisir une voyelle une consonne et un caractère spécial et l'ajouter au mot de passe généré
            caractere = random.choice(consonne)
            mdp += caractere
            caractere = random.choice(voyelle)
            mdp += caractere
            mdp += random.choice(speciaux)
    print(f"Mot de passe généré : {mdp}")
    mdp = modifier_mdp(mdp)
    return mdp





def modifier_mdp(mdp):
    '''
    cette fonction va proposer à l'utilisateur de modifier son mot de passe manuellement afin de le personnaliser
    :param: mot de passe
    :return: mot de passe modifié
    '''
    while True:
        try :
            changement = int(input("voulez vous changer le mot de passe ? 1 : Oui,  2 : Non   : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        if changement == 1:
            while True:
                try:
                    nouveau_mdp = input("Entrez le nouveau mot de passe : ")
                    if len(nouveau_mdp) < 8:
                        raise ValueError("Mot de passe trop court")

                    if nouveau_mdp == mdp:
                        raise ValueError("Le mot de passe doit être différent de l'ancien")

                    return nouveau_mdp
                except ValueError as e:
                    print(e)
        elif changement == 2:
            return mdp
        elif changement != 1 and changement != 2 :
            print("Veuillez entrer un nombre valide.")



def analyser_force(mdp) :
    '''
    cette fonction va analyser le mot de passe générer et va retourner un score de sécurité entre 0 et 100
    :paramètres : mot de passe
    :return:
    '''
    score = 0
    speciaux = ['!', '@', '#', '$', '%', '&', '*', '?', '2', '3', '4', '5', '6', '7', '8', '9']
    nombre, majuscule, minuscule , special = False, False, False, False
    for i in mdp :
        if i.isdigit() and nombre == False:
            nombre = True
            score += 10
        elif i.isupper() and majuscule == False:
            majuscule = True
            score += 15
        elif i.islower() and minuscule == False:
            minuscule = True
            score += 15
        elif i in speciaux and special == False:
            special = True
            score += 20
    if len(mdp) < 8:
        score += 0
    elif 8<=len(mdp)<=9:
        score += 10
    elif 10<=len(mdp)<=11:
        score += 20
    elif 12<=len(mdp)<=15:
        score += 30
    else:
        score += 40
    return score

def ajouter_compte(mdp, score, d):
    '''
    cette fonction va demander à l'utilisateur d'entrer un nom et une catégorie afin de sauvegarder
    le mot de passe avec le site qui correspond dans le fichier externe
    paramètres : mot de passe généré, score , dictionnaire "d" pour sauvegarder les infos
    :return:
    '''
    nom_site = str(input("Entrez le nom du site : "))
    type_site = str(input("entrez le type du site (email, réseaux, banque, ..."))
    d[nom_site] = {
        "type": type_site,
        "mot de passe": mdp,
        "score" : score,
    }
    sauvegarder(d)
    print(d)

def sauvegarder(d):
    with open("sauvegarde_compte.json", "w", encoding="utf-8") as fichier:
        json.dump(d, fichier,indent = 2)


def lister_compte():
    '''
    cette fonction va afficher les comptes présent dans le fichier externe
    paramètres : None
    :return:
    '''

    with open("sauvegarde_compte.json", "r", encoding="utf-8") as fichier:
        compte = json.load(fichier)
        for cle, valeur in compte.items():
            print("___________________________")
            print(cle)
            for cle2 in valeur:
                print (cle2, ": ", valeur[cle2])
    print("___________________________")



def statistiques():
    '''
    cette fonction va afficher le score moyen de tous les mots de passe de l'utilisateur
    :return:
    '''
    moyenne = 0
    with open("sauvegarde_compte.json", "r", encoding="utf-8") as fichier:
        compte = json.load(fichier)
        for cle, valeur in compte.items():
            moyenne += valeur["score"]
    moyenne = moyenne / len(compte)
    print(f"La moyenne des scores des mots de passe est de {moyenne}")
    return moyenne


print(menu())
