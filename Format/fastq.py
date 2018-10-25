#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
fastq
"""
import os
import sys


class FastqRecord (object):
    def __init__(self):
        pass
    
    def record(self,fq):
        self.fq = fq
        with open(self.fq) as f:
            for line in f:
                self.r = line + next(f) + next(f) + next(f)
                yield self.r



def test(fq):
    for line in FastqRecord(fq).record():
        print(line)

if __name__ == "__main__":
    fq = sys.argv[1]
    test(fq)
