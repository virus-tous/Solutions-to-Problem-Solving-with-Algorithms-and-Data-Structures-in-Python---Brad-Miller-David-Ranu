# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 08:39:39 2021

@author: virustous
"""

import LinkedList

ll = LinkedList.LinkedList()

print(ll.isEmpty())

ll.add(31)
ll.add(77)
ll.add(17)
ll.add(93)
ll.add(26)
ll.add(54)

print(ll.size())
print(ll.search(93))
print(ll.search(92))

ll.remove(17)
print(ll.size())

# my ll traversal
while ll.head != None:
    print(ll.head.getData())
    ll.head = ll.head.getNext()
