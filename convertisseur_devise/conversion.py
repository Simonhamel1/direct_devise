import requests

# Dictionnaire des pays et leurs devises
countries_to_currency = {
    "Afghanistan": "AFN",
    "Albanie": "ALL",
    "Algérie": "DZD",
    "Andorre": "EUR",
    "Angola": "AOA",
    "Antigua-et-Barbuda": "XCD",
    "Argentine": "ARS",
    "Arménie": "AMD",
    "Australie": "AUD",
    "Autriche": "EUR",
    "Azerbaïdjan": "AZN",
    "Bahamas": "BSD",
    "Bahreïn": "BHD",
    "Bangladesh": "BDT",
    "Barbade": "BBD",
    "Biélorussie": "BYN",
    "Belgique": "EUR",
    "Belize": "BZD",
    "Bénin": "XOF",
    "Bhoutan": "BTN",
    "Bolivie": "BOB",
    "Bosnie-Herzégovine": "BAM",
    "Botswana": "BWP",
    "Brésil": "BRL",
    "Brunei": "BND",
    "Bulgarie": "BGN",
    "Burkina Faso": "XOF",
    "Burundi": "BIF",
    "Cambodge": "KHR",
    "Cameroun": "XAF",
    "Canada": "CAD",
    "Cap-Vert": "CVE",
    "République Centrafricaine": "XAF",
    "Tchad": "XAF",
    "Chili": "CLP",
    "Chine": "CNY",
    "Colombie": "COP",
    "Comores": "KMF",
    "République du Congo": "XAF",
    "République Démocratique du Congo": "CDF",
    "Costa Rica": "CRC",
    "Croatie": "HRK",
    "Cuba": "CUP",
    "Chypre": "EUR",
    "République Tchèque": "CZK",
    "Danemark": "DKK",
    "Djibouti": "DJF",
    "Dominique": "XCD",
    "République Dominicaine": "DOP",
    "Timor oriental": "USD",
    "Équateur": "USD",
    "Égypte": "EGP",
    "Salvador": "USD",
    "Guinée équatoriale": "XAF",
    "Érythrée": "ERN",
    "Estonie": "EUR",
    "Eswatini": "SZL",
    "Éthiopie": "ETB",
    "Fidji": "FJD",
    "Finlande": "EUR",
    "France": "EUR",
    "Gabon": "XAF",
    "Gambie": "GMD",
    "Géorgie": "GEL",
    "Allemagne": "EUR",
    "Ghana": "GHS",
    "Grèce": "EUR",
    "Grenade": "XCD",
    "Guatemala": "GTQ",
    "Guinée": "GNF",
    "Guinée-Bissau": "XOF",
    "Guyane": "GYD",
    "Haïti": "HTG",
    "Honduras": "HNL",
    "Hongrie": "HUF",
    "Islande": "ISK",
    "Inde": "INR",
    "Indonésie": "IDR",
    "Iran": "IRR",
    "Irak": "IQD",
    "Irlande": "EUR",
    "Israël": "ILS",
    "Italie": "EUR",
    "Côte d'Ivoire": "XOF",
    "Jamaïque": "JMD",
    "Japon": "JPY",
    "Jordanie": "JOD",
    "Kazakhstan": "KZT",
    "Kenya": "KES",
    "Kiribati": "AUD",
    "Koweït": "KWD",
    "Kirghizistan": "KGS",
    "Laos": "LAK",
    "Lettonie": "EUR",
    "Liban": "LBP",
    "Lesotho": "LSL",
    "Liberia": "LRD",
    "Libye": "LYD",
    "Liechtenstein": "CHF",
    "Lituanie": "EUR",
    "Luxembourg": "EUR",
    "Madagascar": "MGA",
    "Malawi": "MWK",
    "Malaisie": "MYR",
    "Maldives": "MVR",
    "Mali": "XOF",
    "Malte": "EUR",
    "Îles Marshall": "USD",
    "Mauritanie": "MRU",
    "Maurice": "MUR",
    "Mexique": "MXN",
    "Micronésie": "USD",
    "Moldavie": "MDL",
    "Monaco": "EUR",
    "Mongolie": "MNT",
    "Monténégro": "EUR",
    "Maroc": "MAD",
    "Mozambique": "MZN",
    "Myanmar": "MMK",
    "Namibie": "NAD",
    "Nauru": "AUD",
    "Népal": "NPR",
    "Pays-Bas": "EUR",
    "Nouvelle-Zélande": "NZD",
    "Nicaragua": "NIO",
    "Niger": "XOF",
    "Nigeria": "NGN",
    "Corée du Nord": "KPW",
    "Norvège": "NOK",
    "Oman": "OMR",
    "Pakistan": "PKR",
    "Palaos": "USD",
    "Panama": "PAB",
    "Papouasie-Nouvelle-Guinée": "PGK",
    "Paraguay": "PYG",
    "Pérou": "PEN",
    "Philippines": "PHP",
    "Pologne": "PLN",
    "Portugal": "EUR",
    "Qatar": "QAR",
    "Roumanie": "RON",
    "Russie": "RUB",
    "Rwanda": "RWF",
    "Saint-Christophe-et-Niévès": "XCD",
    "Sainte-Lucie": "XCD",
    "Saint-Vincent-et-les-Grenadines": "XCD",
    "Samoa": "WST",
    "Saint-Marin": "EUR",
    "Sao Tomé-et-Principe": "STN",
    "Arabie Saoudite": "SAR",
    "Sénégal": "XOF",
    "Serbie": "RSD",
    "Seychelles": "SCR",
    "Sierra Leone": "SLL",
    "Singapour": "SGD",
    "Slovaquie": "EUR",
    "Slovénie": "EUR",
    "Îles Salomon": "SBD",
    "Somalie": "SOS",
    "Afrique du Sud": "ZAR",
    "Corée du Sud": "KRW",
    "Soudan du Sud": "SSP",
    "Espagne": "EUR",
    "Sri Lanka": "LKR",
    "Soudan": "SDG",
    "Suriname": "SRD",
    "Eswatini": "SZL",
    "Suède": "SEK",
    "Suisse": "CHF",
    "Syrie": "SYP",
    "Taïwan": "TWD",
    "Tadjikistan": "TJS",
    "Tanzanie": "TZS",
    "Thaïlande": "THB",
    "Togo": "XOF",
    "Tonga": "TOP",
    "Trinité-et-Tobago": "TTD",
    "Tunisie": "TND",
    "Turquie": "TRY",
    "Turkménistan": "TMT",
    "Tuvalu": "AUD",
    "Ouganda": "UGX",
    "Ukraine": "UAH",
    "Émirats Arabes Unis": "AED",
    "Royaume-Uni": "GBP",
    "États-Unis": "USD",
    "Uruguay": "UYU",
    "Ouzbékistan": "UZS",
    "Vanuatu": "VUV",
    "Vatican": "EUR",
    "Venezuela": "VES",
    "Viêt Nam": "VND",
    "Yémen": "YER",
    "Zambie": "ZMW",
    "Zimbabwe": "ZWL"
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
