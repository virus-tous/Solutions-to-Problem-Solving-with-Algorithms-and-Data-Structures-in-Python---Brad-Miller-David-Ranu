# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:01:09 2021

@author: virustous
"""
# Queue: rear -> front
# enqueue to rear
# dequeue from front
import Queue

def hotPotato(names, n):
    q = Queue.Queue()
    for name in names:
        q.enqueue(name)
        
    while q.size() > 1:     
        # when remain more than 1 person, keep playing
        # pass the potato in the circle
        for i in range(n):
            q.enqueue(q.dequeue()) # simulate the circle
        # when music stops, remove the front person (ie holding potato)
        q.dequeue()
    
    # return the winner (last person)
    return q.dequeue()
# end f. hotPotato

names = ['Bill', 'David', 'Susan', 'Jane', 'Ken', 'Brad']
print(hotPotato(names, 0))
print(hotPotato(names, 7))