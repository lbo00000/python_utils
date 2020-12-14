# -*- coding: utf-8 -*-
"""
Created on 2019/6/12 23:29

@author: LIUBO
"""
import logging
from pprint import pprint
from sys import stdout as STDOUT

# Example 1
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))

# Example 2
from collections import defaultdict


def log_missing():
    print('Key added')
    return 0


# Example 3
current = {'green': 12, 'blue': 3}
increments = [('red', 4), ('blue', 17), ('orange', 9)]
result = defaultdict(log_missing, current)
print('Before', dict(result))
for key, amount in increments:
    result[key] += amount

print('After: ', dict(result))

# Example 4
print("Example 4")


def increment_with_report(current, increment):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


# Example 5
print("Example 5")
result, count = increment_with_report(current, increments)
assert count == 2
print(result)


# Example 6
class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


# Example 7
print("Example 7")
counter = CountMissing()
result = defaultdict(counter.missing, current)
for key, amount in increments:
    result[key] += amount

assert counter.added == 2
print(result)


# Example 8
print("Example 8")
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

# Example 9
counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(result)




