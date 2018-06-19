from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name="pydarn",
    version="0.1dev",
    license="GNU",
    packages=find_packages(exclude=['docs', 'test']),
    author="SuperDARN",
)




