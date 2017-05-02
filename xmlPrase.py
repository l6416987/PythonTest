# -*- coding: UTF-8 -*-
import xml.dom.minidom
from xml.dom.minidom import parse

domTree = xml.dom.minidom.parse('movies.xml')
collection = domTree.documentElement
if collection.hasAttribute('shelf'):
    print "Root element : %s" % collection.getAttribute("shelf")

