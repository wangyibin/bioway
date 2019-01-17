#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time: 2019/1/10 22:11


import logging
import os
import os.path as op
import six
import sys

from bioway.apps.base import ActionDispatcher, OptionParser, must_open
from bioway.apps.base import debug, kwargs_parse
from bioway.apps.font import yellow, blue, red
from bioway.apps.numparse import OrdNum

debug()


class BaseFile(object):
    """
    An object of file handle.
    """
    def __init__(self, filename):
        self.filename = filename

        if filename:
            logging.debug("Loading file `{}`...".format(filename))



class LineFile(BaseFile, list):
    """
    Parse line file, and return a list. It also can assign column to extract it to
     a list.
    """
    def __init__(self, filename, coln=-1, comment=None,sep=None, **kwargs):

        super(LineFile, self).__init__(filename)
        self.filename = filename
        # default_param = {
        #     "comment": None,
        #     #"head": 0,
        #     #"load": False
        # }
        # params = kwargs_parse(kwargs, default_param)


        fp = must_open(filename)
        if coln == -1:
            self.extend([i.strip() for i in fp
                        if not i.startswith(comment)])
            logging.debug("Loaded {0} lines from `{1}` to a list and excluded "
                        "comment line".format(len(self), self.filename))
        else:
            try:
                self.extend([i.strip().split(sep)[coln] for i in fp
                             if not i.startswith(comment)])
                logging.debug("Loaded the {0} column of file `{1}` in a list and"
                              " excluded the comment lines".format(OrdNum(coln)
                                                                   ,self.filename))
            except IndexError as e:
                logging.error("{0}: This file hasn't {1} column.".format(e,yellow(OrdNum(coln))))
        # if params["head"]:
        #     self.header = ""
        #     for i in range(0,head):
        #         self.header += fp.readline()
        # if kwargs:
        #     for param, value in kwargs.items():
        #         if param not in default_param:
        #             kwargs.pop(param)
        #             logging.warning("")
        #     for param, default in default_param:
        #         kwargs[param] = kwargs.get(param, default)

    def __str__(self):
        return "\n".join(self)



class DictFile(BaseFile, dict):
    """
    Gen
    """
    def __init__(self, filename, keypos=0, valuepos=1, sep=None, head=0):
        super(DictFile, self).__init__(filename)
        self.filename = filename

        fp = must_open(filename)
        valuepos = valuepos if not valuepos else -1
        colns = max(keypos, valuepos) + 1
        curr_colns = 0
        if head:
            for i in range(head):
                pass

        for lineno, line in enumerate(fp):
            line = line.rstrip()
            line_list = line.split(sep)
            curr_colns = len(line_list)
            if curr_colns < colns:
                logging.error("Must contain >= {0} columns. {1}.\n"
                              "  --> Lint {2}: {3}".format(colns, "",
                                                        lineno + 1, line))
            key = line_list[keypos]
            value = line_list[valuepos] if (valuepos != -1) else line_list

            self[line_list[keypos]] = line_list[valuepos]

        logging.debug("")





