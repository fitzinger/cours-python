# -*- coding: utf-8 -*-

def stat(a_list):
    """return sum, min and max of a list as a tuple"""
    return sum(a_list), min(a_list), max(a_list)

print(stat([1, 4, 6, 9]))

def stat(*args):
    """return sum, min and max of a sequence of arguments as a tuple"""
    return sum(args), min(args), max(args)

print(stat(1, 4, 6, 9))
