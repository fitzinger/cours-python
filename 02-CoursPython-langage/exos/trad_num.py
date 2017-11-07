# -*- coding: utf-8 -*-

# Une solution concise :

trad_num = {'un': 'one', 'deux': 'two', 'trois': 'three'}
print(trad_num['deux'])  # On teste Fr -> En
trad_num.update({valeur: cle for cle, valeur in trad_num.items()})
print(trad_num)

# Une autre solution :

# Des tuples
fr = 'un', 'deux', 'trois'
en = 'one', 'two', 'three'
num = 1, 2, 3

# Des dictionnaires
trad_fr_en = dict(zip(fr, en))
trad_en_fr = dict(zip(en, fr))
trad___num = dict(zip(num, fr))

# Le dico qui fait rien
trad = {}

# Maintenant il peut tout faire
trad.update(trad_fr_en)
trad.update(trad_en_fr)
trad.update(trad___num)

# La preuve
print("'un' \t devient:", trad['un'])
print("'two' \t devient:", trad['two'])
print("3 \t devient:", trad[3])
