# -*- coding: utf-8 -*-

taille = float(input('Quelle est votre taille ? '))

if taille >= 2.0:
    print('grand')
elif taille >= 1.70: # La taille moyenne en France
    print('moyen')
else:
    print('petit')
