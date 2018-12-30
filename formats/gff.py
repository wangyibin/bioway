#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
gff file parse.
"""
import os
import os.path as op
import sys

def gengff(gfffile):
    """
    Generate the record of gffile.
    """
    with open(gfffile,'r')  as f:
        for line in f:
            if line[0] == "#":
                head = line
            else:
                    yield line.rstrip().split()


def gffrecord(gfffile):
    pass

def error(gfffile):
    o = open(".%s"%gfffile,'w') 
    for record in gengff(gfffile):
        try:
            fore = record[:8]
            info = record[8]
            types = record[2]
        except:
            continue

        info_dict = {}
        for item in info.split(';'):
            info_dict[item.split("=")[0]] = item.split("=")[1]
        
        if 'Name' in info_dict:
            info_dict["Name"] = info_dict["ID"]
        if  types == "CDS":
            info_dict["ID"] = info_dict["ID"] + ":cds"
        info = ""
        for key in info_dict:
            info_j = ""
            info_j = key + "=" + info_dict[key]
            info = info + info_j + ";"
        fore = "\t".join(fore) +'\t' +   info.rstrip(";") + "\n"

        o.write(fore)
    o.close()


if __name__ == "__main__":
    error(sys.argv[1])
        

    
            
