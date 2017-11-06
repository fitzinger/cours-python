# -*- coding: utf-8 -*-

def fibo(x):
    if x < 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(8))
