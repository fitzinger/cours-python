# -*- coding: utf-8 -*-

# Solution simple :

var = 7
print((var >> 0) & 1, (var >> 1) & 1, (var >> 2) & 1)

# Solution réutilisable :

def num2bin(num):
    ret = []
    while num > 0:
        ret.append(str(num & 1))
        num >>= 1
    return ''.join(reversed(ret))

print(num2bin(6))
print(num2bin(7))
print(num2bin(8))
print(num2bin(42))
