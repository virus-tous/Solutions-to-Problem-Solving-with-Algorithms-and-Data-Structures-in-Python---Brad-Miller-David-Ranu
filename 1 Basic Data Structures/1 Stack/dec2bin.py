# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:24:45 2021

@author: virustous
"""

def dec2bin(n):
    binStr = ''
    if n == 0:
        return '0'
    while n > 0:
        binStr += str(n%2)
        n //= 2
    return binStr[::-1]

print(dec2bin(0))
print(dec2bin(1))
print(dec2bin(10))
print(dec2bin(14))