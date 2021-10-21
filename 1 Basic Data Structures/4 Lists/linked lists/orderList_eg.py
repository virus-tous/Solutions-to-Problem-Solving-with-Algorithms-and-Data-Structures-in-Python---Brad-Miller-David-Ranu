# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:45:37 2021

@author: virustous
"""

import OrderedList

l = OrderedList.OrderedList()
print(l.size())

l.add(54)
l.add(26)
l.add(93)
l.add(17)
l.add(17)
l.add(77)
l.add(31)

print(l.size())
l.remove(77)
print(l.size())
print()

while l.head != None:
    print(l.head.getData())
    l.head = l.head.getNext()