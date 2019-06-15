# -*- coding: utf-8 -*-
"""
Created on 2019/6/13 21:41

@author: LIUBO
"""

import logging
from pprint import pprint
from sys import stdout as STDOUT


class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MychildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

    def times_two(self):
        return self.value * 2


foo = MychildClass()
print(foo.times_two())


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


# Example 3
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# Example 4
foo = OneWay(5)
print('First ordering is (5 * 2) + 5 = {}'.format(foo.value))


# Example 5
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# Example 6
bar = AnotherWay(5)
print('Second ordering still is {}'.format(bar.value))


# Example 7
class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2


# Example 8
class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is {}'.format(foo.value))


# Example 11
# This is pretending to be Python 2 but it's not
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


before_pprint = pprint
pprint(GoodWay.mro())
from pprint import pprint

print(GoodWay.mro())
pprint = pprint


# Example 12
class Explicit(MyBaseClass):
    def __init__(self, value):
        super(Explicit, self).__init__(value)



class Implicit(MyBaseClass):
    def __init__(self, value):
        super(Implicit, self).__init__(value)

implicit = Implicit(10)
print(implicit.value)

print(Explicit(10).value)
print(Implicit(10).value)

assert Explicit(10).value == Implicit(10).value



