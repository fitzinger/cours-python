# -*- coding: utf-8 -*-

def chevalier_ret(repetitions, cri=False):
    ret = 'ni!'
    if cri:
        ret = 'NI!'
    return ret * repetitions

print(chevalier_ret(3, True))
