# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 00:46

@author: liubo
"""
import logging


class LazyDB(object):
    def __int__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for {}'.format(name)
        setattr(self, name, value)
        return value

# Exampel 2
data = LazyDB()
print('Before: ', data.__dict__)
print('foo: ', data.foo)
print('After: ', data.__dict__)


#Example 3
class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__({})'.format(name))
        return super().__getattr__(name)


data = LoggingLazyDB()
print('exist: ', data.exists)
print('foo: {}'.format(data.foo))
print('foo: {}'.format(data.foo))



# Example 4
class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name):
        print('Called __getattribute__({})'.format(name))
        try:
            return super().__getattribute__(name)
        except AttributeError:
            value = 'Value for {}'.format(name)
            setattr(self, name, value)
            return value


data = ValidatingDB()
print('exists: {}'.format(data.exists))
print('foo: {}'.format(data.foo))
print('foo: {}'.format(data.foo))


# Example 5
try:
    class MissingPropertyDB(object):
        def __getattr__(self, name):
            if name == 'bad_name':
                raise AttributeError('{} is missing'.format(name))
            value = 'Value for {}'.format(name)
            setattr(self, name, value)
            return value
    data = MissingPropertyDB()
    data.foo
    data.bad_name
except:
    logging.exception('Expected')


# Example 6
data = LoggingLazyDB()
print('Before:     ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))
print('After:      ', data.__dict__)
print('foo exists: ', hasattr(data, 'foo'))


# Example 7
data = ValidatingDB()
print('foo exists: ', hasattr(data, 'foo'))
print('foo exists: ', hasattr(data, 'foo'))






