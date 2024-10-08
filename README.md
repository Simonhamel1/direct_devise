# Convertisseur de devises

Ce projet est un convertisseur de devises qui vous permet de convertir un montant d'une devise à une autre. Il utilise l'API ExchangeRate pour obtenir les taux de change en temps réel.

## Installation

1. Clonez ce dépôt GitHub sur votre machine locale.
2. Assurez-vous d'avoir Python 3 installé sur votre machine.
3. Installez les dépendances en exécutant la commande suivante :

```shell
pip install -r requirements.txt
```

## Configuration

1. Obtenez une clé API gratuite sur le site [ExchangeRate-API](https://www.exchangerate-api.com/).
2. Ouvrez le fichier `main.py` et remplacez la variable `api_key` par votre clé API.

## Utilisation

1. Exécutez le fichier `main.py` à l'aide de la commande suivante :

```shell
python main.py
```

2. Suivez les instructions à l'écran pour sélectionner les pays, entrer le montant à convertir, et obtenir le résultat de la conversion.

## Algorithme de suggestion automatique
Le convertisseur de devises inclut une fonctionnalité de suggestion automatique qui corrige les erreurs de saisie lorsque l'utilisateur entre le nom d'un pays.

## Comment ça fonctionne ?
Le programme utilise la distance de Levenshtein, une méthode de calcul de la similarité entre deux chaînes de caractères. Grâce à cette méthode, il est capable de comparer l'entrée de l'utilisateur avec la liste des pays disponibles et de proposer des suggestions en cas de fautes de frappe ou d'erreurs mineures.

Exemple : Si un utilisateur saisit "Fance" au lieu de "France", le programme propose automatiquement la correction suivante :
```shell
Le pays 'Fance' n'est pas trouvé. Vouliez-vous dire : France ?
```
## Pays disponibles

- Afghanistan
- Albanie
- Algérie
- Andorre
- Angola
- Antigua-et-Barbuda
- Argentine
- Arménie
- Australie
- Autriche
- Azerbaïdjan
- Bahamas
- Bahreïn
- Bangladesh
- Barbade
- Biélorussie
- Belgique
- Belize
- Bénin
- Bhoutan
- Bolivie
- Bosnie-Herzégovine
- Botswana
- Brésil
- Brunei
- Bulgarie
- Burkina Faso
- Burundi
- Cambodge
- Cameroun
- Canada
- Cap-Vert
- République Centrafricaine
- Tchad
- Chili
- Chine
- Colombie
- Comores
- République du Congo
- République Démocratique du Congo
- Costa Rica
- Croatie
- Cuba
- Chypre
- République Tchèque
- Danemark
- Djibouti
- Dominique
- République Dominicaine
- Timor oriental
- Équateur
- Égypte
- Salvador
- Guinée équatoriale
- Érythrée
- Estonie
- Eswatini
- Éthiopie
- Fidji
- Finlande
- France
- Gabon
- Gambie
- Géorgie
- Allemagne
- Ghana
- Grèce
- Grenade
- Guatemala
- Guinée
- Guinée-Bissau
- Guyane
- Haïti
- Honduras
- Hongrie
- Islande
- Inde
- Indonésie
- Iran
- Irak
- Irlande
- Israël
- Italie
- Côte d'Ivoire
- Jamaïque
- Japon
- Jordanie
- Kazakhstan
- Kenya
- Kiribati
- Koweït
- Kirghizistan
- Laos
- Lettonie
- Liban
- Lesotho
- Liberia
- Libye
- Liechtenstein
- Lituanie
- Luxembourg
- Madagascar
- Malawi
- Malaisie
- Maldives
- Mali
- Malte
- Îles Marshall
- Mauritanie
- Maurice
- Mexique
- Micronésie
- Moldavie
- Monaco
- Mongolie
- Monténégro
- Maroc
- Mozambique
- Myanmar
- Namibie
- Nauru
- Népal
- Pays-Bas
- Nouvelle-Zélande
- Nicaragua
- Niger
- Nigeria
- Corée du Nord
- Norvège
- Oman
- Pakistan
- Palaos
- Panama
- Papouasie-Nouvelle-Guinée
- Paraguay
- Pérou
- Philippines
- Pologne
- Portugal
- Qatar
- Roumanie
- Russie
- Rwanda
- Saint-Christophe-et-Niévès
- Sainte-Lucie
- Saint-Vincent-et-les-Grenadines
- Samoa
- Saint-Marin
- Sao Tomé-et-Principe
- Arabie Saoudite
- Sénégal
- Serbie
- Seychelles
- Sierra Leone
- Singapour
- Slovaquie
- Slovénie
- Îles Salomon
- Somalie
- Afrique du Sud
- Corée du Sud
- Soudan du Sud
- Espagne
- Sri Lanka
- Soudan
- Suriname
- Eswatini
- Suède
- Suisse
- Syrie
- Taïwan
- Tadjikistan
- Tanzanie
- Thaïlande
- Togo
- Tonga
- Trinité-et-Tobago
- Tunisie
- Turquie
- Turkménistan
- Tuvalu
- Ouganda
- Ukraine
- Émirats Arabes Unis
- Royaume-Uni
- États-Unis
- Uruguay
- Ouzbékistan
- Vanuatu
- Vatican
- Venezuela
- Viêt Nam
- Yémen
- Zambie
- Zimbabwe
