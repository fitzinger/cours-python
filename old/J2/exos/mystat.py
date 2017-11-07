# -*- coding: utf-8 -*-

def stat(*args):
    # votre fonction
    return sum(args), min(args), max(args)

print(stat(1, 4, 6, 9))
