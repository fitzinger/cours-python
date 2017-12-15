# -*- coding: utf-8 -*-

L = "Dans le Python, tout est bon.".split()

# La solution simple et élégante :
print(L[::-1])

# Explications:
# Pas de bornes => valeurs par défaut => on prend tout
# Le pas est de -1 => à l'envers

# La version explicite :
print(L[-1:-len(L)-1:-1])

# Explications :
# On commence à la dernière place
# On s'arrête à la première, exprimée en indices négatifs
# Le pas est de -1 => à l'envers

# Ne pas oublier que les indices vont:
# dans le sens normal : de 0 à 5
# dans le sens contraire : de -1 à -6

# Ne pas oublier que les bornes d'un slice qui prend tout les éléments vont:
# dans le sens normal : de 0 à 6
# dans le sens contraire : de -1 à -7

# La solution "optimale" : elle utilise un iterateur et donc
# ne consomme aucune ressource tant qu'on ne l'utilise pas
print(list(reversed(L)))

# Pour le fun, voici une version fonctionelle récursive
def rev(alist):
    if not alist:
        return []
    return alist[-1:] + rev(alist[:-1])

print(rev(L))