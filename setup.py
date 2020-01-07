#!/usr/bin/env python3
from setuptools import setup

setup(
    name='mkdocs-emailprotect-plugin',
    version='0.1',
    description='Obscure email-addresses from crawlers in MkDocs',
    keywords='mkdocs email spam',
    url='https://www.simple-is-better.org/TODO',
    author='Roland Freikamp',
    author_email='rk@simple-is-better.org',
    license='MIT',
    install_requires=['mkdocs>=1.0.4'],
    packages=["emailprotect"],
    entry_points={
        'mkdocs.plugins': [
            'emailprotect = emailprotect:EmailProtect'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
	'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
