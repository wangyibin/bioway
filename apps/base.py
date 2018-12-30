#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
basic support for running library.
"""
from __future__ import print_function

import glob
import logging
import os
import os.path as op
import re
import shutil
import subprocess
import sys
import time

from bioway import __copyright__,__version__


BIOWAYHELP = "bioway utility libraries v{0} [{1}]\n".format(__version__,__copyright__)

def main():
    
    actions = (
            ('ls', 'list the file')
            )
    p = ActionDispatcher(actions)
    p.dispatch(globals())


def dmain(mainfile, type="action"):
    cwd = op.dirname(mainfile)
    pyscripts = [x for x in glob(op.join(cwd, "*", '__main__py'))] \
            if type == "module" \
            else glob(op.join(cwd, "*.py"))
    actions = []
    for ps in sorted(pyscripts):
        action = op.basename(op.dirname(ps)) \
                if type == 'module'\
                else op.basename(ps).replace(".py", "")
        if action[0] == "_":
            continue
        pd = get_module_docstring(ps)
        action_help = [x.rstrip(":.,\n") for x in pd.splitlines(True) \
                if len(x.strip()) > 10 and x[0] != "%"][0] \
                if pd else "no docstring found"
        actions.append((action,action_help))
    
    a = ActionDispatcher(actions)
    a.print_help()

def call(cmd,shell=True):
    """
    Modify the call function which shell change to True.
    >>>call(cmd)
    """
    cmd = cmd.split(' ')
    for i in cmd:
        if not i:
            cmd.remove(i)
    subprocess.call(cmd,shell)

def kwargs_parse(parameters,kwargs):
    """
    Parse the kwargs, and return a new parameters dict.

    >>>parameters = kwargs(parameters,kwargs)
    """
    if kwargs:
        for pa in kwargs:
            if pa in parameters:
                parameters[pa] = kwargs[pa]
            else:
                logging.warning("ParameterError:There is not {} in \
                                parameters."
                                "Use the default parameter".format(pa))
    return parameters


def ls(filename):
    """
    List directory except hided file, and return a list.
    >>>ls('.')
        ['1.txt','2.txt','5.txt']
    """
    filelist = os.listdir(filename)
    for i in filelist:
        if i[0] == '.':
            filelist.remove(i)
    return filelist


def pwd():
    """
    Return current work directory, similar to linux pwd.
    >>>pwd()
        '/public1/home/user/code/'
    """
    return os.getcwd()


def touch(filename):
    """
    Create a new file and return bool, similar to linux command touch.
    >>>touch('test.txt')
    """
    path,filen = op.split(filename)
    if not path:
        path = "."
    if filen in os.listdir(path):
        logging.debug("File exist")
        return False
    else:
        f = open(filename,'w')
        f.close()
        return True


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


def must_open(filename,mode='r'):
    """
    Return filehandle
    Deal multifiletype such as .gz .bz2
    """
    if filename.endswith('.gz'):
        fp = gzip.open(filename, mode)
    elif filename.endswith('.bz2'):
        cmd ="" 
class ActionDispatcher (object):
    """
    The action dispatch function.
    Copy from jcvi(https//:github.com/tanghaibao/jcvi)
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

        help = "Usage:\n    python -m {0}\n\n\n".format('.'.join(args))
        help += "Available {0}s:\n".format(meta)
        max_action_len = max(len(action) for action, ah in self.actions)
        for action, action_help in sorted(self.actions):
            action = action.rjust(max_action_len +4)
            help += " | ".join((action, action_help.capitalize() + "\n"))

        help += "\n" + BIOWAYHELP

        sys.stderr.write(help)
        sys.exit(1)

    def dispatch(self, globals):
        from difflib import get_close_matches
        meta = "ACTION"
        if len(sys.argv) == 1:
            self.print_help()

        action = sys.argv[1]

        if not action in self.valid_actions:
            print("[error] {0} not a valid {1}\n".format(action, meta),
                    file=sys.stderr)
            alt = get_close_matches(action, self.valid_actions)
            print("Did you mean one of these?\n\t{0}\n".
                    format(", ".join(alt)), file=sys.stderr)
            self.print_help

        globals[action](sys.argv[2:])

 
def get_module_docstring(filepath):
    """
    
    """
    co = compile(open(filepath).read(), filepath, 'exec')
    if co.co_consts and isinstance(co.co_consts[0], basestring):
        docstring = co.co_consts[0]
    else:
        docstring = None
    retur
    actions = []
    for ps in sorted(pyscripts):
        action = op.basename(op.dirname(ps)) \
                if type == 'module' \
                else op.basename(ps).replace(".py", "")
        if action[0] == "_":
            continue
        pd = get_module_docstring(ps)
        action_help = [x.rstrip(":.,\n") for x in pd.splitlines(True) 
                if len(x.strip()) > 10 and x[0] != '%'][0] \
                if pd else "No docstring found"
        actions.append((action, action_help))
        
    a = ActionDispatcher(actions)
    a.print_help()


class PWD:
    def __init__(self):
        print(os.getcwd())

def key_parse(item):
    """
    parse a string which is key=value to dict.
    """
    d = {}

def fuzzyfinder(user_input,collection):
    """
    fuzzzy matching, to obtain a fuzzy matched list.
    >>>collection = [
                    "user_name",
                    "api_user",
                    "school",
                    "email"
                    ]
    >>>fuzzyfinder("user",collection)
    ["user_name","api_user"]
    """
    suggestions = []
    pattern = ".*?".join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()),match.start(),item))
    
    return [x for _, _, x in sorted(suggestions)]


if __name__ == "__main__":
    main()
