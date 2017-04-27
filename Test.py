# -*- coding: UTF-8 -*-
import Hello
import os

a = Hello.fun1(10, 20, 30)
print a


# print input('please input: ')
try:
    string = open('test.txt', "r")
    print string.name
except IOError, e:
    print e
else:
    print "异常出现"

a = 10
print a




