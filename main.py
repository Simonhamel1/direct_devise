import difflib
from convertisseur_devise.conversion import convertir_devise, countries_to_currency

if __name__ == "__main__":
    api_key = "acd4d552c1ef2f1a183cb14a"  # Ta clé API

    # Afficher les pays disponibles
    print("Pays disponibles:")
    for country in countries_to_currency:
        print(f"- {country}")

    # Demander à l'utilisateur de sélectionner les pays
    while True:
        pays_de = input("Entrez le pays de départ : ")
        pays_a = input("Entrez le pays cible : ")

        # Trouver les correspondances les plus proches pour les pays
        matches_de = difflib.get_close_matches(pays_de, countries_to_currency.keys(), n=1, cutoff=0.6)
        matches_a = difflib.get_close_matches(pays_a, countries_to_currency.keys(), n=1, cutoff=0.6)

        if matches_de and matches_a:
            pays_de_corrige = matches_de[0]
            pays_a_corrige = matches_a[0]
            break
        else:
            print("Aucune correspondance trouvée pour l'un des pays ou les deux. Veuillez réessayer.")

    print(f"Pays de départ corrigé : {pays_de_corrige}")
    print(f"Pays cible corrigé : {pays_a_corrige}")

    # Vérifier si les pays corrigés sont dans le dictionnaire
    if pays_de_corrige not in countries_to_currency or pays_a_corrige not in countries_to_currency:
        print("L'un des pays ou les deux ne sont pas disponibles.")
        exit(1)

    # Récupérer les devises correspondantes
    devise_de = countries_to_currency[pays_de_corrige]
    devise_a = countries_to_currency[pays_a_corrige]

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