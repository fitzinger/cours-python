# -*- coding: utf-8 -*-

def ttc(liste):
    return sum(liste) * 1.2

liste_prix_ht = [23, 56.20, 19.99, 0.80, .01]
print("%.02f" % ttc(liste_prix_ht))
