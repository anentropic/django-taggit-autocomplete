# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
long_description = open('README.txt').read()
 
setup(
    name='django-taggit-autocomplete',
    version='0.2',
    description='Autocompletion for django-taggit',
    long_description=long_description,
    author='Flavio Curella',
    author_email='flavio.curella@gmail.com',
    url='https://github.com/fcurella/django-taggit-autocomplete',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=[
        'django-taggit',
    ],
) 
