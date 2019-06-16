# -*- coding: utf-8 -*-
"""

Created on 2019-06-15 17:46

@author: liubo
"""

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Exampe 1


class OldResisitor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


# Example 2
r0 = OldResisitor(50e3)
print('Before: {}'.format(r0.get_ohms()))
r0.set_ohms(10e3)
print('After {}'.format(r0.get_ohms()))

# Example 3
r0.set_ohms(r0.get_ohms() + 5e3)


# Example 4
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
print("{} {} {}".format(r1.ohms, r1.voltage, r1.current))


# Example 6


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def votage(self):
        return self._voltage

    @votage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


# Example 7
r2 = VoltageResistance(1e3)
print('Before: {} amps'.format(r2.current))
r2.voltage = 10
print('After: {} amps'.format(r2.current))


# Example 8
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('{} ohms must be > 0'.format(ohms))
        self._ohms = ohms


# Example 9
try:
    r3 = BoundedResistance(1e3)
    r3.ohms = 0

except:
    logging.exception('Expected')
else:
    assert False

# Example 10

try:
    BoundedResistance(-5)
except:
    logging.exception('Expected')


# Example 11
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


# Example 12
# try:
#     r4 = FixedResistance(1e3)
#     r4.ohms = 2e3
#
# except:
#     logging.exception('Expected')
# else:
#     assert False


# Example 13
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


# Example 14
print("Example 14")
r7 = MysteriousResistor(10)
r7.current = 0.01
print('Before: {}'.format(r7.voltage))
r7.ohms
print('After: {}'.format(r7.voltage))

















