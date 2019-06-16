# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 01:01

@author: liubo
"""

import logging
from pprint import pprint
from sys import stdout as STDOUT


class Meta(type):
    def __new__(meta, name, bases, class_dict):
        orig_print = __builtins__.print
        print = pprint
        print((meta, name, bases, class_dict))
        print = orig_print
        return type.__new__(meta, name, bases, class_dict)


class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


# Example 3
class ValidatePolygon(type):
    def __new__(meta, name, bases, class_dict):
        if bases != (object,):
            if class_dict['sides'] < 3:
                raise ValueError('Polygons need 3+ seides')
            return type.__new__(meta, name, bases, class_dict)


class Polygon(object, metaclass=ValidatePolygon):
    sides = None

    @classmethod
    def interior_angles(cls):
        return (cls.sides - 2) * 180


# class Triangle(Polygon):
#     sides = 3


# print(Triangle.interior_angles())

# Example 4
print("Example 4")
try:
    print('Before class')


    class Line(Polygon):
        print('Before sides')
        sides = 1
        print('After sides')


    print('After class')
except:
    logging.exception('Excepted')
