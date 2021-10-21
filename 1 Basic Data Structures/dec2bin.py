# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:52:04 2021

@author: virustous
"""

def dec2bin(n):
    s = ''
    while n > 0:
        s += str(n%2)
        n //= 2
    return s[::-1]

print(dec2bin(17))
print(dec2bin(45))
print(dec2bin(96))