import time
from distutils.core import setup
import os

from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

VERSION = os.environ.get('TRAVIS_TAG') or '0.0.0-{}'.format(time.time())

setup(
    name='RGBControlCenter',
    version=VERSION,
    packages=find_packages(),
    url='https://github.com/chestm007/RGBControlCenter',
    license='GPL-2.0',
    author='Max Chesterfield',
    author_email='chestm007@hotmail.com',
    maintainer='Max Chesterfield',
    maintainer_email='chestm007@hotmail.com',
    description='lighting and fan controller for linux_thermaltake_rgb daemon',
    long_description=readme,
    install_requires=[
        "dbus-python",
    ],
    entry_points="""
        [console_scripts]
        RGBControlCenter=RGBControlCenter.main:main
    """,
)