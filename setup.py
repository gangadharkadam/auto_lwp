from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='auto_lwp',
    version=version,
    description='Automatic lwp calculation',
    author='Frappe',
    author_email='lwp@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
