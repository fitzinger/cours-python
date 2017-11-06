#! /usr/bin/env python
# -*- coding: utf-8 -*-

source = [4,3,2,1]
interm = []
destin = []

def move(a, b):
    if not a:
        raise Exception('Interdit: la colonne source est vide !')
    item = a.pop()
    if b and item > b[-1]:
        raise Exception('Interdit: le disque {} est trop grand pour la colonne destination: {} => {}'.format(item, a, b))
    b.append(item)
    print('Déplaçons {}: source={}, interm={}, destin={}'.format(item, source, interm, destin))

def hanoi(size, source, interm, destin):
    if size > 0:
        hanoi(size - 1, source, destin, interm)
        move(source, destin)
        hanoi(size - 1, interm, source, destin)

hanoi(len(source), source, interm, destin)

assert (source, interm, destin) == ([], [], [4,3,2,1])
