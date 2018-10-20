#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ordnum:
    """
    Return the corresponding ordinal number of a number.
    Such as 21>21st; 11>11th; 3>3rd.
    """
    def __init__(self,num):
        self.num = num
    def __str__(self):
        
        if not self.num.isnum:
            print('Please input a number!')
            
        last2bits = int(str(self.num)[-2:])
        if (last2bits < 10) or (last2bits > 20):
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
    
        ordnum = '%d%s'%(self.num,suffix)
        
        return ordnum
    __repr__ = __str__


if __name__ == "__main__":
    
