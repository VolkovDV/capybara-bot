"""
Setup module
"""
from setuptools import find_packages, setup

with open('requirements.txt', encoding='utf-8') as file:
    required = file.read().splitlines()

setup(
      name='capybara-bot',
      version='0.0.2',
      author='Dmitri Volkov',
      author_email='volkovdmvd@gmail.com',
      packages=find_packages(),
      install_requires=required,
      classifiers=[
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
      ],
      )
