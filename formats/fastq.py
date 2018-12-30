#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
The fastq file parse libraries.
"""
import os
import sys
import gzip

class FastqRecord (object):
    def __init__(self,fastqfile):
        self.fq = fastqfile
    
    def record(self):
        print self.fq
        with gzip.open(self.fq,'r') as f:
            for line in f:
                self.r = line + next(f) + next(f) + next(f)
                yield self.r



def test(fq):
    for line in FastqRecord(fq).record():
        print(line)

if __name__ == "__main__":
    pass
