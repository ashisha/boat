#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.0.1'

setup(
        name = 'boat',
        version = VERSION,
        description = 'Instantly transfer files locally over HTTP',
        long_description=open('README.md').read(),
        author = 'Ashish Anand',
        license='MIT',
        keywords=['http', 'file', 'server', 'command line', 'cli'],
        url = 'https://github.com/ashisha/boat',
        packages=find_packages(),
        install_requires = [
            'pyqrcode',
            'Pillow'
            ],
        entry_points={
            'console_scripts': [
                    'boat=boat.boat:main'
                ]
            }
        )
