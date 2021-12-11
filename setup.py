from setuptools import setup

from workdir-context import __version__

setup(
    name='workdir-context',
    version=__version__,

    url='https://github.com/de-cocco/workdir-context',
    author='Dominic Decocco',
    install_requires=['os', 'contextlib']

    py_modules=['workdir-context'],
)
