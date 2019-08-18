from setuptools import setup, find_packages
from os import path
from io import open
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
   long_description = f.read()
setup(
   name='datanerdpy',
   version='1.0.0',
   description='Utility Package for Nashville Data Nerds projects',
   long_description=long_description,
   long_description_content_type='text/markdown',
   url='https://github.com/nashville-data-nerds/datanerdpy',
   author='Alex Antonison',
   author_email='adantonison@gmail.com',
   packages=find_packages(exclude=['tests']),
   python_requires='>=3',
   install_requires=['boto3',
                     'configparser',
                     'pandas'
                     ],
   include_package_data=True
)