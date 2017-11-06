# Contenu

Ce dépôt contient le matériel utilisé dans une formation d'initiation au langage Python [disponible en ligne](https://fitzinger.pages.math.unistra.fr/formation-python).

# Utilisation des notebooks Python

## Installation de Jupyter

Le plus simple est d'utiliser [Anaconda](https://www.continuum.io/downloads), une suite assez complète et facile à utiliser qui contient en particulier :

- [Jupyter](http://jupyter.org/)
- l'IDE [Spyder](https://github.com/spyder-ide/spyder)
- les deux versions Python 2 et Python 3
- le gestionnaire de paquets Python ``conda``

> Attention: Le code présent dans les notebooks de cette formation est compatible uniquement avec python3.

Pour installer [Jupyter](https://pypi.python.org/pypi/jupyter) sur une distribution
linux qui ne le propose pas dans son gestionnaire de paquets, il faut utiliser [``pip``](https://pypi.python.org/pypi/pip) :

    sudo pip install jupyter

Pour l'IDE [Spyder](https://pypi.python.org/pypi/spyder), on peut faire de même:

    sudo pip install spyder

## Lancement d'un serveur Jupyter

- Soit via l'utilitaire ``Launcher`` d'Anaconda
- Soit en ligne de commande, par exemple depuis le répertoire de travail des notebooks avec la commande:

```
jupyter-notebook
```

Cette commande ouvre directement une page dans le navigateur par défaut sur [http://localhost:8888/tree](http://localhost:8888/tree).
Sur cette page, il suffit de cliquer sur le nom du notebook pour l'éditer et l'exécuter.

## Conversion du notebook Jupyter

En document pdf :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to pdf
	
Vers le mode diaporama en l'ouvrant dans un navigateur:

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve
	
Lancer le diaporama en utilisant un port différent du port par défaut (afin d'avoir plusieurs diaporamas ouverts) :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve --ServePostProcessor.port=8001 
	
Lancer le diaporama après avoir exécuté toutes les cellules du notebook :

	jupyter-nbconvert 00-InitPython-generalites.ipynb --to slides --post serve --execute


> **Utile :** Insertion d'un bouton de rendu "diaporama" *(live reveal)* dans l'interface d'édition du notebook en installant [RISE](https://github.com/damianavila/RISE).

D'autres exemples de conversion avec

	jupyter-nbconvert -h


## Création de diaporamas à partir des notebooks

Le script `scripts/make_slides.sh` convertit l'ensemble des notebooks en slides reveal qui peuvent être ouverts localement dans un navigateur depuis le répertoire `public/`.
Grâce au fichier [.gitlab-ci.yml](https://gitlab.com/fitzinger/formation-python/blob/master/.gitlab-ci.yml), la  [version en ligne](https://fitzinger.gitlab.io/formation-python) est publiée automatiquement par GitLab Pages à chaque `git push` vers le dépôt GitLab.

## Suivi avec Git

Pour éviter des différences indésirables dans git liées aux exécutions des cellules du notebook, il faut utiliser `nbstripout` :

```
pip install nbstripout
```

Puis dans le répertoire git :

```
nbstripout --install
```

Ce script ajoute une entrée dans `.git/config` qui permet de filtrer les modificactions du fichier notebook liées aux exécutions.