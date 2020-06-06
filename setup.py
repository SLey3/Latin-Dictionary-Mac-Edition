from distutils.core import setup

Project = "Latin Dictionary for Latin I"

VERSION = 1.0

AUTHOR = "Sergio Ley Languren"

EMAIL = "ghub4127@gmail.com"

with open('LICENSE.txt') as f:
    LICENSE = f.read()

with open('README.md') as r:
    Long_Description = r.read()

setup(
    name=Project,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    url='https://github.com/SLey3/Latin-Dictionary-Mac-Edition',
    long_description=Long_Description,
    packages=['Contents', 'Modules']
)