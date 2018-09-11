#! /usr/bin/env python
#
# Copyright (C) 2018 Michal Jamry


from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'numpy>=1.9.3',
    'scipy>=0.14.0',
    'pandas>=0.15.2',
    'matplotlib>=1.4.3',
]

setup(
    name='Abecadels',
    version='0.2predev',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='https://github.com/abecadel',
    url='https://github.com/abecadel/abecadels',
    download_url='https://github.com/abecadel/abecadels',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=INSTALL_REQUIRES,
)
