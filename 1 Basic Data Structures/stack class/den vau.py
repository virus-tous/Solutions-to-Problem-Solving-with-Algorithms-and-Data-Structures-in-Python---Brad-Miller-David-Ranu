# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 12:43:19 2020

@author: virustous
"""

def isLeap(y):
    return (y%400==0) or (y%4==0 and y%100!=0)


class Date:
    def __init__(self, year, month, day):
        daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeap(year):
            daysOfMonths[2] += 1
            
        while (day > daysOfMonths[month]) or (month>12):
            day = int(input('Input a valid day: '))
            month = int(input('Input a valid month: '))
            
        self.__y = year
        self.__m = month
        self.__d = day
        
    def add1day(self):
        daysOfMonths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if isLeap(self.__y):
            daysOfMonths[2] += 1
        if self.__m==12:
            if self.__d == daysOfMonths[12]:
                self.__m = 1
                self.__d = 1
                self.__y += 1
            else:
                self.__d += 1
        else:
            if self.__d == daysOfMonths[self.__m]:
                self.__m += 1
                self.__d = 1
            else:
                self.__d += 1
        return Date(self.__y, self.__m, self.__d)
    
    def __str__(self):
        return 'Date: {}/{}/{}'.format(self.__m, self.__d, self.__y)
# end class Date
        
myBirthday = Date(2016, 2, 28)
print(myBirthday)
print(myBirthday.add1day())

            
                