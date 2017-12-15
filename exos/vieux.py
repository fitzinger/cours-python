#!/usr/bin/env python3
# -*- coding: utf-8 -*-


_AGE_LIMITE = 50

class AgeInvalide(Exception):
    pass

class AgeNegatif(AgeInvalide):
    pass

class AgeMauvaisType(AgeInvalide):
    pass

def vieux(age):
    if not isinstance(age, int):
        raise AgeMauvaisType
    if age < 0:
        raise AgeNegatif
    if age == 0:
        raise AgeInvalide
    return age >= _AGE_LIMITE
