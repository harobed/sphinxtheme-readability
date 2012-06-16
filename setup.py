# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_description = ''.join([
    open("README.rst").read()
])

setup(
    name='sphinxthemes.readability',
    version='0.0.1',
    url='http://sphinx-themes-readability.readthedocs.org/',
    license='BSD',
    author='Tsuyoshi Tokuda',
    author_email='tokuda109@gmail.com',
    description='Readability sphinx theme',
    long_description=long_description,
    keywords=['Sphinx', 'Readability', 'Theme', 'reStructuredText'],
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'setuptools',
        'docutils',
        'sphinx',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Documentation',
        'Topic :: Text Processing :: Markup'
    ]
)
