from setuptools import find_packages, setup

long_desc = open('README.md', 'r').read() 

setup(
    name='Spitzer',
    version='0.1',
    description='A scanner for the first day of a pentest',
    long_description=long_desc,
    author='Rick Theeuwes',
    packages=find_packages(),
    entry_points=
    {'console_scripts': ['spitzer = Spitzer.main:main']},
    install_requires=['xmltodict==0.12.0', 'python-nmap==0.6.1', 'python-docx==0.8.10', 'beautifulsoup4==4.8.1', 'requests==2.22.0'],
    include_package_data=True,
    package_data={'': ['*.json', 'Netwerkservices.docx', 'logo.png']}
)  