# -*- coding: utf-8 -*-

tup_mois = ('jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
tup_long = (31, (28, 29), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

dic_mois = dict(zip(tup_mois, tup_long))

print('Quel est votre mois de naissance. Choisissez parmi :', tup_mois)
mois_naissance = input('? ')
if mois_naissance in tup_mois:
    print('Il y a {} jours dans votre mois de naissance'.format(dic_mois[mois_naissance]))
else:
    print('Mauvais choix...')
