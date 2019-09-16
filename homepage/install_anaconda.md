## Installer Anaconda

Télécharger Anaconda (<https://www.anaconda.com/download>) pour le système d'exploitation visé et l'installer.

Pour Linux, ouvrir l'application *Terminal* :

```bash
cd Téléchargements
bash ./Anaconda*.sh
```

## Installer l'extension *Exercise2* pour Jupyter

### Soit en ligne de commande

- Windows : *Menu démarrer > Tous les programmes > Anaconda3 (64bits) > Anaconda Prompt*
- Linux ou Mac : ouvrir *Terminal*

Taper :

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter nbextension enable exercise2/main
```

### Soit par l'interface graphique

#### Installer *jupyter_contrib_nbextensions*

1. Ouvrir Anaconda Navigator :
    - Mac : *Applications/Anaconda-Navigator*
    - Linux ou Mac : dans Terminal taper `~/anaconda3/bin/anaconda-navigator`
    - Windows : *Menu démarrer > Tous les programmes > Anaconda3 (64bits) > Anaconda Navigator*
- Menu de gauche : *Environments > base (root) > Channels* puis *Add* : entrer `conda-forge` puis *Update channels*
- Menu déroulant *Installed* : sélectionner *All*
- Dans *Search packages*, entrer `jupyter_contrib_nbextensions`
- Cocher la case devant *jupyter_contrib_nbextensions* puis *Apply* et *Apply* à nouveau dans la fenêtre popup

#### Installer l'extension *Exercise2*

1. Menu de gauche *Home > Jupyter notebook > Launch*
- Dans un navigateur, aller sur <http://localhost:8888/nbextensions> ou depuis la page d'accueil du notebook sélectionner l'onglet de droite *Nbextensions*
- Cocher la case *Exercise2*


