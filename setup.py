"""Setup file for mailroom assignment."""
from setuptools import setup

setup(
    name="mailroom",
    description="A Python implementaiton of MailRoom Madness",
    version=0.1,
    author="David Franklin, Allan Liebold",
    license="MIT",
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}
)
