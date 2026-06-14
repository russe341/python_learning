#Gestionnaire de compte bancaire
#Nous avons quatre client avec des montants sur leur compte
#Il y'a que le nom de la personne qui est demander pour qu'il puisse accéder aux différents options
nom = input("Entrez votre nom: ")
solde_drissa = 500000
solde_mohamed = 150000
solde_fayza = 200000
solde_sara = 300000
base_donnees = ["Drissa", "Mohamed", "Fayza", "Sara"]

#cette partie consiste a vérifier si le nom entré est dans la base de données
#si ce n'est pas le cas le programme s'arrête
if nom not in base_donnees:
    print("Désolé, vous n'avez pas de compte chez nous")
    raise SystemExit()
else:
    options = input("Options ['1) Consulter votre solde', '2) Déposer de l'argent', '3) Retirer de l'argent']: ")

match options:
    case "1":
        if nom == "Drissa":
            print(f"Votre solde est: {solde_drissa}")
        elif nom == "Mohamed":
            print(f"Votre solde est: {solde_mohamed}")
        elif nom == "Fayza":
            print(f"Votre solde est: {solde_fayza}")
        else:
            print(f"Votre solde est: {solde_sara}")
    case "2":
        montant_depot = input("Entrez votre montant à dépôt: ")
        #isnumeric() permet de vérifier si la chaîne de caractère est un nombre
        if not montant_depot.isnumeric():
            print("Montant invalid: veillez entré un nombre")
            raise SystemExit()
        montant_depot = int(montant_depot)
        if nom == "Drissa":
            solde_drissa += montant_depot
            print(f"Vous avez reçu un montant de: {montant_depot}")
            print(f"Votre nouveau solde est: {solde_drissa}")
        elif nom == "Mohamed":
            solde_mohamed += montant_depot
            print(f"Vous avez reçu un montant de: {montant_depot}")
            print(f"Votre nouveau solde est: {solde_mohamed}")
        elif nom == "Fayza":
            solde_fayza += montant_depot
            print(f"Vous avez reçu un montant de: {montant_depot}")
            print(f"Votre nouveau solde est: {solde_fayza}")
        else:
            solde_sara += montant_depot
            print(f"Vous avez reçu un montant de: {montant_depot}")
            print(f"Votre nouveau solde est: {solde_sara}")
    case "3":
        montant_retrait = input("Entrez votre montant à retirer: ")
        if not montant_retrait.isnumeric():
            print("Montant invalid: veillez entré un nombre")
            raise SystemExit()
        montant_retrait = int(montant_retrait)
        if nom == "Drissa":
            if solde_drissa < montant_retrait:
                print("Fond insuffisant!")
                raise SystemExit()
            else:
                solde_drissa -= montant_retrait
                print(f"Vous avez retiré un montant de: {montant_retrait}")
                print(f"Votre nouveau solde est: {solde_drissa}")
        elif nom == "Mohamed":
            if solde_mohamed < montant_retrait:
                print("Fond insuffisant!")
                raise SystemExit()
            else:
                solde_mohamed =- montant_retrait
                print(f"Vous avez retiré un montant de: {montant_retrait}")
                print(f"Votre nouveau solde est: {solde_mohamed}")
        elif nom == "Fayza":
            if solde_fayza < montant_retrait:
                print("Fond insuffisant!")
                raise SystemExit()
            else:
                solde_fayza -= montant_retrait
                print(f"Vous avez retiré un montant de: {montant_retrait}")
                print(f"Votre nouveau solde est: {solde_fayza}")
        else:
            if solde_sara < montant_retrait:
                print("Fond insuffisant!")
                raise SystemExit()
            else:
                solde_sara -= montant_retrait
                print(f"Vous avez retiré un montant de: {montant_retrait}")
                print(f"Votre nouveau solde est: {solde_sara}")
    case _:
        print("Options invalid")