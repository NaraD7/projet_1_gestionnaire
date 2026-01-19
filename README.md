📄 Template de README.md
# Générateur de Mots de Passe Sécurisés

## 📝 Description

Application Python permettant de générer des mots de passe sécurisés avec analyse de force et historique. Développé dans le cadre du module 1PRJ1 - Projet Python Fondamental.

## ✨ Fonctionnalités

- ✅ Génération de mots de passe personnalisables (8-50 caractères)
- ✅ Choix des types de caractères (majuscules, minuscules, chiffres, symboles)
- ✅ Analyse de la force du mot de passe (Faible/Moyen/Fort/Très Fort)
- ✅ Historique des 10 derniers mots de passe générés
- ✅ Sauvegarde persistante dans un fichier
- ✅ Interface console intuitive avec menu

## 🛠️ Prérequis

- Python 3.8 ou supérieur
- Modules standard Python (random, string, os, json)

## 🚀 Installation et utilisation

### Installation

```bash
# Cloner le projet
git clone https://github.com/NaraD7/projet_1_gestionnaire
cd projet_1_gestionnaire

# Aucune dépendance externe requise
```

### Lancement

```bash
python3 main.py
```

## 📖 Guide d'utilisation

1. Lancez le programme avec `python3 main.py`
2. Choisissez une option dans le menu :
```
--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter
```
### Exemple d'utilisation

```
--- MENU TÂCHES ---
1. Générer
2. Analyser
3. Ajouter compte
4. Lister comptes
5. Rechercher
6. Statistiques
7. Quitter
Votre choix : 1
Mot de passe généré : bE6HI9Bo*Bi5Qu$

```

## 📁 Structure du projet

```
generateur-mdp/
│
├── main.py              # Code principal
├── sauvegarde_compte.json       # Fichier de sauvegarde (généré automatiquement)
├── README.md            # Documentation
└── .gitignore           # Fichiers ignorés par Git
```

## 🧪 Tests effectués

- ✅ Génération avec tous les types de caractères
- ✅ Gestion des erreurs de saisie
- ✅ Sauvegarde et lecture de l'historique
- ✅ Calcul correct des scores de force

## 👥 Équipe

- **DENIZON Lilian** - Développeur principal
- **Antitene Mustapha** - Développeur
- **Zoumana Laetitia** - Développeur

## 🎓 Contexte pédagogique

Projet réalisé dans le cadre du module **1PRJ1 - Projet Python Fondamental** à l'École IT (Bachelor 1, Unité 1).

**Objectifs pédagogiques :**
- Conception et développement d'un programme Python complet
- Application des bonnes pratiques de programmation (PEP 8)
- Gestion de projet avec Git
- Documentation technique

## 📜 Licence

Projet étudiant - École IT - 2025-2026

## 📧 Contact

Pour toute question : Lilian : 110363@ecole-it.com , Mustapha : 110816@ecole-it.com , Laetitia : 110051@ecole-it.com
