import requests

def obtenir_taux_change(devise_de, devise_a, api_key):
    try:
        # Construire l'URL avec la clé API et les devises
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{devise_de}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200 or devise_a not in data['conversion_rates']:
            print(f"Erreur : impossible de récupérer le taux pour {devise_de} vers {devise_a}.")
            return None
        
        taux = data['conversion_rates'][devise_a]
        print(f"Taux de change récupéré: {taux}")
        return taux
    except Exception as e:
        print(f"Erreur lors de la récupération du taux de change: {e}")
        return None

def convertir_devise(montant, devise_de, devise_a, api_key):
    taux = obtenir_taux_change(devise_de, devise_a, api_key)
    if taux is not None:
        montant_converti = montant * taux
        return montant_converti, taux
    else:
        return None, None

if __name__ == "__main__":
    api_key = "acd4d552c1ef2f1a183cb14a"  # Ta clé API
    devise_de = input("Entrez la devise de départ (par exemple, USD, EUR) : ").upper()
    devise_a = input("Entrez la devise cible (par exemple, USD, EUR) : ").upper()
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
