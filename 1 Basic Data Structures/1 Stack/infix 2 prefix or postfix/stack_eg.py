# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:41:23 2021

@author: virustous
"""

import Stack

st = Stack.Stack()
st.push(1)
st.push(2)
st.push(3)
print(st.peek())
st.pop()
st.pop()
print(st.peek())

print(st.isEmpty())

