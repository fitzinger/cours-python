# -*- coding: utf-8 -*-

def odds(nums):
    return [n for n in nums if (n % 2) == 1]

print(odds([1,2,3,4,5]))
