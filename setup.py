#!/usr/bin/env python

from setuptools import setup,find_packages,Extension
from setup_helper import SetupHelper



name = "biowy"
classifiers = [
    'Development Status :: 0 - Beta',
    'Intended Audience :: Science/Research',
    'License :: WYB License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Bio-Informatics',
    ]

# Use the helper
h = SetupHelper(initfile="__init__.py", readmefile="README.md")
h.check_version(name,majorv=2,minorv=7)
h.install_requirements(requires=[])


setup(
    name=name,
    author=h.author,
    author_email=h.email,
    version=h.version,
    license=h.license,
    long_description=h.long_description,
    package_dir={name: '.'},
    packages=[name] + ['.'.join((name,x)) for x in find_packages()],
    include_package_data=True,
    package_data={"biowy.utils.data":["*.*"]},
    classifiers=classifiers,

    zip_safe=False,
    url='http://github.come/wangyibin/biowy',
    description='Python utility libraries on my bioinformatics study,',
    install_requires=['biopython','numpy','pysam','matplotlib'],
    )
