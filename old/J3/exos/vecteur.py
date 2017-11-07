#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Vecteur():
    commentaire = "Cette classe est top"

    def __init__(self, x, y, z):
        self.coord = [x, y, z]

    def __repr__(self):
        """On surcharge l'opérateur __repr__ pour renvoyer
        une chaîne de caractère"""
        s = ''
        for c in self.coord:
            s += '({})\n'.format(c)
        return s

    def __add__(self, v):
        return Vecteur(self.coord[0] + v.coord[0],
                       self.coord[1] + v.coord[1],
                       self.coord[2] + v.coord[2])

    def scal(self, v):
        return (self.coord[0]*v.coord[0] +
                self.coord[1]*v.coord[1] +
                self.coord[2]*v.coord[2])

if __name__ == '__main__':

    v1 = Vecteur(2., 3., 4.)
    v2 = Vecteur(6., 4., 3.)
    print(v1)
    print(v2)
    print(v1 + v2)
    print(v1.scal(v2))
