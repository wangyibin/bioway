#!/usr/bin/env python
# -*- coding:utf-8 -*-

class FastqRecord (object):
    def __init__(self, fq):
        self.fq = fq
    
    def record(self):
        with open(self.fq) as f:
            for line in f:
                self.r = line + next(f) + next(f) + next(f)
                yield self.r



def test(fq):
    for line in FastqRecord(fq).record():
        print(line)

if __name__ == "__main__":
    import sys
    fq = sys.argv[1]
    test(fq)
