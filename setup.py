from setuptools import find_packages, setup  # type: ignore
from setuptools.command.test import test as TestCommand  # type: ignore


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest  # type: ignore

        pytest.main(self.test_args)

pypi_name = "nisystemlink-configuration"

def _get_version(name):
    import os

    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, name)
    if not os.path.exists(os.path.join(script_dir, "VERSION")):
        version = "0.1.0"
    else:
        with open(os.path.join(script_dir, "VERSION"), "r") as version_file:
            version = version_file.read().rstrip()
    return version

def _read_contents(file_to_read):
    with open(file_to_read, "r") as f:
        return f.read()


setup(
    name=pypi_name,
    version=_get_version(pypi_name),
    description='A command-line utility for managing SystemLink Server configurations',
    long_description=_read_contents('README.rst'),
    long_description_content_type='text/markdown',
    author='NI',
    maintainer='cameronwaterman',
    maintainer_email='cameron.waterman@ni.com',
    keywords=["nisystemlink", "systemlink"],
    license='MIT',
    packages=find_packages(exclude=["examples", "tests"]),
    url='https://github.com/ni/systemlink-configuration-utility',
    python_requires='>=3.7',
    install_requires=[],
    tests_require=["pytest", "pytest-asyncio"],
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License'
    ],
    cmdclass={"test": PyTest},
    package_data={"": ["VERSION", "*.pyi", "py.typed"]}
)
