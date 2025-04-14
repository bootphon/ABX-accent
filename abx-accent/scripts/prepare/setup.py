#!/usr/bin/env python
# Copyright KHENTOUT Manel, CoML
#
# This file is part of prepare step: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with abkhazia. If not, see <http://www.gnu.org/licenses/>.
"""Setup script for the abkhazia package"""

import os
import abkhazia
from setuptools import setup, find_packages

# Constants and configuration
GITHUB_BOOTPHON = 'https://github.com/bootphon/'
SETUP_DIR = os.path.dirname(os.path.abspath(__file__))
VERSION = abkhazia.__version__

# Check if running on ReadTheDocs
ON_RTD = os.environ.get('READTHEDOCS', None) == 'True'

# Dependencies
REQUIREMENTS = [] if ON_RTD else [
    'numpy',
    'progressbar2',
    'joblib',
    'argcomplete',
    'pytest',
    'Sphinx',
    'h5features',
    'phonemizer',
    'matplotlib'
]

# Read long description from README
with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    # Package information
    name='abkhazia',
    version=VERSION,
    packages=find_packages(exclude=['test']),
    zip_safe=False,
    
    # Dependencies
    install_requires=REQUIREMENTS,
    
    # Data files and resources
    package_data={'abkhazia': ['share/*.*']},
    
    # Entry points
    entry_points={
        'console_scripts': [
            'abkhazia = abkhazia.commands.abkhazia_main:main'
        ]
    },
    
    # Metadata for PyPI
    author='Thomas Schatz, Mathieu Bernard, Manel Khentout, Roland Thiolliere, Xuan-Nga Cao',
    author_email='manelkhentoutmk@gmail.com',
    description='ABX and Kaldi experiments on speech corpora made easy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL3',
    keywords='speech corpus ASR kaldi ABX',
    url='https://github.com/bootphon/abkhazia',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.6',
)
