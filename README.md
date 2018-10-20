# bioway utility libraries

Collection of Python libraries to parse bioinformatics files.

| | |
| --- | --- |
| Authors | Yibin Wang ([wangyibin](http://github.com/wangyibin)) |
| Email   | <yibinwang96@outlook.com> |
| License | [BSD](http://creativecommons.org/licenses/BSD/) |

### Table of Contents

<!-- vim markdown-toc GFM -->

* [Introduction](#introduction)
* [Installation](#installation)

## Introduction

## Content

## Installation

The way to install the bioway is:
```bash
cd ~/code # or any directory of your choice
git clone git://github.com/wangyibin/bioway.git
cd bioway
python setup.py install
```
Or:
```bash
cd ~/code 
git clone git://github.com/wangyibin/bioway.git
export PYTHONPATH=~/code:$PYTHONPATH
```

Please replace `~/code` above with whatever you like, but it must
contain `bioway`. To avoid setting `PYTHONPATH` everytime, please insert
the `export` command in your `~/.bashrc` or `~/.bash_profile`.

## Uninstalltion
The way to uninstall the bioway is:
```bash
easy_install -m bioway
```
Or, remove the egg file in your pkgs directory.


