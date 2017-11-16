# -*- coding: utf-8 -*-

def chevalier_ret(repetitions, cri=False):
    if cri:
        ret = 'NI!'
    else:
        ret = 'ni!'
    return ret * repetitions

print(chevalier_ret(3, True))
