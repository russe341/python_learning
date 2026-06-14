#Convertisseur de devises
#devise = ["EUR", "USD", "GBP"]
print("=== Convertisseur de devises ===")
print("devises pris en compte:")
print("EUR -> FCFA")
print("USD -> FCFA")
print("GBP -> FCFA")
choix = input("Choississez votre devise ['EUR', 'USD', 'GBP']: ")



match choix:
    case "EUR":
        montant = input("Entrez votre montant: ")
        if not montant.isnumeric():
            print("Veillez entrer un nombre")
            raise SystemExit()

        montant = int(montant)
        resultat = montant * 650
    case "USD":
        montant = input("Entrez votre montant: ")
        if not montant.isnumeric():
            print("Veillez entrer un nombre")
            raise SystemExit()

        montant = int(montant)
        resultat = montant * 500
    case "GBP":
        montant = input("Entrez votre montant: ")
        if not montant.isnumeric():
            print("Veillez entrer un nombre")
            raise SystemExit()

        montant = int(montant)
        resultat = montant * 650
    case _:
        print("Devise non pris en charge pour le moment")
        raise SystemExit()
    

print(f"Le montant en FCFA est: {resultat}")