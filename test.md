# Fiche de test du gestionnaire de mot de passe

Pour les tests à effectuer il y a :
- voir si l'entrée de lettres dans l'input de ``menu()`` nous retourne une erreur  [x]
- voir si le mot de passe généré respecte les caractéristique demandées


## Test 1 : Entrée de lettre dans l'input du menu 
### Résultat : 
<img width="301" height="647" alt="image" src="https://github.com/user-attachments/assets/0cfec675-0b20-4d6a-9010-4c9a1b8607c2" />

❌ Echec : erreur due à l'implémentation de la comparaison 

<img width="393" height="205" alt="image" src="https://github.com/user-attachments/assets/733e3131-b181-41be-af00-ba240aaeea40" />

#### Correction

<img width="1480" height="1160" alt="image" src="https://github.com/user-attachments/assets/6806c651-f44a-4e5d-a1c6-9ee711e51853" />

<img width="445" height="393" alt="image" src="https://github.com/user-attachments/assets/fcbfd4ff-11a3-44c9-bc81-6c89fe7ef419" />

La gestion des erreurs fonctionne.

## Test 2 : conformité du mot de passe généré 

<img width="269" height="353" alt="image" src="https://github.com/user-attachments/assets/b637c773-889b-4fd4-9bb6-ce86c775ce42" />

✅ Le mot de passe contient bien les caractères spéciaux, le 0 , O et 1 sont retirés, et les majuscules minuscules sont présentes.


