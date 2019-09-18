from setuptools import find_packages, setup

long_desc = open('README.md', 'r').read() 

setup(
    name='Spitzer',
    version='0.01',
    description='A scanner for the first day of a pentest',
    long_description=long_desc,
    author='Rick Theeuwes',
    packages=find_packages(),
    entry_points=
    {'console_scripts': ['spitzer = Spitzer.main:main']},
    install_requires=['xmltodict', 'python-nmap'],
    include_package_data=True
)