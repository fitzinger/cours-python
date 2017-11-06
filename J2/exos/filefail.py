# -*- coding: utf-8 -*-

def openfile():
    fn = input('Donnez un chemin de fichier : ')
    try:
        fin = open(fn, 'rb')
        print(fin.readline())
        fin.close()
        return True
    except OSError as err:
        # Ignore errors while trying to open file
        pass
    return False

print(openfile())
