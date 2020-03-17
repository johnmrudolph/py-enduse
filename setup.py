# setup.py
# https://blog.godatadriven.com/setup-py
# pip install e .
from setuptools import setup, find_packages

setup(
    name = 'py-enduse',
    version = '0.1.0',
    author = 'John Rudolph',
    author_email = 'contact@johnmrudolph.com',
    description = ('Python implementation of stock turnover based end-use model'),
    packages = find_packages(),
    install_requires = [
        'numpy',
        'numba',
        'pytest',
        'jupyter',
    ]
)