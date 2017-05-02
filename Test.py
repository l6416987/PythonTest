# -*- coding: UTF-8 -*-
import Hello
import os
# a = Hello.fun1(10, 20, 30)
# print a
#
#
# # print input('please input: ')
# try:
#     string = open('test.txt', "r")
#     print string.name
# except IOError, e:
#     print e
# else:
#     print "异常出现"
#
# a = 10
# print a

class Student:
    '学生信息类'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

    def getInfo(self):
        print 'name: '+ self.name, "\nage: ", self.age

chao = Student('machao', 18)
wen = Student('mawen', 17)

# chao.getInfo()
# wen.getInfo()
# print Student.count
# print getattr(chao, 'name')
print Student.__dict__
print Student.__doc__
print Student.__name__
print Student.__module__
print Student.__bases__
print '-------------------------------------'

class Printer:
    "打印机基类"
    count = 0

    def __init__(self, string):
        self.string = string

    def print_string(self):
        print '打印---->', self.string

    def get_printinfo(self):
        print Printer.__dict__
        print Printer.__doc__
        print Printer.__name__
        print Printer.__module__
        print Printer.__bases__

class RedPrinter(Printer):
    '子类：红色打印机'
    def __init__(self, string):
        self.string = string

    def print_red(self):
        print '红色打印---->', self.string

    def get_printinfored(self):
        print RedPrinter.__dict__
        print RedPrinter.__doc__
        print RedPrinter.__name__
        print RedPrinter.__module__
        print RedPrinter.__bases__


red = RedPrinter('哈哈哈哈')
red.print_red()
red.get_printinfored()
red.get_printinfo()






