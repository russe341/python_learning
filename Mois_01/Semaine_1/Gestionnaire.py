# Gestionnaire d'information personnelle

nom= "Fayza"
age= 20
ville= "Abjidjan"

competences=["linux", "réseau", "python",]

materiel_informatique=["ordinateur", "routeur", "switch"]

date_de_naissance=(28, "03", 2001)

competences.append("trading")
materiel_informatique.append("câble ethernet")

utilisateur={'nom': nom, 'Age': age, 'Ville': ville}

print("====== Profil =======")

print(f"Nom: {nom}")
print(f"Age: {age}")
print(f"Ville: {ville}")

print("date de naissance:")

print(f"jour: {date_de_naissance[0]}")
print(f"Mois: {date_de_naissance[1]}")
print(f"Année: {date_de_naissance[2]}")

print("Compétences:")

print("-",competences[0])
print("-",competences[1])
print("-",competences[2])

print("Materiel:")
print("-",materiel_informatique[0])
print("-",materiel_informatique[1])
print("-",materiel_informatique[2])