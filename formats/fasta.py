#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
The fasta file parse libraries.
"""



import os
import sys

from Bio import SeqIO, Seq
from bioway.apps.base import ActionDispatcher, OptionParser



def main():
    actions = (
            ('test','test print 124'),
            ("reverse_complement", "reverse_complement sequences from a file to a new file")
            )
    p = ActionDispatcher(actions)
    p.dispatch(globals())


def parsefasta(infasta,item='record'):
    """
    
    """
    f = SeqIO.parse(open(infasta),'fasta')
    return f
def info(infasta):
    """
    Stat the fasta.
    """
    print(212)

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

def reverse_complement(args):
    """
    reverse complement complement_fasta reverse_fasta .

    """
    p = OptionParser(reverse_complement.__doc__)
    opts, args = p.parse_args(args)

    if len(args) < 2:
        sys.exit(not p.print_help())

    complement_fasta, reverse_fasta = args

    with open(complement_fasta) as fa_in:
        with open(reverse_fasta, 'w') as fa_out:
            fa = SeqIO.parse(fa_in,"fasta")
            for record in fa:
                record.seq = Seq.reverse_complement(record.seq)
                SeqIO.write(record, fa_out, "fasta")


class OutPut:
    pass

def test():
    print(123)


if __name__ == "__main__":
    main()
