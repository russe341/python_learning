# Python_learning

Ce dépôt contient mes mini-projets python réalisés dans le cadre de mon apprentissage du language de programmation python.

## Mois_01

### Semaine_1

#### Compétences travaillées:
- Variables
- Listes
- Tuple
- Dictionnaire

#### Mini-projet:
[Gestionnaire d'informations personnelles](Mois_01/Semaine_1/Gestionnaire.py)


### Semaine_2

#### Compétences travaillées:
- Conditions
- for
- while
- range

#### Mini-projet:
[Gestionnaire_compte_bancaire](Mois_01/Semaine_2/Gestionnaire_compte_bancaire)

[convertisseur_devises](Mois_01/Semaine_2/convertisseur_devises)

##### Détails sur le gestionnaire de compte bancaire:
- Authentification demandans le nom du client
- Vérifier si le nom du client se trouve dans la base de données
- Demander au client de choisir une option parmi les 3
- 1) Consulter votre solde
- 2) Déposer de l'argent 
- 3) Retirer de l'argent
- Dans l'options 2 et 3 un montant lui sera demandé

##### Détails sur le convertisseur de devises:
- Un champ demande a l'utilisateur de choisir la devises de son choix 
- Puis un champ récupérant le montant sera afficher lui demandant d'entré le montant
- La chaine de caractère entrer sera vérifier si c'est un nombre sinon
- Il sera transformer en nombre entier

### Semaine_3

#### Compétences travaillées:
- Fonctions
- paramètres
- Boucles
- Simulation de scan réseau

#### Mini-projet:
[scanneur.py](Mois_01/Semaine_3/scanneur.py)

##### Détails sur le scanneur:
- Le programme génère plusieurs adresse ip à l'aide de range()
- Chaque ip est analysé pour vérifier si la machine est active
- Si le dernier octet de l'adresse ip appartient à une liste prédéfinie la machine est considérée comme active
- Pour chaque machine active, le programme scanne une liste de port prédéfinie
- Les ports 22, 80 et 443 sont simulés comme ouvert

### Semaine_4

#### Compétences travaillées:
- Fonctions
- Dictionnaires imbriqué
- Conditions
- Boucles

#### Mini-projet:
[g_i_informatique.py](/Mois_01/Semaine_4/g_i_informatique.py)

##### Détails sur le gestionnaire d'inventaire informatique:
- Le programme affiche un menu contenant les fonctionnalités qu'il prend en compte
- Ajouter équipement
- Consulter équipement
- Modifier état
- Afficher tout
- Un champ récuperant la saisie de l'utilisateur sera afficher lui demandant de choisir une option
- En fonction du choisir de l'utilisateur un resultat lui sera donner
- Chaque action mener par l'utilisateur restera enregistrer jusqu'a ce qu'il quitte le programme


## Projet mensuel:
[soc_monitoring_tool](/Mois_01/Projet_mensuel/soc_monitoring_tool.py)

##### Détails sur le soc_monitoring_tool:
- Une page de presentation est afficher accompagner du premier menu
- Puis un champ de récuperation est afficher demandant a l'utilisateur de choisir une option entre se conncter ou quitter le programme
- Après authentification de l'utilisateur un deuxième menu est afficher contenant les différentes fonctionnalités du programme
- Simule scan réseau
- Simule scan ports
- Simule lecture de log
- Simule statistique
- Simule Alerte
- Un champ de récuperation sera disponible demandant à l'utilisateur de choisir une option selon son besoin
