import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

install_requires = [
    'ipython>=1.0',
    'beatbox',
    'pandas'
]

setup(
    name='jupyter-salesforce',
    packages=['src'],
    version='0.1',
    description='Access to salesforce via ipython',
    long_description=README,
    author='Eyal Trabelsi',
    author_email='eyaltrabelsi@gmail.com',
    url='https://github.com/eyaltrabelsi/jupyter-salesforce',
    keywords=['sql', 'ipython', 'salesforce'],
    install_requires=install_requires
)
