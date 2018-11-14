## Contenu

Ce dépôt contient le matériel utilisé dans un cours d'initiation au langage Python [disponible en ligne](https://mm2act.pages.math.unistra.fr/cours-python).


## Execution des notebooks Jupyter

> **Attention :** Le code présent dans les notebooks de cette formation est compatible uniquement avec python3.

### En utilisant Mybinder

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/fitzinger/cours-python/master)


### À partir d'un serveur jupyter local


#### Installation

##### avec Anaconda

[Anaconda](https://www.continuum.io/downloads) est une suite assez complète et facile à utiliser qui contient entre autres :

- [Jupyter](http://jupyter.org/)
- l'IDE [Spyder](https://github.com/spyder-ide/spyder)
- les bibliothèques de Scipy : Numpy, Pandas, etc.

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter nbextension enable exercise2/main
```

##### avec Pip


Pour installer certains paquets qui ne sont pas dans la distribution Anaconda, il faut utiliser [``pip``](https://pypi.python.org/pypi/pip) (depuis le répertoire racine du projet) :

```bash
pip install -r requirements.txt
jupyter contrib nbextension install --user
jupyter nbextension enable exercise2/main
```

#### Lancement d'un serveur Jupyter

- Soit via l'interface d'Anaconda
- Soit en ligne de commande depuis le répertoire racine du projet :

```
jupyter-notebook
```

## Conversion du notebook Jupyter

### Conversion en html, diaporama et pdf

Utiliser `make` :

```bash
make help
Please use `make <target>' where <target> is one of
  html      to make standalone HTML files
  slides    to make slideshows (use local_reveal=True to run them without internet connection)
  pdf       to compile all notebooks as a single PDF book
Use `make' to run all these targets
```

### Lancer un diaporama

Le résultat se trouve dans le répertoire `build/`.

	
Lancer le diaporama :

```bash
./launch_slide.sh 01-generalites.ipynb [--execute]
```

`--execute` permet d'afficher le résultat d'exécution des cellules.

## Suivi avec Git

Pour éviter des différences indésirables dans git liées aux exécutions des cellules du notebook, on peut utiliser `nbstripout` :

```bash
pip install --upgrade nbstripout
# Depuis le répertoire racine du projet :
nbstripout install
```
## Publication avec Pages

Grâce au fichier [.gitlab-ci.yml](.gitlab-ci.yml), la [version en ligne](https://fitzinger.pages.math.unistra.fr/cours-python) est publiée automatiquement par GitLab Pages à chaque `git push` vers le dépôt GitLab.

