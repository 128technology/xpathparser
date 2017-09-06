###############################################################################
# Copyright (c) 2016-2017 128 Technology, Inc.
# All rights reserved.
###############################################################################

from setuptools import setup

setup(
    name='xpathparser',
    version='1.0.0',
    description=(
        'A fork of the xpath module from the pyang package that parses XPath '
        'strings into tokens'
    ),
    py_modules=['xpathparser'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='BSD'
)
