#!/usr/bin/env python
# -*- coding:utf-8 -*-


def ordnum(num):
    """
    Return the corresponding ordinal number of a number.
    Such as 21>21st; 11>11th; 3>3rd.
    """
    last2bits = int(str(num)[-2:])
    if (last2bits) < 10 or (last2bits > 20):
        if last2bits % 10 == 1:
            suffix = 'st'
        elif last2bits % 10 == 2:
            suffix = 'nd'
        elif last2bits % 10 == 3:
            suffix = 'rd'
        else :
            suffix = 'th'
    else:
        suffix = 'th'
    
    ordnum = str(num) + suffix
    return ordnum
    

