# biowy utility libraries

Collection of Python libraries to parse bioinformatics files.

| | |
| --- | --- |
| Authors | Yibin Wang ([wangyibin](http://github.com/wangyibin)) |
| Email   | <yibinwang96@outlook.com> |
| License | [BSD](http://creativecommons.org/licenses/BSD/) |

###Table of Contents

<!-- vim markdown-toc GFM -->

* [Introduction](#introduction)
* [Installation](#installation)

## Introduction

## Content

## Installation

The way to install the biowy is:
```bash
cd ~/code # or any directory of your choice
git clone git://github.com/wangyibin/biowy.git
cd biowy
python setup.py install
```
Or:
```bash
cd ~/code 
git clone git://github.com/wangyibin/biowy.git
export PYTHONPATH=~/code:$PYTHONPATH
```

Please replace `~/code` above with whatever you like, but it must
contain `biowy`. To avoid setting `PYTHONPATH` everytime, please insert
the `export` command in your `~/.bashrc` or `~/.bash_profile`.

## Uninstalltion
The way to uninstall the biowy is:
```bash
easy_install -m biowy
```
Or, remove the egg file in your pkgs directory.


