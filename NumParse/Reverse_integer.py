#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path as op
import sys

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def isnegative(x):
            """
            :type x: int
            :rtype: bool
            """
            if x < 0:
                return True
            else:
                return False
            
        def rmendzero(x):
            """
            :type x: int
            :rtype: int
            """
            y = str(x)
            if y.endswith('0'):
                y = y[:-1]
                return rmendzero(int(y))
            else:
                return int(y)
        
        x = rmendzero(x)
        if isnegative(x):
            x = str("-") + str(x)[1:][::-1]
        else:
            x = str(x)[::-1]
        return int(x)


if __name__ == "__main__":
    x = sys.argv[1]

    print Solution().reverse(x)
