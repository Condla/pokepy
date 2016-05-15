"""
pokepy setup module
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pokepy',
    version='0.1.0',
    description='A Pokeapi wrapper command line tool',
    long_description=long_description,
    url='https://github.com/condla/pokepy',
    author='Stefan Kupstaitis-Dunkler',
    author_email='stefan.dun@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='Pokeapi REST client wrapper command line interface',
    packages=find_packages(),
    install_requires=['docopt', 'requests'],
    extras_require={ },
    package_data={},
    data_files=[],

    entry_points={
        'console_scripts': [
            'pokepy=pokepy:__main__',
        ],
    },
)
