# -*- coding: UTF-8 -*-
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

