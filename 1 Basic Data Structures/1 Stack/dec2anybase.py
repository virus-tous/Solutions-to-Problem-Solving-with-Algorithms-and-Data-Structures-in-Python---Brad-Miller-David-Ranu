# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:18:15 2021

@author: virustous
"""

def dec2anybase(n, base):
    '''convert a decimal number to a number of any base'''
    digits = '0123456789ABCDF'
    res = ''
    if n == 0:
        return '0'
    while n > 0:
        res += digits[n % base]
        n //= base
    return res[::-1]

print(dec2anybase(1000, 2))
print(dec2anybase(1000, 8))
print(dec2anybase(1000, 16))
print(dec2anybase(1000, 7))
print(dec2anybase(25, 8))
print(dec2anybase(256, 16))
print(dec2anybase(26, 26))