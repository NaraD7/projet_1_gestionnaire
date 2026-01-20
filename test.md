# Fiche de test du gestionnaire de mot de passe

## Test  : Menu()
#### Résultat obtenu :
C:\Users\Lilian\PycharmProjects\PythonProject2\.venv\Scripts\python.exe "C:\Users\Lilian\Downloads\projet_1_gestionnaire-main (1)\projet_1_gestionnaire-main\main.py" 

--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter
   
Votre choix :

## Test : generer_mdp()
#### Résultat obtenu :

C:\Users\Lilian\PycharmProjects\PythonProject2\.venv\Scripts\python.exe "C:\Users\Lilian\Downloads\projet_1_gestionnaire-main (1)\projet_1_gestionnaire-main\main.py" 

pY6ZE2kU3

voulez vous changer le mot de passe ? 1 : Oui,  2 : Non   : 1

entrez le nouveau mot de passe : Exemple.59300

## Test : analyser_mdp()
#### Résultat obtenu :
--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter
   
Votre choix : 2

90

## Test : ajouter_compte()
#### Résultat obtenu :
``--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter
   
Votre choix : 3

Entrez le nom du site : Twitch

entrez le type du site (email, réseaux, banque, ...) : divertissement

{'Twitch': {'type': 'divertissement', 'mot de passe': 'Exemple.59300', 'score': 90}}

None

## Test : lister_compte()
#### Résultat obtenu :

--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter

Votre choix :

Veuillez entrer un nombre valide.

Votre choix : 4

___________________________

twitch 

type :  divertissement

mot de passe :  mustaphA?85214

score :  90


## Test : maj_mdp()
#### Résultat obtenu :

___________________________
twitch
type :  reseau
mot de passe :  twitch59205
score :  70/100
___________________________
youtube
type :  reseau
mot de passe :  PI%Ha&SE@LA!NE8qA$MY*ji?HI7
score :  100/100
___________________________
Twitch
type :  reseau
mot de passe :  NE5wo5Go*dU6GA6
score :  90/100
___________________________
De quel site voulez vous modifier le mot de passe ?Twitch
Entrez le nouveau mot de passe : projetPython1__

## Test : statistiques()
#### Résultat obtenu :

--- MENU TÂCHES ---
1. Générer
2. Ajouter compte
3. Lister comptes
4. Statistiques
5. Modifier un mot de passe
6. Quitter
Votre choix : 4

La moyenne des scores des mots de passe est de 100.0
