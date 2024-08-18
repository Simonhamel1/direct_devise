from forex_python.converter import CurrencyRates
import requests

def convertir_devise(montant, devise_de, devise_a):
    c = CurrencyRates()
    try:
        print(f"Tentative de récupération du taux de change pour {devise_de} vers {devise_a}")
        # Effectuer une requête manuelle pour voir la réponse brute
        response = requests.get(f"https://api.exchangeratesapi.io/latest?base={devise_de}&symbols={devise_a}")
        print(f"Réponse brute de l'API: {response.text}")
        taux = c.get_rate(devise_de, devise_a)
        print(f"Taux de change récupéré: {taux}")
        montant_converti = montant * taux
        return montant_converti, taux
    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return None, None

if __name__ == "__main__":
    devise_de = input("Entrez la devise de départ (par exemple, USD, EUR) : ").upper()
    devise_a = input("Entrez la devise cible (par exemple, USD, EUR) : ").upper()
    try:
        montant = float(input("Entrez le montant à convertir : "))
    except ValueError:
        print("Le montant doit être un nombre.")
        exit(1)

    resultat, taux = convertir_devise(montant, devise_de, devise_a)
    
    if resultat is not None:
        print(f"{montant} {devise_de} équivaut à {resultat:.2f} {devise_a} (Taux de change: {taux:.4f})")
    else:
        print("La conversion a échoué.")