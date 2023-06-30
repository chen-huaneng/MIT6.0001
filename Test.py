# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:52:23 2023

@author: Abel
"""
# import copy
# L = [2]
# L1 = [L]
# L2 = [[L1]]
# L3 = copy.deepcopy(L2)
# L.append(3)
# print(f'L1 = {L1},L2 = {L2},L3 = {L3}')
# L1 = [2]
# L2 = [L1,L1]
# L3 = copy.deepcopy(L2)
# L3[0].append(3)
# print(L3)
# L1 = [2]
# L1.append(L1)
# print(L1[1][1][1])
# a = [x for x in range(2, 100) if not all((x % y) != 0 for y in range(2, x))]
# print(a)
# def f(L1,L2):
# """_summary_
# L1,L2 lists of same length of numbers
# returns the sum of raising each element in L1
# to the power of the element at the same index in L2
# For example, f([1,2],[2,3]) returns 9
# """
# total = 0
# for i in map(lambda x,y:x**y, L1,L2):
# total += i
# return total
# print(f([1,2], [2,3]))
# def get_mid(d):
#     """
#     returns the value in d with the key that occurs first in the alphabet.
#     E.g., if d = {x = 11, b = 12},get_min returns 12.
#     Args:
#     d (dict): a dict mapping letters to ints
#     """
#     a = []
#     for key,val in d.items():
#         a.append(key)
#     a.sort()
#     return d[a[0]]
# print(get_mid({'x': 11,'b': 12}))
# a = 'history'
# for letter in a:
#     print(letter)