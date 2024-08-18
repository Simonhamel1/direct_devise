from forex_python.converter import CurrencyRates

def convertir_devise(montant, devise_de, devise_a):
    c = CurrencyRates()
    try:
        taux = c.get_rate(devise_de, devise_a)
        montant_converti = montant * taux
        return montant_converti, taux
    except Exception as e:
        print(f"Erreur lors de la conversion: {e}")
        return None, None

if __name__ == "__main__":
    devise_de = input("Entrez la devise de départ (par exemple, USD, EUR) : ").upper()
    devise_a = input("Entrez la devise cible (par exemple, USD, EUR) : ").upper()
    montant = float(input("Entrez le montant à convertir : "))

    resultat, taux = convertir_devise(montant, devise_de, devise_a)
    
    if resultat is not None:
        print(f"{montant} {devise_de} équivaut à {resultat:.2f} {devise_a} (Taux de change: {taux:.4f})")
    else:
        print("La conversion a échoué.")

