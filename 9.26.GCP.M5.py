# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:06:56 2022

@author: jingy
"""

import math

def any_odd(values):
    # Supposed to determine whether any value in the list is odd.
    for v in values:
        if v % 2 == 1:
            return True
            break

def mean(values):
    total_sum = 0
    for value in values:
        total_sum += value
    average = total_sum/(len(values))
    return average

def median(values):
    length = len(values)
    if length%2 == 1:
        index = length/2 - 0.5
        return values[int(index)]
    elif length%2 == 0:
        median = (values[int(length/2)] + values[int(length/2 - 1)]) / 2
        return median
    
def q1(values):
    med = median(values)
    nums = []
    for value in values:
        if value<med:
            nums.append(value)
    return median(nums)

def q3(values):
    med = median(values)
    nums = []
    for value in values:
        if value>med:
            nums.append(value)
    return median(nums)
    
if __name__ == '__main__':
    nums_input = input('Enter values: ')
    nums = list(map(int, nums_input.split()))
    print(f'Median = {median(nums)}\nMean = {mean(nums)}\nQ1 = {q1(nums)}\nQ3 = {q3(nums)}')
    
    
    
    