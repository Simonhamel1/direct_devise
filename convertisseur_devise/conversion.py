import requests

# Dictionnaire des pays et leurs devises
countries_to_currency = {
    "États-Unis": "USD",
    "Canada": "CAD",
    "Union Européenne": "EUR",
    "Royaume-Uni": "GBP",
    "Japon": "JPY",
    "Australie": "AUD",
    "Suisse": "CHF",
    "Chine": "CNY",
    "Inde": "INR",
    "Russie": "RUB",
    "Brésil": "BRL",
    "Afrique du Sud": "ZAR",
    "Mexique": "MXN"
    # Ajoute ici d'autres pays et devises si nécessaire
}

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
