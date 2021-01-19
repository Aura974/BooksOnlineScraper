# Book Scraper
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

# Description

(Projet OpenClassrooms - Parcours DA - Python)

#### Mission

Analyste Marketing chez Books Online, mon responsable m'a demandé de développer une version bêta d'un système qui suit les prix des livres sur le Site [Books to scrape](http://books.toscrape.com/). En pratique, il ne s'agit pas de suivre les prix en temps réel, mais de récupérer les données du site à chaque exécution.

#### En détails

Mon programme est donc un scraper. Il va s'occuper de récupérer les informations suivantes pour chaque livre sur le site :
- Url du livre
- UPC (Universal Product Code)
- Titre
- Prix TTC
- Prix HT
- Nombre d'exemplaires en stock
- Description
- Categorie
- Note (sur 5)
- Url de l'image

Il va ensuite les stocker dans un fichier csv par catégorie et stocker toutes les images dans un dossier séparé.

### Pré-requis

Pour pouvoir exécuter ce programme, il faudra impérativement avoir installé Python 3.9.0 ou supérieur.

> [Dernière version de Python](https://www.python.org/downloads/)


### Installation

1. Clonez le projet depuis Github sur votre ordinateur (bouton "code" en vert)
2. Le mieux est de créer un environnement virtuel dans le dossier mais cette étape est optionnelle
3. Téléchargez les modules requis en entrant cette commande dans votre terminal :

``pip install -r requirements``

## Démarrage

Pour lancer le programme, exécutez le fichier *_main.py_* en lançant cette commande :

``python main.py``

depuis le dossier cloné.

Vous pouvez également lancer le fichier depuis un éditeur de code. 

## Fabriqué avec

Python 3.9.0 (puis 3.9.1)

[Visual Studio Code](https://code.visualstudio.com/) - éditeur de code



