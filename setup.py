from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
      name='capybara-bot',
      version='0.0.1',
      author='Dmitri Volkov',
      author_email='volkovdmvd@gmail.com',
      packages=find_packages(),
      install_requires=required,
      )
