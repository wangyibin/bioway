#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
fasta.
"""


import os
import sys

from Bio import SeqIO
def parsefasta(infasta,item='record'):
    """
    
    """
    f = SeqIO.parse(open(infasta),'fasta')
    return f



def gen_fasize(infasta):
    """
    Generate a tuple of the fasta chromosome size.
    >>>gen_fasize('reference.fasta')
        ('Chr1','3232323')
        ...
        ...
        ('Chr12',3423424)
    """
    f = SeqIO.parse(open(infasta),'fasta')
    for record in f:
        yield (record.id,len(record.seq))


def fasize(infasta):
    """
    Return a dictionary of the fasta chromosome size.
    >>>fasize('reference.fasta')
    {'Chr1':1231231,...}
    """
    fasize_dict = {}
    f = parsefasta(infasta)
    for record in f:
        fasize_dict[record.id] = len(record.seq)
   # for i in gen_fasize(infasta):
    #    fasize_dict[i[0]] = i[1]
    return fasize_dict


class OutPut:
    pass
