## 1. Installer Anaconda

Téléchargez Anaconda (<https://www.anaconda.com/download>) pour votre système d'exploitation et installez-le.

Pour Linux, ouvrez l'application *Terminal* :

```bash
cd Téléchargements
bash ./Anaconda*.sh
```

## 2. Installer l'extension *Exercise2* pour Jupyter

### 2.1 Soit en ligne de commande

- Windows : *Menu démarrer > Tous les programmes > Anaconda3 (64bits) > Anaconda Prompt*
- Linux ou Mac : ouvrir *Terminal*

Taper :

```bash
conda install -c conda-forge jupyter_contrib_nbextensions
jupyter nbextension enable exercise2/main
```

### 2.2 Soit par l'interface graphique

#### 2.2.1 Installer *jupyter_contrib_nbextensions*

1. Ouvrir Anaconda Navigator :
    - Mac : *Applications/Anaconda-Navigator*
    - Linux ou Mac : dans Terminal tapez `~/anaconda3/bin/anaconda-navigator`
    - Windows : *Menu démarrer > Tous les programmes > Anaconda3 (64bits) > Anaconda Navigator*
- Menu de gauche : *Environments > base (root) > Channels* puis *Add* : entrez `conda-forge` puis *Update channels*
- Menu déroulant *Installed* : sélectionnez *All*
- Dans *Search packages*, entrez `jupyter_contrib_nbextensions`
- Cochez la case devant *jupyter_contrib_nbextensions* puis *Apply* et *Apply* à nouveau dans la fenêtre popup

#### 2.2.2 Installer l'extension *Exercise2*

1. Menu de gauche *Home > Jupyter notebook > Launch*
- Dans votre navigateur, allez sur <http://localhost:8888/nbextensions> ou depuis la page d'accueil du notebook sélectionnez l'onglet de droite *Nbextensions*
- Cochez la case *Exercise2*


