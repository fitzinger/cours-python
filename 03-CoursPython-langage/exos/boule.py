# -*- coding: utf-8 -*-

def boule_or(*args, **kwargs):
    kwargs['couleur'] = "or"  # seule instruction qui fait une hypothèse sur la fonction boule() 
    return boule(*args, **kwargs)
boule_or(1, 2, rendu='brillant')
