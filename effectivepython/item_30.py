# -*- coding: utf-8 -*-
"""

Created on 2019-06-15 19:05

@author: liubo
"""

import logging
from pprint import pprint
from sys import stdout as STDOUT

# Example 1
from datetime import datetime, timedelta


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota={})'.format(self.quota)


bucket = Bucket(60)
print(bucket)


# Example 2
def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


# Example 3
def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


# Example 4
bucket = Bucket(60)
fill(bucket, 100)
print(bucket)


# Example 5
if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)


# Example 6
if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print(bucket)


# Example 7

class Bucket(object):
    def __init__(self, peried):
        self.period_delta = timedelta(seconds=peried)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return ('Bucket(max_quota={}, quota_consumed={})'.
                format(self.max_quota, self.quota_consumed))

# Example 8
    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

# Example 9
    @quota.setter
    def quota(self, amout):
        delta = self.max_quota - amout
        if amout == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amout
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


# Example 10
bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')

print('Now', bucket)

if deduct(bucket, 3):
    print('Had 3 quota')
else:
    print('Not enough for 3 quota')
print('Still', bucket)














