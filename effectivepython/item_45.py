# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 10:19

@author: liubo
"""


import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
from time import localtime, strftime

now = 1407694710
local_tuple = localtime(now)
time_format= '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)


# Example 2
from time import mktime, strptime

time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)


# Example 3
parse_format = '%Y-%m-%d %H:%M:%S'
depart_sfo = '2014-05-01 15:45:16'
time_tuple = strptime(depart_sfo, parse_format)
time_str = strftime(time_format, time_tuple)
print(time_str)



# Example 4
try:
    arrival_nyc = '2014-05-01 23:33:24'
    time_tuple = strptime(arrival_nyc, time_format)
except:
    logging.exception('Expected')


# Example 5
from datetime import datetime, timezone

now = datetime(2014, 8, 10, 18, 18, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(now_local)


# Example 6











