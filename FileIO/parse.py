#/usr/bin/env python
# -*- coding:utf-8 -*- 


import os.path as op
import os
import sys


def checkfile(infile):
    """
    Check a file.
    """
    if op.exists(infile):
        pass
    else:
        e = "No such file or directory:{}.".format(infile)
        raise IOError,e

    
    
def list_open(infile,**kwargs):
    """
    Open a file, and store in a list.
    Usage:list_open(infile,column=1,sep='\\t',header=0)
    """
    parameters = {'column':1,'sep':'\t','header':0}
    
    if kwargs:
        for parameter in kwargs:
            if parameter in parameters:
                parameters[parameter] = kwargs[parameter]
            else:
                print('ParameterError:there is not {} in parameters. '
                        'Use the default parameter'.format(parameter))
    
    column = int(parameters['column'])
    header = int(parameters['header'])
    sep = parameters['sep']
    olist = []


    with open(infile,'r') as f:
        i = 0
        head = ""
        while i < header:
            head = head + f.readline()
            i += 1
        for j,line in enumerate(f):
            try:
                olist.append(line.rstrip().split(sep)[column-1])
            except IndexError,e:
                if column == 1:
                    suffix = 'st'
                elif column == 2:
                    suffix = 'nd'
                elif column == 3:
                    suffix = 'rd'
                else:
                    suffix = 'th'
                print('ColumnError:this file does not contain {0}{1} '
                        'columns'.format(column,suffix))
                break
    
    return olist


def dict_open(infile,key=1,value=2,sep="\t"):
    """
    Open a file and store in a dictory.
    """
    odict = {}
    with open(infile, 'r') as f:
        for line in f:
            keys = line.rstrip().split(sep)[int(key)-1]
            values = line.rstrip().split(sep)[int(value)-1]
            if keys in odict:
                odict[keys].append(values)
            else :
                odict[keys] = [values]

    return odict
