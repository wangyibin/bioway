#!/usr/bin/env python
# -*- coding:utf-8 -*- 


def list_open(infile,column=1,sep='\t',header=0):
    """
    Open a file, and store in a list.
    """

    olist = []
    with open(infile,'r') as f:
        for line in f:
            olist.append(line.split(sep)[column-1])

    return olist
