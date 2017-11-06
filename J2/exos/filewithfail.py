# -*- coding: utf-8 -*-

def openfile():
    fn = input('Donnez un chemin de fichier : ')
    try:
        with open(fn, 'rb') as fin:
            print(fin.readline())
            return True
    except OSError as err:
        # Ignore errors while trying to open file
        pass
    return False

print(openfile())
