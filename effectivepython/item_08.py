# -*- coding: utf-8 -*-
"""

Created on 2019-06-16 15:56

@author: liubo
"""




# Example 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flag = [x for row in matrix for x in row]
print(flag)
