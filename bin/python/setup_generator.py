#!/usr/bin/env python
import datetime
import os
import sys
import requests

name = os.path.basename(os.getcwd()).replace('.py','')
version = datetime.datetime.now().strftime('%y-%m-%d')
url="https://pypi.org/pypi/%s/json" % name
r = requests.get(url)
if r.status_code==200:
    version = r.json()['info']['version']

code = """
import setuptools

# PRODUCTION setup.py without classifiers/description/keywords/README/etc
setuptools.setup(
    name='{name}',
    version='{version}',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
""".format(name=name,version=version).strip()
if not os.path.exists('requirements.txt'):
    code = "\n".join(filter(
        lambda s:'install_requires' not in s,
        code.splitlines()
    ))
print(code)
