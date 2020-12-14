# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 14:30

@author: liubo
"""


import logging


# Example 1
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b'foo')))
print(repr(to_str('foo')))


# Example 2
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value


print(repr(to_bytes(b'foo')))
print(repr(to_bytes('foo')))


# Example 5
try:
    import os
    with open('random.bin', 'w') as f:
        f.write(os.urandom(10))
except:
    logging.exception('Expected')


# Example 6
with open('random.bin', 'wb') as f:
    f.write(os.urandom(10))












