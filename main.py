from convertisseur_devise.conversion import convertir_devise, countries_to_currency

if __name__ == "__main__":
    api_key = "acd4d552c1ef2f1a183cb14a"  # Ta clé API

    # Afficher les pays disponibles
    print("Pays disponibles:")
    for country in countries_to_currency:
        print(f"- {country}")

    # Demander à l'utilisateur de sélectionner les pays
    pays_de = input("Entrez le pays de départ : ")
    pays_a = input("Entrez le pays cible : ")

    # Vérifier si les pays sont dans le dictionnaire
    if pays_de not in countries_to_currency or pays_a not in countries_to_currency:
        print("L'un des pays ou les deux ne sont pas disponibles.")
        exit(1)

    # Récupérer les devises correspondantes
    devise_de = countries_to_currency[pays_de]
    devise_a = countries_to_currency[pays_a]

    try:
        montant = float(input("Entrez le montant à convertir : "))
    except ValueError:
        print("Le montant doit être un nombre.")
        exit(1)

    resultat, taux = convertir_devise(montant, devise_de, devise_a, api_key)
    
    if resultat is not None:
        print(f"{montant} {devise_de} équivaut à {resultat:.2f} {devise_a} (Taux de change: {taux:.4f})")
    else:
        print("La conversion a échoué.")
