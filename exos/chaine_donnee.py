# -*- coding: utf-8 -*-

chaine_donnee = "azertyuioppoiuytreza"

milieu = len(chaine_donnee) // 2
print(chaine_donnee[:milieu] + '#' + chaine_donnee[milieu:])

intervale = len(chaine_donnee) // 3
print(chaine_donnee[:intervale] + '@' + chaine_donnee[intervale:2 * intervale + 1] + '@' + chaine_donnee[2 * intervale + 1:])

print('|'.join(chaine_donnee))
