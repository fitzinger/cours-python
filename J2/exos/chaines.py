# -*- coding: utf-8 -*-

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

toupper = dict(zip(lower, upper))
tolower = dict(zip(upper, lower))

inverse = dict(toupper)
inverse.update(tolower)

def to_case(chaine, dico):
    ret = []
    for c in chaine:
        d = dico.get(c, None)
        ret . append(d or c)
    return ''.join(ret)

def majuscules(chaine):
    return to_case(chaine, toupper)

def minuscules(chaine):
    return to_case(chaine, tolower)

def inverse_casse(chaine):
    return to_case(chaine, inverse)
    
def nom_propre(chaine):
    return majuscules(chaine[0]) + minuscules(chaine[1:])

print(majuscules('aTtEnTioN'))
print(minuscules('aTtEnTioN'))

print(inverse_casse('aTtEnTioN'))
print(nom_propre('aTtEnTioN'))
