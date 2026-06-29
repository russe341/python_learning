#LAB 1: gestionnaire d'inventaire informatique

# La fonction afficher_menu() affiche le menu principal du gestionnaire d'inventaire informatique.
def afficher_menu():
    print("========= Menu =========")
    print("1. Ajouter un équipement")
    print("2. Consulter un équipement")
    print("3. Modifier état")
    print("4. Afficher tout")
    print("5. Quitter")

# La fonction ajouter_equipement() permet à l'utilisateur d'ajouter un nouvel équipement à l'inventaire.
def ajouter_equipement():
    identifiant = input("Entrez l'id de l'équipement à ajouter: ")
    type_equipement = input("Le type d'équipement: ")
    etat = input("L'état de l'équipement: ")
    equipement[identifiant]= {"type": type_equipement, "etat": etat}
    print(f"L'equipement {identifiant} à été ajouter avec succès")

# La fonction consulter_equipement() permet à l'utilisateur de consulter les détails d'un équipement.
def consulter_equipement():
    identifiant = input("Entrez l'id de l'équipement à consulter: ")
    if identifiant in equipement:
        print(f"Type: {equipement[identifiant]['type']}")
        print(f"Etat: {equipement[identifiant]['etat']}")
    else:
        print("L'équipement n'existe pas.")

# La fonction modifier_etat() permet à l'utilisateur de modifier l'état d'un équipement.
def modifier_etat():
    identifiant = input("Entrez l'id de l'équipement à modifer: ")
    if identifiant in equipement:
        etat = input("Entrez le nouvel état de l'équipement: ")
        equipement[identifiant]['etat']= etat
        print("L'état de l'équipement a été modifié avec succès.")
        return 
    print("équipement introuvable")
    

# La fonction afficher_tout() permet d'afficher tous les équipements de l'inventaire.
def afficher_tout():
    for identifiant, infos in equipement.items():
        print(f"ID: {identifiant}, Type: {infos['type']}, Etat: {infos['etat']}")
    

# La base de données initiale des équipements est représentée par un dictionnaire appelé "equipement".
equipement = {
    "PC-001": {"type": "Laptop", "etat": "Actif"},
    "PC-002": {"type": "Desktop", "etat": "Maintenance"},
    "RTR-001": {"type": "Routeur", "etat": "Actif"}
    }

# La fonction correspondance_choix() permet de gérer les choix de l'utilisateur dans le menu principal.
def correspondance_choix():
    choix = input("Choisissez une option (1-5): ")
    match choix:
        case "1":
            ajouter_equipement()
        case "2":
            consulter_equipement()
        case "3":
            modifier_etat()
        case "4":
            afficher_tout()
        case "5":
            print("Au revoir!")
            raise SystemExit()
        case _:
            print("Choix invalide. Veuillez réessayer.")

while True:
    afficher_menu()
    correspondance_choix()
