#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
A library of number parse.
"""
import logging
import numpy as np
import os
import os.path as op
import sys

#from scipy import stats


class OrdNum(object):
    """
    Return the corresponding ordinal number of a number.
    Such as 21>21st; 11>11th; 3>3rd.
    """

    def __init__(self, num):
        self.num = str(num)

    def __str__(self):

        if not self.num.isnumeric():
            print('Please input a number!')

        last2bits = int(str(self.num)[-2:])
        if (last2bits < 10) or (last2bits > 20):
            if last2bits % 10 == 1:
                suffix = 'st'
            elif last2bits % 10 == 2:
                suffix = 'nd'
            elif last2bits % 10 == 3:
                suffix = 'rd'
            else:
                suffix = 'th'
        else:
            suffix = 'th'

        ordnum = '%s%s' % (self.num, suffix)

        return ordnum

    __repr__ = __str__

def get_mode(numlist):
    """
    Caculate the mode value of a lists by numpy.
    >>>get_mode(numlist)
    """
    count = np.bincount(numlist)
    return np.argmax(count)


def get_median(numlist):
    """
    Caculate the median value of a list by numpy.
    >>>get_median(numlist)
    """
    return np.median(numlist)


def get_mean(numlist):
    """
    Caculate the mean value of a list by numpy.
    >>>l = [1,4,5,6,7]
    >>>get_mean(l)
        4.6
    """
    return np.mean(numlist)


def factorial(n, end=1):
    """
    
    """

    if n < end:
        logging.debug("{} is ".format(n))
    elif n == end:
        return end 
    else:
        return n*factorial(n-1,end)



