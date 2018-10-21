#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
basic support for running library.
"""
import logging
import os
import os.path as op
import shutil
import sys
import time


def kwargs_parse(parameters,kwargs):
    """
    Parse the kwargs.
    """
    if kwargs:
        for pa in kwargs:
            if pa in parameters:
                parameters[pa] = kwargs[pa]
            else:
                logging.warning("ParameterError:There is not {} in parameters."
                                    "Use the default parameter".format(pa))
    return parameters


def mkdir(dirname, overwrite=False):
    """
    Make directory 
    """
    if op.isdir(dirname):
        if overwrite:
            shutil.rmtree(dirname)
            os.mkdir(dirname)
        else:
            return False
    else: 
        os.mkdir(dirname)

    return True


def splitall(path):
    """
    Split a path to a list.
    
    Example:
    >>>splitall('/public/home/user/code')
    ['public','home','user','code']
    """
    allparts = []
    while True:
        path, p1 = op.split(path)
        if not p1:
            break
        allparts.append(p1)
    allparts = allparts[::-1]
    return allparts


class ActionDispatcher (object):
    """

    """
    def __init__(self, actions):

        self.actions = actions
        if not actions:
            actions = [(None,None)]
        self.valid_actions, self.action_helps = zip(*actions)

    def get_meta(self):
        args = splitall(sys.argv[0])[-3:]
        args[-1] = args[-1].replace(".py", "")
        if args[-2] == "bioway":
            meta = "MODULE"
        elif args[-1] == "__main__":
            meta = "SCRIPT"
        else:
            meta = "ACTION"
        return meta, args

    def print_help(self):
        meta, args = self.get_meta()
        if meta == "MODULE":
            del args[0]
            args[-1] = meta
        elif meta == "SCRIPT":
            args[-1] = meta
        else:
            args[-1] += " " + meta


