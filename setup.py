from pathlib import Path
from setuptools import setup

from slconf import __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(Path(__file__).parent / fname).read()


def read_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


settings = dict(
    name='slconf',
    packages=['slconf'],
    version=__version__,
    author='cameronwaterman',
    author_email='cameron.waterman@ni.com',
    description='A command-line utility for managing SystemLink Server configurations',
    license='MIT',
    keywords='slconf',
    url='https://github.com/ni/systemlink-configuration-utility',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('test-requirements.txt'),
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
    ]
)

if __name__ == '__main__':
    setup(**settings)
